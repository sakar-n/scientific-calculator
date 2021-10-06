from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_USER: str = "postgres"
POSTGRES_PASSWORD = "password"
POSTGRES_SERVER: str = "localhost"
POSTGRES_PORT: str = 5432  # default postgres port is 5432
POSTGRES_DB: str = "user_db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
