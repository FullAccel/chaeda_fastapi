import cv2
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os
from cheada.cloud_service_agent.s3 import s3_utils
import tempfile
from PIL import Image
from cheada.globalUtils.global_vars import globalUtils_dir
import logging

def change_dpi(input_path, output_path, index, dpi=(600, 600)):
    # 이미지를 엽니다
    with Image.open(input_path) as img:
        # 이미지를 저장할 때 DPI를 설정합니다
        img.save(os.path.join(output_path, f"{index}_1200.png"), dpi=dpi)
        print(f"Saved {output_path} with DPI {dpi}")


def convert_images_to_pdf(data, filename, image_folder, output_pdf):
    info_list = data.review_note_problem_info_list
    
    # 페이지 사이즈 정의 (A4)
    page_width, page_height = A4

    
    # 이미지 파일 목록 가져오기
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]

    # 이미지 파일 크기 나누기
    threshold = 320
    large_problems = []
    small_problems = []
    for file in image_files:
        img_path = os.path.join(image_folder, file)
        img = cv2.imread(img_path)
        img_height, img_width, _ = img.shape
        if img_height >= threshold:
            large_problems.append((img_path, img))
        else:
            small_problems.append((img_path, img))

    c = canvas.Canvas(output_pdf, pagesize=A4)

    # TTF 파일 경로
    font_path = os.path.join(globalUtils_dir, "NanumBarunGothic.ttf")

    # 폰트 등록
    pdfmetrics.registerFont(TTFont('NanumBarunGothic', font_path))

    # 폰트 설정
    c.setFont('NanumBarunGothic', 10)

    left_page_full = False

    for i, (img_path, img) in enumerate(large_problems):
        logging.info("large_problem 생성 중")
        if i%2 == 0:
            c.drawImage(os.path.join(globalUtils_dir, "template_large.png"), 0, 0, width=page_width, height=page_height)
        img_height, img_width, _ = img.shape
        
        if img_width > 254:
            new_width = 254
            new_height = int((new_width / img_width) * img_height)
            resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
            img_path = save_temp_image(resized_img)
        
        # 이미지 배치
        if left_page_full:
            c.drawImage(img_path, page_width / 2 + 20, page_height - img_height - 14)
            c.setFillColorRGB(0.2, 0.2, 0.2)
            c.setFont('NanumBarunGothic', 10)
            c.drawString(page_width / 2 + 30, page_height / 2 - 354, f'교재: {info_list[i].textbook_name}')
            c.setFillColorRGB(0.2, 0.2, 0.2)
            c.setFont('NanumBarunGothic', 10)
            c.drawString(page_width / 2 + 30, page_height / 2 - 370, f'단원: {info_list[i].chapter.value}')
            c.setFillColorRGB(0.2, 0.2, 0.2)
            c.setFont('NanumBarunGothic', 10)
            c.drawString(page_width / 2 + 30, page_height / 2 - 386, f'정답: {info_list[i].answer}')
            c.showPage()
        else:
            c.drawImage(img_path, 22, page_height - img_height - 14)
            c.setFillColorRGB(0.2, 0.2, 0.2)
            c.setFont('NanumBarunGothic', 10)
            c.drawString(30, page_height / 2 - 354, f'교재: {info_list[i].textbook_name}')
            c.setFillColorRGB(0.2, 0.2, 0.2)
            c.setFont('NanumBarunGothic', 10)
            c.drawString(30, page_height / 2 - 370, f'단원: {info_list[i].chapter.value}')
            c.setFillColorRGB(0.2, 0.2, 0.2)
            c.setFont('NanumBarunGothic', 10)
            c.drawString(30, page_height / 2 - 386, f'정답: {info_list[i].answer}')
            
        left_page_full = not left_page_full

    # 왼쪽 절반만 그리고 끝났을 때
    if left_page_full:
        left_page_full = not left_page_full
        c.showPage()
        
    for i, (img_path, img) in enumerate(small_problems):
        logging.info("small_problems 생성 중")
        if i%4 == 0:
            c.drawImage(os.path.join(globalUtils_dir, "template.png"), 0, 0, width=page_width, height=page_height)
        img_height, img_width, _ = img.shape

        if img_width > 254:
            new_width = 254
            new_height = int((new_width / img_width) * img_height)
            resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
            img_path = save_temp_image(resized_img)
        

        # 이미지 배치
        if left_page_full:
            if i % 2 == 0:
                c.drawImage(img_path, page_width / 2 + 20, page_height - img_height - 24)
                c.setFillColorRGB(0.2, 0.2, 0.2)
                c.setFont('NanumBarunGothic', 10)
                c.drawString(page_width / 2 + 30, page_height / 2 + 51, f'교재: {info_list[i].textbook_name}')
                c.setFillColorRGB(0.2, 0.2, 0.2)
                c.setFont('NanumBarunGothic', 10)
                c.drawString(page_width / 2 + 30, page_height / 2 + 35, f'단원: {info_list[i].chapter.value}')
                c.setFillColorRGB(0.2, 0.2, 0.2)
                c.setFont('NanumBarunGothic', 10)
                c.drawString(page_width / 2 + 30, page_height / 2 + 19, f'정답: {info_list[i].answer}')
            else:
                c.drawImage(img_path, page_width / 2 + 20, page_height / 2 - img_height - 10)
                c.setFillColorRGB(0.2, 0.2, 0.2)
                c.setFont('NanumBarunGothic', 10)
                c.drawString(page_width / 2 + 30, page_height / 2 - 354, f'교재: {info_list[i].textbook_name}')
                c.setFillColorRGB(0.2, 0.2, 0.2)
                c.setFont('NanumBarunGothic', 10)
                c.drawString(page_width / 2 + 30, page_height / 2 - 370, f'단원: {info_list[i].chapter.value}')
                c.setFillColorRGB(0.2, 0.2, 0.2)
                c.setFont('NanumBarunGothic', 10)
                c.drawString(page_width / 2 + 30, page_height / 2 - 386, f'정답: {info_list[i].answer}')
                left_page_full = False
                c.showPage()
        else:
            if i % 2 == 0:
                c.drawImage(img_path, 22, page_height - img_height - 24)
                c.setFillColorRGB(0.2, 0.2, 0.2)
                c.setFont('NanumBarunGothic', 10)
                c.drawString(30, page_height - 369, f'교재: {info_list[i].textbook_name}')
                c.setFillColorRGB(0.2, 0.2, 0.2)
                c.setFont('NanumBarunGothic', 10)
                c.drawString(30, page_height - 385, f'단원: {info_list[i].chapter.value}')
                c.setFillColorRGB(0.2, 0.2, 0.2)
                c.setFont('NanumBarunGothic', 10)
                c.drawString(30, page_height - 401, f'정답: {info_list[i].answer}')
            else:
                c.drawImage(img_path, 22, page_height / 2 - img_height - 10)
                c.setFillColorRGB(0.2, 0.2, 0.2)
                c.setFont('NanumBarunGothic', 10)
                c.drawString(30, page_height / 2 - 354, f'교재: {info_list[i].textbook_name}')
                c.setFillColorRGB(0.2, 0.2, 0.2)
                c.setFont('NanumBarunGothic', 10)
                c.drawString(30, page_height / 2 - 370, f'단원: {info_list[i].chapter.value}')
                c.setFillColorRGB(0.2, 0.2, 0.2)
                c.setFont('NanumBarunGothic', 10)
                c.drawString(30, page_height / 2 - 386, f'정답: {info_list[i].answer}')
                left_page_full = True

    c.save()
    print(f"PDF 파일이 성공적으로 생성되었습니다: {output_pdf}")
    upload_problem_image_from_s3(f'review-note/{data.memberId}/2024-03-27T10:15:30/{filename}.pdf', output_pdf)


def save_temp_image(image):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_path = temp_file.name
    cv2.imwrite(temp_path, image)
    return temp_path


def download_problem_image_from_s3(filename, file_location):
    """

    :param filename:
    :param file_location:
    :return:
    """
    s3_utils.download_file_from_s3(filename, file_location)

def upload_problem_image_from_s3(filename, file_location):
    """

    :param filename:
    :param file_location:
    :return:
    """
    s3_utils.upload_file_to_s3(filename, file_location)