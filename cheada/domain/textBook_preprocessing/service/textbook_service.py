from cheada_fastapi.cheada.cloud_service_agent.s3 import s3_utils
from PIL import Image
import fitz
import os

def download_textbook_from_s3(filename, file_location):
    """
    교재 파일을 s3에 저장하여 file_location에 저장합니다.
    :param filename: s3에 저장된 파일 이름
    :param file_location: 교재 파일을 저장할 로컬 파일 경로
    :return:
    """
    s3_utils.download_file_from_s3(filename, file_location)

def convert_pdf_to_png(pdf_file, output_folder, pdf_page_number = 0):
    file_name = os.path.basename(pdf_file)[:-4].replace(" ", "")

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    
    doc = fitz.open(pdf_file)

    
    try:
        if pdf_page_number == 0: # pdf_page_number 특정 값 미지정 시, 전체 변환
            for i, page in enumerate(doc):
                img = page.get_pixmap()   # 이미지 변환
                img.save(output_folder + "\\" + file_name + f'_{i}_output.png') # 변환된 이미지 저장
            print('전체 변환')
        elif pdf_page_number != 0:
            page = doc.load_page(pdf_page_number - 1) # 특정 페이지 가져오기
            i = pdf_page_number
            img = page.get_pixmap()   # 이미지 변환
            img.save(output_folder + "\\" + file_name + f'_{i}_only_output.png') # 변환된 이미지 저장
            print(pdf_page_number, '페이지 변환')
    except ValueError:
        print('Error: page not in document')
    
