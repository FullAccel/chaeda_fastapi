from fastapi import HTTPException
from requests import Session

from cheada_fastapi.cheada.domain.textBook_preprocessing.dto.ProblemInfoDto import ProblemInfoDto
from cheada_fastapi.cheada.db import schemas
from cheada_fastapi.cheada.db.models import Users

def create_user(session: Session, user: schemas.UserBase) -> Users:
    db_user = Users(
        nickname=user.nickname,
        gender=user.gender,
        age=user.age,
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user

