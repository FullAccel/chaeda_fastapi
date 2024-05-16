from cheada.cloud_service_agent.s3 import s3_utils


def download_textbook_from_s3(filename, file_location):
    """
    교재 파일을 s3에 저장하여 file_location에 저장합니다.
    :param filename: s3에 저장된 파일 이름
    :param file_location: 교재 파일을 저장할 로컬 파일 경로
    :return:
    """
    s3_utils.download_file_from_s3(filename, file_location)

