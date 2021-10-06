from pydantic import BaseModel


class User(BaseModel):
    username: str
    full_name: str
    email: str
    is_active: str
    is_superuser: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    full_name: str
    email: str
    username: str
    password: str
    is_active: str
    is_superuser: str
