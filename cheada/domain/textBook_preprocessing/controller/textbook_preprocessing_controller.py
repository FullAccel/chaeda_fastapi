import threading
from fastapi import APIRouter
from pydantic import BaseModel
from cheada.domain.textBook_preprocessing.service import textbook_service


class Data(BaseModel):
    fileName: str


router = APIRouter()


@router.post("/textbook/preprocessing")
async def preprocessing(data: Data):
    fileName = data.fileName
    save_location = "globalUtils/temp_textbook_storage"
    textbook_service.download_textbook_from_s3(filename=fileName, file_location=save_location)

    #현재 spring 서버가 동기로 응답을 기다리고 있기 때문에 전처리하는 과정을 thread를 만들어 비동기로 처리한 후 spring에게
    # 바로 응답을 보내줘야합니다.
    # threading.Thread(target=start_preprocessing, args=(fileName, save_location)).start()
    return True
