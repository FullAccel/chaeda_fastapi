import ultralytics
import os, random
from roboflow import Roboflow
from PIL import Image
from cheada.domain.textBook_preprocessing.dto import ProblemInfoDto
import collections
import cv2
import tempfile
import numpy as np
# ultralytics.checks()


def save_temp_image(image):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_path = temp_file.name
    cv2.imwrite(temp_path, image)
    return temp_path

def pil_to_cv2(pil_image):
    rgb_image = pil_image.convert('RGB')
    np_image = np.array(rgb_image)
    cv2_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)
    return cv2_image

def model_predict(image_dir, save_location):
    rf = Roboflow(api_key="wIwiZJgd5Jdz0gp2KcZc")
    project = rf.workspace("myproject-1dhrs").project("math_problem_segmentation")
    model = project.version(5).model

    # page2problems = collections.defaultdict(list)
    
    for i, image in enumerate(os.listdir(rf"{image_dir}")): 
        if i == 10:
            break

        image_path = os.path.join(image_dir, image)
        predictions = model.predict(image_path, confidence=40, overlap=40).json()["predictions"]
        page_num = image.split(".")[0]

        with Image.open(image_path) as img:
            for j, p in enumerate(predictions):
                cx, cy, width, height = p['x'], p['y'], p['width'], p['height']
                left = cx - width // 2
                upper = cy - height // 2
                right = cx + width // 2
                lower = cy + height // 2
                box = (left, upper, right, lower)
                cropped_img = img.crop(box)
                # page2problems[i].append(cropped_img)
                
                # 이미지의 가로 길이 260px에 맞춰 저장
                new_width = 260
                new_height = int((new_width / width) * height)

                new_cropped_img = pil_to_cv2(cropped_img)
                resized_img = cv2.resize(new_cropped_img, (int(new_width), new_height), interpolation=cv2.INTER_LANCZOS4)

                # 샤프닝 필터 적용
                # kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
                # sharpened_image = cv2.filter2D(resized_img, -1, kernel)
                
                # cv2.imwrite(save_location + "\\" + f"{page_num}p_{j}.png", sharpened_image)
                
                cv2.imwrite(os.path.join(save_location, f"{page_num}p_{j}.png"), resized_img)
                
                # problem_info = create_image_file_name(ProblemInfoDto(subject="수학 II", publish_year="2024", textbook_name="블랙라벨", page_num=f'i', problem_num=f'i_j', image_file_extension='.png'))

    
        
