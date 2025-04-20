from fastapi import FastAPI
from enum import Enum
from typing import Optional

#SQL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey, Text, TIMESTAMP, func

# 資料型態驗證
from pydantic import BaseModel

# 連接資料庫
DATABASE_URL = "postgresql://user:adminrd@localhost:5432/OwnLibrary"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Models
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String, nullable=False)
    author = Column(String)
    isbn = Column(String, unique=True)
    category = Column(String)
    price = Column(Numeric(10, 2))
    created_at = Column(TIMESTAMP, server_default=func.now())

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())



# 定義預設值
# class BlogType(str, Enum):
#     business = "business"
#     story = "story"
#     qa = "qa"
# Schemas

class BookBase(BaseModel):
    title: str
    author: Optional[str] = None #選填，字串，預設 None
    isbn: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    user_id: int

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int
    created_at: Optional[str]

    class Config:
        orm_mode = True


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

@app.get("/blog/all")
def get_blog(page=0, size=0):
    if int(page) > 10:
        return {"error": "超出頁數"}
    return {"message": f"所有的 blogs： 來自第 {page} 頁， 總共有 {size} 筆資料"}

# 驗證參數的型別
@app.get("/blog/alltype")
def get_blog(page=0, size: Optional[int] = None):
    return {"message": f"所有的 blogs： 來自第 {page} 頁， 總共有 {size} 筆資料"}



@app.get("/blog/{id}")
def get_blog(id: int):
    return {"data":f"Blog id is: {id}"}

#設定只能輸入 blogType 的值
@app.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"message":f"Blog 的資料型態是 {type}"}