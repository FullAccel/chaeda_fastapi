from cheada.cloud_service_agent.s3 import s3_utils


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

