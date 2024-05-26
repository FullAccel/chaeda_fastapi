import json
from fastapi import HTTPException
from matplotlib import pyplot as plt
from AI.extract_data.get_problem_data import get_response_from_claude
from AI.image_segmentation.crop_pieces import model_predict
from cheada.domain.textBook_preprocessing.dto.ProblemInfoDto import ProblemInfoDto
from cheada.domain.textBook_preprocessing.service.image_service import upload_image_to_s3
from cheada.db import crud, models, schemas
from cheada.globalUtils.types import ChapterEnum

import os, fitz, cv2
import numpy as np
import requests
import glob
import shutil

type2id = {
	"수학 상": ["다항식", "방정식", "부등식", "도형의 방정식"],
	"수학 하": ["집합과 명제", "함수", "순열과 조합"],
	"수학 I": ["지수함수와 로그함수", "삼각함수", "수열"],
	"수학 II": ["함수의 극한과 연속", "미분", "적분"],
	"미적분": ["수열의 극한", "미분법", "적분법"],
	"확률과 통계": ["경우의 수", "확률", "통계"],
	"기하": ["이차곡선", "평면벡터", "공간도형과 공간좌표"]
}

def determine_vertical_line(pix, index):
    image_bytes = pix.samples
    image = np.frombuffer(image_bytes, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    if pix.n == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary_image = cv2.threshold(gray_img, 240, 255, cv2.THRESH_BINARY)
    height, width = binary_image.shape
    center = width // 2
    thickness = 20 # 검사할 선의 두께
    center_line = binary_image[100:height-100, center-thickness//2:center+thickness//2]
    
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(center_line, cv2.MORPH_OPEN, kernel)
    
    for r in range(20, opening.shape[0], 20):
        piece = opening[r-20:r, :]
        y_coords, x_coords = np.where(piece == 0)

        if y_coords.size == 0 or np.max(piece) == 0:
            return

        prev_y, prev_x = y_coords[0], x_coords[0]
        for y in y_coords:
            if abs(y-prev_y) >= 5:
                return
            prev_y = y

    # plt.title(f"{index}")
    # plt.imshow(opening, cmap='gray_r')
    # plt.show()
    return True
    
def convert_pdf_to_png(pdf_file, output_folder, pdf_page_number = 0):
    pure_file_name = os.path.basename(pdf_file)[:-4]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    doc = fitz.open(pdf_file)

    
    try:
        if pdf_page_number == 0: # pdf_page_number 특정 값 미지정 시, 전체 변환
            for i, page in enumerate(doc):
                img = page.get_pixmap()   # 이미지 변환
                if determine_vertical_line(pix=img, index=i+1):
                    # img.save(output_folder + "\\" + f'{i}.png') # 변환된 이미지 저장
                    img.save(os.path.join(output_folder, f"{i}.png"))
                
            print('전체 변환')
        elif pdf_page_number != 0:
            page = doc.load_page(pdf_page_number - 1) # 특정 페이지 가져오기
            i = pdf_page_number
            img = page.get_pixmap()   # 이미지 변환
            # img.save(output_folder + "\\" + pure_file_name + f'_{i}_only_output.png') # 변환된 이미지 저장
            img.save(os.path.join(output_folder, pure_file_name, f'_{i}_only_output.png'))
            
            print(pdf_page_number, '페이지 변환')

        
    except ValueError:
        print('Error: page not in document')
    

def start_preprocessing(fileName, local_textbook_dir, temp_page_storage, temp_problem_storage):
    print("\nstart preprocess thread\n")
    # 1. pdf를 png로 바꾸고
    if os.path.exists(temp_page_storage):
        print("해당 문제집은 이미 이미지로 변환된 상태입니다.")
    else:
        print('변환')
        # convert_pdf_to_png(pdf_file=f"{local_textbook_dir}\\{fileName}", output_folder=temp_page_storage)
        convert_pdf_to_png(pdf_file=os.path.join(local_textbook_dir, fileName), output_folder=temp_page_storage)
    
    # 2. png마다 문제 crop하고 추출
    print("2. png마다 문제 crop하고 추출")
    if len(os.listdir(temp_problem_storage)) == 0:
        model_predict(image_dir=temp_page_storage, save_location=temp_problem_storage)
    
    # 3. crop한 문제 s3에 업로드

    # textbook_id 가져오기
    res = requests.get(f"http://127.0.0.1:8000/textbooks/Textbook 10").json()
    # print(res)
    textbook_id = res['id']
    
    for i, page_img in enumerate(os.listdir(temp_problem_storage)): 
        # result = get_response_from_claude(image_path=f"{temp_problem_storage}\\{page_img}", subject="수학 II")
        result = {'category': '미분', 'problem_number': i+15}

        print(result)
        page_num = page_img.split("p")[0]
        
        for eng_chap in ChapterEnum:
            if eng_chap.value == result['category']:
                chapter_eng = eng_chap.name
        print(chapter_eng)
        res = requests.get(f"http://127.0.0.1:8000/math_problem_type/chapter/{chapter_eng}").json()
        type_id = res['id']
        # print(f"type_id: {res['id']}")

        problem = {
                    "type_id": type_id,
                    "textbook_id": textbook_id,
                    "problem_number": str(result['problem_number']),
                    "page_number": page_num,
                    "solved_students_count": 0,
                    "incorrect_students_count": 0,
                    "easy_num": 0,
                    "medium_difficulty_perceived_count": 0,
                    "high_difficulty_perceived_count": 0
                    }
        res = requests.post("http://127.0.0.1:8000/problem/", json=problem)
        print(textbook_id, str(result['problem_number']))

        # s3에 problem 이미지 저장
        problem_info = ProblemInfoDto(subject="수학", publish_year=2024, textbook_name="[블랙라벨] 수학 II", page_num=page_num, problem_num=page_img.split("p")[1][1], image_file_extension="png")
        upload_image_to_s3(problem_info, f"{temp_problem_storage}/{page_img}")
        
        if res.status_code == 200:
            print(f"Problem created successfully.")
            
        else:
            print(f"Failed to create problem: {res.content}")
        
        # if i == 2: break
    shutil.rmtree(temp_page_storage)
    [os.remove(f) for f in glob.glob(os.path.join(temp_problem_storage, "*.png"))]