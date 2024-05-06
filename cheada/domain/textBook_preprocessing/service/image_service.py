import os

from AI.image_segmentation.crop_pieces import model_predict
from cheada_fastapi.cheada.domain.textBook_preprocessing.service.textbook_service import convert_pdf_to_png
from cheada_fastapi.cheada.cloud_service_agent.s3 import s3_utils


def upload_image_to_s3(problemInfoDto, file_location):
    """
    이미지를 s3에 업로드합니다.
    :param problemInfoDto: 이미지파일 이름을 정할 정보가 담겨있는 dto입니다.
    :param file_location: 교재에서 crop한 이미지를 임시저장한 이미지파일의 임시경로입니다
    :return: void
    """
    
    file_name = create_image_file_name(problemInfoDto)
    s3_utils.upload_file_to_s3(file_name, file_location)


def create_image_file_name(problemInfoDto):
    """
    problemInfoDto를 바탕으로 s3에 저장될 이미지 파일 이름을 생성합니다.
    :param problemInfoDto: 이미지파일 이름을 정할 정보가 담겨있는 dto입니다.
    :return: 이미지 파일명
    """
    return f"problem_images/{problemInfoDto.subject}/{problemInfoDto.publish_year}/{problemInfoDto.textbook_name}/{problemInfoDto.page_num}/{problemInfoDto.problem_num}.{problemInfoDto.image_file_extension}"

def start_preprocessing(fileName, save_location):
    print("thread start")
    # 1. pdf를 png로 바꾸고
    pdf_file_path = r"C:\Users\aiotu\Projects\GradProj\books\RPM 수학 I.pdf"
    # pdf_file_name = os.path.basename(pdf_file_path)[:-4]
    output_folder = r"C:\Users\aiotu\Projects\GradProj\AI\image_segmentation\png_files\\" + fileName
    if os.path.exists(output_folder):
        print("해당 문제집은 이미 이미지로 변환된 상태입니다.")
    else:
        convert_pdf_to_png(pdf_file=pdf_file_path, output_folder=output_folder)
    
    # 2. png마다 문제 crop하고 추출
    model_predict(output_folder, save_location)
    
    # 3. crop한 문제 s3에 업로드