from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, SessionLocal
import models
import Schema

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# 建立 models 內的資料表
models.Base.metadata.create_all(bind=engine)

# 建立那些 url 可以呼叫到此 API
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello, this in index page"}

articles = []

# 列出全部的清單
@app.get("/books")
def find_book(db: Session = Depends(get_db)):
    result = db.query(models.Book).all()
    print(result)
    return {"message": result}

@app.get("/get_book_detail/{book_title}")
def get_books(book_title:str, db: Session = Depends(get_db)):
    result = db.query(models.Book).filter(models.Book.title == book_title)

    if not result:
        raise HTTPException(status_code=404, detail='This id\'s question is not found...')

    return result

# 新增書籍
@app.post("/create_book")
def create_book(book: Schema.BookCreate, db: Session = Depends(get_db)):
    new_book = models.Book(**book.dict())
    new_book.user_id = 1

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

'''

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
'''