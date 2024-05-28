import uvicorn

from fastapi import Depends, FastAPI, HTTPException
from cheada.domain.textBook_preprocessing.controller.textbook_preprocessing_controller import router as textbook_preprocessing_router
from cheada.domain.review_note_maker.controller.review_note_maker_controller import router as review_note_maker_router
from cheada.db import crud, models, schemas
from cheada.db.database import SessionLocal, engine
from cheada.db.db_router import router as db_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(textbook_preprocessing_router)
app.include_router(review_note_maker_router)
app.include_router(db_router)

if __name__ == "__main__" :
    uvicorn.run(app)
