from fastapi import Depends, FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


class Data(BaseModel):
    fileName: str


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()


@router.post("/problems/", response_model=schemas.MathProblem)
def create_problem(problem: schemas.MathProblemCreate, db: Session = Depends(get_db)):
    db_problem = crud.get_problem(db, problem_id=1)
    if db_problem:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, problem=problem)

@router.get("/problems/{problem_id}", response_model=schemas.MathProblem)
def read_problem(problem_id: int, db: Session = Depends(get_db)):
    db_problem = crud.get_problem(db, user_id=problem_id)
    if db_problem is None:
        raise HTTPException(status_code=404, detail="Problem not found")
    return db_problem