import threading
from fastapi import APIRouter
from pydantic import BaseModel
from cheada_fastapi.cheada.domain.textBook_preprocessing.service.preprocessing_service import start_preprocessing
from cheada_fastapi.cheada.domain.textBook_preprocessing.service import textbook_service
from fastapi import FastAPI, HTTPException, Depends
from cheada_fastapi.cheada.domain.textBook_preprocessing.dto import ProblemInfoDto
from cheada_fastapi.cheada.db import schemas, models, crud
from sqlalchemy.orm import Session


class Data(BaseModel):
    fileName: str


router = APIRouter()

@router.post("/textbook/preprocessing")
def preprocessing(data: Data):
    fileName = data.fileName
    s3_textbook_path = f"textbook/2024/{fileName}"
    
    globalUtils_dir = r"C:\Users\aiotu\Projects\GradProj\cheada_fastapi\cheada\globalUtils"
    local_textbook_dir = r"C:\Users\aiotu\Projects\GradProj\books"
    textbook_service.download_textbook_from_s3(filename=s3_textbook_path, file_location=local_textbook_dir)
    
    temp_page_storage = f"{globalUtils_dir}\\temp_page_storage\\{fileName[:-4]}"
    temp_problem_storage = f"{globalUtils_dir}\\temp_problem_storage"

    #현재 spring 서버가 동기로 응답을 기다리고 있기 때문에 전처리하는 과정을 thread를 만들어 비동기로 처리한 후 spring에게
    # 바로 응답을 보내줘야합니다.
    threading.Thread(target=start_preprocessing, args=(fileName, local_textbook_dir, temp_page_storage, temp_problem_storage)).start()
    
    return True
