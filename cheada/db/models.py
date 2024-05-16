from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship

from .database import Base


# subject, publish_year, textbook_name, page_num, problem_num, image_file_extension

class MathProblemType(Base):
    __tablename__ = "math_problem_type"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    chapter = Column(String, nullable=False)
    sub_concept = Column(String, nullable=False)

    math_problems = relationship("MathProblem", back_populates="math_problem_types")


class MathProblem(Base):
    __tablename__ = "math_problem"

    id = Column(Integer, primary_key=True, nullable=False)
    typeId = Column(Integer, ForeignKey("math_problem_type.id"))
    textbookName = Column(String)
    problemNumber = Column(String, nullable=False)
    pageNum = Column(Integer, nullable=False)
    solveStudentNum = Column(Integer)
    incorrectStudentNum = Column(Integer)
    easyNum = Column(Integer)
    middleNum = Column(Integer)
    difficultNum = Column(Integer)
    
    math_problem_types = relationship("MathProblemType", back_populates="math_problems")

# association_table = Table(
#     "association",
#     Base.metadata,
#     Column("problem_id", ForeignKey("math_problem.id"), primary_key=True),
#     Column("math_problem_type_id", ForeignKey("math_problem_type.id"), primary_key=True)
#     )