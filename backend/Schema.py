# 資料型態驗證
from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None #選填，字串，預設 None
    isbn: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None