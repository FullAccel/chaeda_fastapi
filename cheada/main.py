from fastapi import FastAPI
import uvicorn
from domain.textBook_preprocessing.controller.textbook_preprocessing_controller import router as textbook_preprocessing_router
from cloud_service_agent.s3 import s3_utils

app = FastAPI()
app.include_router(textbook_preprocessing_router)

if __name__ == "__main__" :
    # s3_utils.download_file_from_s3("s3test.pdf", "C:/Users/aiotu/Projects/GradProj/cheada_fastapi/cheada/globalUtils/temp_textbook_storage")
    uvicorn.run(app)
