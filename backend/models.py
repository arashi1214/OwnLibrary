from sqlalchemy import TIMESTAMP, Column, Numeric, String, Boolean, Integer, ForeignKey, func
from database import Base

# 資料型態驗證
from pydantic import BaseModel
from typing import Optional

# Models
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String, nullable=False)
    author = Column(String)
    isbn = Column(String)
    category = Column(String)
    price = Column(Numeric(10, 2))
    created_at = Column(TIMESTAMP, server_default=func.now())

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())


