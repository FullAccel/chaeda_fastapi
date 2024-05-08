# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

# from .database import Base


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")

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

    math_problems = relationship("MathProblem", back_populates="type")


class MathProblem(Base):
    __tablename__ = "math_problem"

    id = Column(Integer, primary_key=True, nullable=False)
    typeId = Column(Integer, ForeignKey("type.id"))
    textbookName = Column(String)
    problemNumber = Column(Integer, nullable=False)
    pageNum = Column(Integer, nullable=False)
    solveStudentNum = Column(Integer)
    incorrectStudentNum = Column(Integer)
    easyNum = Column(Integer)
    middleNum = Column(Integer)
    difficultNum = Column(Integer)
    
    type = relationship("Type", back_populates="math_problems")