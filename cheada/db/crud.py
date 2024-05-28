from sqlalchemy.orm import Session

# from cheada_fastapi.cheada.domain.textBook_preprocessing.dto.ProblemInfoDto import ProblemInfoDto
from . import models, schemas

def get_problem_by_id(db: Session, problem_id: int):
	return db.query(models.MathProblem).filter(models.MathProblem.id == problem_id).first()

def get_problem_by_id_problem_number(db: Session, id: int, problem_number: str):
	# print("jfdslfdjs", id, problem_number)
	return db.query(models.MathProblem).filter(models.MathProblem.textbook_id == id, models.MathProblem.problem_number == problem_number).first()

def get_problems(db: Session, skip: int = 0, limit: int = 100):
	return db.query(models.MathProblem).offset(skip).limit(limit).all()

def create_problem(db: Session, problem: schemas.MathProblemCreate):
	print("type_id:", problem.type_id)
	db_problem = models.MathProblem(
		textbook_id=problem.textbook_id,
		problem_number=problem.problem_number,
		page_number=problem.page_number,
		solved_students_count=problem.solved_students_count,
		incorrect_students_count=problem.incorrect_students_count,
		easy_num=problem.easy_num,
		medium_difficulty_perceived_count=problem.medium_difficulty_perceived_count,
		high_difficulty_perceived_count=problem.high_difficulty_perceived_count
	)
	db.add(db_problem)
	db.commit()
	db.refresh(db_problem)


	if problem.type_id:
		db.execute(
                models.association_table.insert().values(
                    math_problem_id=db_problem.id,
                    math_problem_type_id=problem.type_id
                )
            )

	db.commit()
	return db_problem

def get_types(db: Session, skip: int = 0, limit: int = 100):
	return db.query(models.MathProblemType).offset(skip).limit(limit).all()

def get_type_by_subject(db: Session, subject: str):
	return db.query(models.MathProblemType).filter(models.MathProblemType.subject == subject).first()

def get_type_by_chapter(db: Session, chapter: str):
    return db.query(models.MathProblemType).filter(models.MathProblemType.chapter == chapter).first()

def get_type_by_sub_concept(db: Session, sub_concept: str):
	return db.query(models.MathProblemType).filter(models.MathProblemType.sub_concept == sub_concept).first()

def create_type(db: Session, type: schemas.MathProblemTypeCreate):
	# db_type = models.MathProblemType(
	#     subject=type.subject,
	#     chapter=type.chapter,
	#     sub_concept=type.sub_concept
	# )
	db_type = models.MathProblemType(**type.model_dump())
	db.add(db_type)
	db.commit()
	db.refresh(db_type)
	return db_type

def get_textbook_by_name(db: Session, textbook_name: str):
    return db.query(models.Textbook).filter(models.Textbook.name == textbook_name).first()