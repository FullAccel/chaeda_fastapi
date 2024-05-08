# from pydantic import BaseModel


# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     items: list[Item] = []

#     class Config:
#         orm_mode = True

from pydantic import BaseModel


class TypeBase(BaseModel):
    subject: str
    chapter: str
    subconcept: str
    

class TypeCreate(TypeBase):
    pass


class Type(TypeBase):
    id: int

    class Config:
        orm_mode = True


class MathProblemBase(BaseModel):
    textbookName: str
    problemNumber: int
    pageNum: int
    solveStudentNum: int
    incorrectStudentNum: int
    easyNum: int
    middleNum: int
    difficultNum: int


class MathProblemCreate(MathProblemBase):
    typeId: int


class MathProblem(MathProblemBase):
    id: int

    class Config:
        orm_mode = True