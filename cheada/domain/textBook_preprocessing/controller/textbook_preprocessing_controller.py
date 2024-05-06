import threading
from fastapi import APIRouter
from pydantic import BaseModel
from cheada_fastapi.cheada.domain.textBook_preprocessing.service.image_service import start_preprocessing
from cheada_fastapi.cheada.domain.textBook_preprocessing.service import textbook_service
from fastapi import FastAPI, HTTPException, Depends
from cheada_fastapi.cheada.domain.textBook_preprocessing.dto import ProblemInfoDto
from cheada_fastapi.cheada.db import schemas, models, crud
from sqlalchemy.orm import Session
import httpx, os

from db.database import get_db

class Data(BaseModel):
    fileName: str


router = APIRouter()

@router.post("/textbook/preprocessing")
async def preprocessing(data: Data):
    # fileName = data.fileName
    fileName = "textbook/2024/[블랙라벨] 수학 II.pdf"
    # save_location = "globalUtils/temp_textbook_storage"
    save_location = "C:/Users/aiotu/Projects/GradProj/cheada_fastapi/cheada/globalUtils/temp_textbook_storage"
    
    textbook_service.download_textbook_from_s3(filename=fileName, file_location=save_location)

    fileName = (fileName.split('/')[-1])[:-4]
    save_location = "C:/Users/aiotu/Projects/GradProj/cheada_fastapi/cheada/globalUtils/temp_problem_storage"

    #현재 spring 서버가 동기로 응답을 기다리고 있기 때문에 전처리하는 과정을 thread를 만들어 비동기로 처리한 후 spring에게
    # 바로 응답을 보내줘야합니다.
    threading.Thread(target=start_preprocessing, args=(fileName, save_location)).start()
    
    return True

@router.post("/users", response_model=schemas.User)
def create_user(user_info: schemas.UserBase, session: Session = Depends(get_db)):
    db_user = (
        session.query(models.Users)
        .filter(models.Users.nickname == user_info.nickname)
        .first()
    )

    if db_user:
        raise HTTPException(status_code=400, detail="Nickname already registered")
    return crud.create_user(session, user_info)