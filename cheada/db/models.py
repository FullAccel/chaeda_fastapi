from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .database import Base


# subject, publish_year, textbook_name, page_num, problem_num, image_file_extension

class Type(Base):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    chapter = Column(String, nullable=False)
    subconcept = Column(String, nullable=False)

    problems = relationship("MathProblem", back_populates="type")


class MathProblem(Base):
    __tablename__ = "math_problem"

    id = Column(Integer, primary_key=True, nullable=False)
    typeId = Column(Integer, ForeignKey("type.id"))
    textbookName = Column(String)
    problemNumber = Column(Integer, nullable=False)
    pageNum = Column(Integer, nullable=False)
    solveStudentNum = Column(Integer, nullable=False)
    incorrectStudentNum = Column(Integer, nullable=False)
    easyNum = Column(Integer, nullable=False)
    middleNum = Column(Integer, nullable=False)
    difficultNum = Column(Integer, nullable=False)
    
    types = relationship("Type", back_populates="problems")