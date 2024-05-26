import cv2
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from cheada.cloud_service_agent.s3 import s3_utils
import tempfile

def convert_images_to_pdf(filename, image_folder, output_pdf):
    # 페이지 사이즈 정의 (A4)
    page_width, page_height = A4

    # 이미지 파일 목록 가져오기
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]

    # 이미지 파일 크기 나누기
    threshold = 500
    large_problems = []
    small_problems = []
    img_path_list = []
    for file in image_files:
        img_path = os.path.join(image_folder, file)
        img = cv2.imread(img_path)
        img_height, img_width, _ = img.shape
        if img_height >= threshold:
            large_problems.append(img)
        else:
            small_problems.append(img)
        img_path_list.append(img_path)

    c = canvas.Canvas(output_pdf, pagesize=A4)

    left_page_full = False
    for i, img in enumerate(large_problems):
        img_height, img_width, _ = img.shape
        # 이미지의 높이가 일정 값 이상인 경우에는 절반 구역에 하나만 맨 위에 배치
        # new_height = page_height / 2
        # new_width = int((new_height / img_height) * img_width)
        # resized_img = cv2.resize(img, (new_width, int(new_height)), interpolation=cv2.INTER_AREA)

        # temp_img_path = save_temp_image(resized_img)

        if left_page_full:
            c.drawImage(img_path_list[i], page_width / 2, page_height - img_height - 20)
            c.showPage()
        else:
            c.drawImage(img_path_list[i], 10, page_height - img_height - 20)
        left_page_full != left_page_full

    for i, img in enumerate(small_problems):
        img_height, img_width, _ = img.shape

        # 이미지의 가로 길이를 페이지의 절반에 맞추어 조정
        # new_width = page_width / 2
        # new_height = int((new_width / img_width) * img_height)
        # resized_img = cv2.resize(img, (int(new_width), new_height), interpolation=cv2.INTER_AREA)

        # temp_img_path = save_temp_image(resized_img)

        # 이미지 배치
        if left_page_full:
            if i % 2 == 0:
                c.drawImage(img_path_list[i], page_width / 2, page_height - img_height - 20)
            else:
                c.drawImage(img_path_list[i], page_width / 2, page_height / 2 - img_height - 20)
                left_page_full = False
                c.showPage()
        else:
            if i % 2 == 0:
                c.drawImage(img_path_list[i], 10, page_height - img_height - 20)
            else:
                c.drawImage(img_path_list[i], 10, page_height / 2 - img_height - 20)
                left_page_full = True

    c.save()
    print(f"PDF 파일이 성공적으로 생성되었습니다: {output_pdf}")
    upload_problem_image_from_s3(filename, output_pdf)


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