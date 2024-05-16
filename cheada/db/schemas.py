from pydantic import BaseModel

# MathProblemType
class MathProblemTypeBase(BaseModel):
    subject: str
    chapter: str
    sub_concept: str
    

class MathProblemTypeCreate(MathProblemTypeBase):
    pass


class MathProblemType(MathProblemTypeBase):
    id: int

    class Config:
        orm_mode = True


# MathProblem
class MathProblemBase(BaseModel):
    typeId: int
    textbookName: str
    problemNumber: str
    pageNum: int
    solveStudentNum: int
    incorrectStudentNum: int
    easyNum: int
    middleNum: int
    difficultNum: int


class MathProblemCreate(MathProblemBase):
    pass


class MathProblem(MathProblemBase):
    id: int
    
    class Config:
        orm_mode = True