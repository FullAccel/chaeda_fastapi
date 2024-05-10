# from sqlalchemy.orm import Session

# from . import models, schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

from sqlalchemy.orm import Session

# from cheada_fastapi.cheada.domain.textBook_preprocessing.dto.ProblemInfoDto import ProblemInfoDto
from . import models, schemas

def get_problem_by_id(db: Session, problem_id: int):
	return db.query(models.MathProblem).filter(models.MathProblem.id == problem_id).first()

def get_problem_by_name_problem_number(db: Session, name: str, problem_number: str):
	return db.query(models.MathProblem).filter(models.MathProblem.textbookName == name and models.MathProblem.problemNumber == problem_number).first()

def get_problems(db: Session, skip: int = 0, limit: int = 100):
	return db.query(models.MathProblem).offset(skip).limit(limit).all()

def create_problem(db: Session, problem: schemas.MathProblemCreate):
	db_problem = models.MathProblem(
		typeId=problem.typeId,
		textbookName=problem.textbookName,
		problemNumber=problem.problemNumber,
		pageNum=problem.pageNum,
		solveStudentNum=problem.solveStudentNum,
		incorrectStudentNum=problem.incorrectStudentNum,
		easyNum=problem.easyNum,
		middleNum=problem.middleNum,
		difficultnum=problem.difficultNum
	)
	db.add(db_problem)
	db.commit()
	db.refresh(db_problem)
	return db_problem


def get_types(db: Session, skip: int = 0, limit: int = 100):
	return db.query(models.MathProblemType).offset(skip).limit(limit).all()

def get_type_by_subject(db: Session, subject: str):
	return db.query(models.MathProblemType).filter(models.MathProblemType.subject == subject).first()

def create_type(db: Session, type: schemas.MathProblemTypeCreate):
	# db_type = models.Type(
	#     subject=type.subject,
	#     chapter=type.chapter,
	#     subconcept=type.subconcept
	# )
	db_type = models.MathProblemType(**type.model_dump())
	db.add(db_type)
	db.commit()
	db.refresh(db_type)
	return db_type