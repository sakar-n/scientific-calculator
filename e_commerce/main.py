from typing import List, Optional
from starlette.routing import Host
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Path, Query, dependencies
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, oauth2
from apps import crud, models, schemas
from apps.database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from authentication import *

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
async def generate_token(request_form: OAuth2PasswordRequestForm = Depends()):
    token = await token_generator(request_form.username, request_form.password)
    return {"acess_token": token, "token_type": "bearer"}


@app.get("/")
async def get_current_user(token: str = Depends(oauth2_schema)):
    return {"token": "user_token"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register/", response_model=schemas.User)
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.register(db, user)


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="127.0.0.1", reload=True)
