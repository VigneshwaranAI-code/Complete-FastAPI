from fastapi import FastAPI , status , HTTPException , Depends
from uuid import UUID , uuid4
from pydantic import BaseModel , Field
from typing import List 
from deps import get_db
from Models import Books 
from sqlalchemy.orm import Session
from Database import engine , Base
import Models

Models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Book store API", version="0.0.1")

class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, le=101)


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True


class BookCreate(BookBase):
    pass



@app.get("/books", response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    return db.query(Books).all()


@app.post("/books", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Books(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@app.put("/update/{id}", response_model=Book)
def update_book(id, book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(Books).filter(Books.id == id).first()

    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {id} not found"
        )
    
    for key, value in book.dict().items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/delete/{id}")
def delete(id , db : Session = Depends(get_db)):
    db_book = db.query(Books).filter(Books.id == id).first()

    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {id} not found"
        )
    
    db.delete(db_book)
    db.refresh(db_book)
    db.commit()
    return {"message":"Successfully"}







