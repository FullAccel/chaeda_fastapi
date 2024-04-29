from fastapi import FastAPI
import uvicorn
from cheada.domain.textBook_preprocessing.controller.textbook_preprocessing_controller import router as textbook_preprocessing_router

app = FastAPI()
app.include_router(textbook_preprocessing_router)

if __name__ == "__main__" :
	uvicorn.run(app)