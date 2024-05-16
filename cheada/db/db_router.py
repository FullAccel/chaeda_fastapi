from fastapi import Depends, FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


class Data(BaseModel):
    fileName: str


router = APIRouter()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/problem/", response_model=schemas.MathProblem)
def create_problem(problem: schemas.MathProblemCreate, db: Session = Depends(get_db)):
    db_problem = crud.get_problem_by_name_problem_number(db, name=problem.textbookName, problem_number=problem.problemNumber)
    if db_problem:
        raise HTTPException(status_code=400, detail="Problem Already Exist")
    return crud.create_problem(db=db, problem=problem)

@router.get("/problem/{problem_id}", response_model=schemas.MathProblem)
def read_problem(problem_id: int, db: Session = Depends(get_db)):
    db_problem = crud.get_problem_by_id(db, problem_id=problem_id)
    if db_problem is None:
        raise HTTPException(status_code=404, detail="Problem not found")
    return db_problem

@router.get("/problems/", response_model=list[schemas.MathProblem])
def read_math_problems(db: Session = Depends(get_db)):
    math_problems = crud.get_problems(db)
    return math_problems

@router.post("/type/", response_model=schemas.MathProblemType)
def create_type(type: schemas.MathProblemTypeCreate, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_sub_concept(db, sub_concept=type.sub_concept)
    if db_type:
        raise HTTPException(status_code=400, detail="Subject already registered")
    return crud.create_type(db=db, type=type)

@router.get("/math_problem_type/{subject}", response_model=schemas.MathProblemType)
def read_type(subject: str, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_subject(db, subject=subject)
    if db_type is None:
        raise HTTPException(status_code=404, detail="Type not found")
    return db_type

@router.get("/math_problem_type/{sub_concept}", response_model=schemas.MathProblemType)
def read_type(sub_concept: str, db: Session = Depends(get_db)):
    db_type = crud.get_type_by_sub_concept(db, sub_concept=sub_concept)
    if db_type is None:
        raise HTTPException(status_code=404, detail="Type not found")
    return db_type

@router.get("/math_problem_types/", response_model=list[schemas.MathProblemType])
def read_types(db: Session = Depends(get_db)):
    types = crud.get_types(db)
    return types