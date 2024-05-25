from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship

from .database import Base


# subject, publish_year, textbook_name, page_num, problem_num, image_file_extension

association_table = Table(
    "problem_type_mapping",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("math_problem_id", Integer, ForeignKey("math_problem.id")),
    Column("math_problem_type_id", Integer, ForeignKey("math_problem_type.id"))
)


class MathProblemType(Base):
    __tablename__ = "math_problem_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String, nullable=False, index=True)
    chapter = Column(String, nullable=False, index=True)
    sub_concept = Column(String, nullable=False, index=True)

    math_problems = relationship("MathProblem", secondary=association_table, back_populates="math_problem_types")


class MathProblem(Base):
    __tablename__ = "math_problem"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    textbook_id = Column(Integer, ForeignKey("textbook.id"), nullable=False)
    problem_number = Column(String, nullable=False)
    page_number = Column(Integer, nullable=False)
    solved_students_count = Column(Integer)
    incorrect_students_count = Column(Integer)
    easy_num = Column(Integer)
    medium_difficulty_perceived_count = Column(Integer)
    high_difficulty_perceived_count = Column(Integer)
    
    math_problem_types = relationship("MathProblemType", secondary=association_table, back_populates="math_problems")

class Textbook(Base):
    __tablename__ = "textbook"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    last_page_num = Column(Integer, nullable=False)
    publish_year = Column(Integer, nullable=False)
    start_page_num = Column(Integer, nullable=False)
    created_date = Column(String)
    modified_date = Column(String)
    upload_member_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    publisher = Column(String)
    subject = Column(String, nullable=False)
    target_grade = Column(String)
    textbook_src_url = Column(String)
    textbook_thumbnail = Column(String)
    
    