import os
from os import path, makedirs
from botocore.exceptions import NoCredentialsError, ClientError
from pathlib import Path

from globalUtils.loggerConfig import logger
from cloud_service_agent.s3.config.S3Config import client_s3

""" 
[파일 설명]
s3 접근 및 조작에 사용되는 공통 메서드들이 모여있는 util 파일입니다.
"""

def upload_file_to_s3(filename, file_location):
    """
    AWS S3에서 지정된 위치로 파일을 업로드합니다.
    :param filename: s3에 저장될 파일 이름 구조
    :param file_location: 저장할 이미지 파일이 저장된 로컬 시스템의 경로
    :return: None
    :raises ValueError: 파일 이름 매개변수가 비어 있는 경우.
    :raises NoCredentialsError: AWS 자격 증명이 제공되지 않은 경우.
    :raises ClientError: S3에서 파일을 다운로드하는 동안 오류가 발생한 경우.
    :raises Exception: 다운로드 프로세스 중에 알 수 없는 오류가 발생하는 경우.
    """
    filename = str(filename)

    if not filename:
        raise ValueError("파일 이름은 비어 있을 수 없습니다.")

    bucket_name = os.getenv("S3_BUCKET")
    if not bucket_name:
        raise ValueError("환경 변수 S3_BUCKET이 설정되지 않았습니다.")

    if not os.path.isfile(file_location):
        raise FileNotFoundError(f"지정된 위치에 파일이 없습니다: {file_location}")

    try:
        client_s3.upload_file(
            filename=f"{file_location}",
            bucket=bucket_name, #s3 bucket이름
            key=f"{filename}",
            ExtraArgs={'ContentType': 'image/png'}
        )
    except NoCredentialsError as e:
        logger.error("AWS 자격 증명이 제공되지 않았습니다.")
        raise
    except ClientError as e:
        logger.error(f"S3 업로드 중 오류 발생: {e}")
        raise
    except Exception as e:
        logger.error(f"S3 업로드 중 알수 없는 오류 발생: {e}")
        raise

    logger.info(f"{filename} 파일이 S3 버킷 {bucket_name}에 성공적으로 업로드 되었습니다.")


def download_file_from_s3(filename, save_location):
    """
    AWS S3에서 지정된 위치로 파일을 다운로드합니다.

    :param filename: S3의 파일 이름입니다.
    :param save_location: 파일이 저장될 로컬 디렉터리입니다.
    :return: None
    :raises ValueError: 파일 이름 매개변수가 비어 있는 경우.
    :raises NoCredentialsError: AWS 자격 증명이 제공되지 않은 경우.
    :raises ClientError: S3에서 파일을 다운로드하는 동안 오류가 발생한 경우.
    :raises Exception: 다운로드 프로세스 중에 알 수 없는 오류가 발생하는 경우.
    """
    if not filename:
        raise ValueError("파일 이름은 비어 있을 수 없습니다.")

    bucket_name = os.getenv("S3_BUCKET")


    # 'filename'에서 실제 파일 이름 부분만 추출합니다.
    actual_file_name = os.path.basename(filename)

    # save_location과 실제 파일 이름을 합친 경로를 생성합니다.
    filepath = os.path.join(save_location, actual_file_name)

    print(f'파일 이름은 {filename}')
    try:
        client_s3.download_file(
            Bucket=bucket_name,
            Key=filename,
            Filename=filepath
        )
    except NoCredentialsError as e:
        logger.error("AWS 자격 증명이 제공되지 않았습니다.")
        raise
    except ClientError as e:
        logger.error(f"S3 다운로드 중 오류 발생: {e}")
        raise
    except Exception as e:
        logger.error(f"S3 업로드 중 알수 없는 오류 발생: {e}")
        raise

    logger.info(f"{filename} 파일이 S3 버킷 {bucket_name}에서 {save_location}로 성공적으로 다운로드 되었습니다.")
