import threading
from fastapi import APIRouter
from pydantic import BaseModel, Field
from cheada.domain.textBook_preprocessing.service.preprocessing_service import start_preprocessing
from cheada.domain.review_note_maker.service import review_note_service
from typing import List
from cheada.globalUtils.types import ChapterEnum
from enum import Enum
from cheada.globalUtils.global_vars import globalUtils_dir, temp_problem_storage

import os

class FileExtension(Enum):
    PNG = "PNG"


class ReviewNoteProblemInfo(BaseModel):
    incorrect_date: str = Field(..., description='문제를 틀린 날짜', example='2024-05-22')
    image_key: str = Field(..., description='이미지 파일의 고유 키 값', example='10a99bab-4940-48af-92e7-867a56d6ec79')
    file_extension: FileExtension = Field(default=FileExtension.PNG, description='이미지 파일의 확장자')
    answer: str = Field(..., description='문제의 정답', example='42')
    textbook_name: str = Field(..., description='교재 이름', example='쎈 미적분')
    problem_num: str = Field(..., description='문제 번호', example='101')
    chapter: ChapterEnum = Field(..., description='문제가 속한 챕터')


class ReviewNoteMakeRequest(BaseModel):
    filename: str
    memberId: int
    review_note_problem_info_list: List[ReviewNoteProblemInfo]


router = APIRouter()


@router.post("/review-note")
def reviewNoteMaker(data: ReviewNoteMakeRequest):
    fileName = data.filename

    for info in data.review_note_problem_info_list:

        s3_problem_image_path = f"review_note_problem/{data.memberId}/{info.image_key}.png"

        review_note_service.download_problem_image_from_s3(filename=s3_problem_image_path, file_location=temp_problem_storage)

    review_note_service.convert_images_to_pdf(filename=fileName, image_folder=temp_problem_storage, output_pdf=os.path.join(globalUtils_dir, "editted.pdf"))
    return True
