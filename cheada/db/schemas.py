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
        from_attributes=True


# MathProblem
class MathProblemBase(BaseModel):
    textbook_id: int
    problem_number: str
    page_number: int
    solved_students_count: int
    incorrect_students_count: int
    easy_num: int
    medium_difficulty_perceived_count: int
    high_difficulty_perceived_count: int


class MathProblemCreate(MathProblemBase):
    type_id: int


class MathProblem(MathProblemBase):
    id: int
    
    class Config:
        orm_mode = True
        from_attributes=True