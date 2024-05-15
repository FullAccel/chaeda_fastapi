import uvicorn

from fastapi import Depends, FastAPI, HTTPException
from cheada_fastapi.cheada.domain.textBook_preprocessing.controller.textbook_preprocessing_controller import router as textbook_preprocessing_router
from cheada_fastapi.cheada.db import crud, models, schemas
from cheada_fastapi.cheada.db.database import SessionLocal, engine
from cheada_fastapi.cheada.db.db_router import router as db_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(textbook_preprocessing_router)
app.include_router(db_router)

if __name__ == "__main__" :
    uvicorn.run(app)
