#SQL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 連接資料庫
DATABASE_URL = "sqlite:///./OwnLibrary.db"
engine = create_engine(DATABASE_URL, echo=True) 
Base = declarative_base()

# Create a session to interact with the database
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()