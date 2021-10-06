from apps.schemas import UserCreate
from sqlalchemy.orm import Session
from apps import models


def register(db: Session, login: UserCreate):
    db_user = models.Login(
        full_name=login.full_name,
        email=login.email,
        username=login.username,
        password=login.password,
        is_active=login.is_active,
        is_superuser=login.is_superuser,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
