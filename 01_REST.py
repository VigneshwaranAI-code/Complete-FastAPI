# from fastapi import FastAPI ,HTTPException
# from pydantic import BaseModel , Field
# from uuid import UUID


# app =FastAPI() 

# class Book(BaseModel):
#     id : UUID
#     title : str = Field(min_length=1)
#     author : str = Field(min_length=1, max_length=100)
#     description : str = Field(min_length=1 ,max_length=50)
#     rating: int= Field(gt=-1 , lt=101)

# BOOKS = []



# @app.get("/")  #view the data
# def about():
#     return BOOKS

# @app.post("/")  #create new data 
# def create_book(book : Book):
#     BOOKS.append(book)
#     return book

# @app.put("/{book_id}")  #update the data
# def Update_book(book_id : UUID , book:Book):
#     count = 0
#     for x in BOOKS:
#         count += 1
#         if x.id == book_id:
#             BOOKS[count -1 ] = book
#             return BOOKS[count -1]
#     raise HTTPException(
#             status_code=404,
#             detail=f"ID {book_id} : does not exist"
#         )

# @app.delete("/{book_id}")  #detel the data 
# def delete_book(book_id : UUID):
#     for i, x in enumerate(BOOKS):
#         if x.id == book_id:
#             del BOOKS[i]
#             return {"message": f"ID {book_id} deleted"}
#     raise HTTPException(
#         status_code=404,
#         detail=f"ID {book_id}: Does not exist"
#     )


from fastapi import FastAPI ,status , HTTPException
from pydantic import BaseModel , Field
from uuid import UUID , uuid4
from typing import List


app =FastAPI(title="Book store API", version="0.0.1")


class Bookbase(BaseModel):
    title : str = Field(min_length=1 , max_length=100)
    author : str = Field(min_length=1 , max_length=100)
    Description : str = Field(min_length=1 , max_length=100)
    rating : int = Field(gt=0 , le=101)




class BookCreate(Bookbase):
    pass

class Book(Bookbase): 
    id : UUID




BOOKs : List[Book] = []


@app.get("/",response_model=list[Book])
def get_book():
    return BOOKs

@app.post("/create_book",response_model=Book ,status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    """create a new book"""
    new_book = Book(id=uuid4(), **book.dict())
    BOOKs.append(new_book)
    return new_book 

@app.put("/{id}",response_model=Book)
def Update_data(id: UUID , book:BookCreate):
    """"update an existing Book"""
    for index , existign_book in enumerate(BOOKs):
        if existign_book.id == id:
            Updated_data = Book(id = id , **book.dict())
            BOOKs[index]= Updated_data
            return Updated_data
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with Id {id} is not book in the book databse"
    )

@app.delete("/{id}")
def delete_book(id :UUID):

    for index , book in enumerate(BOOKs):
        if book.id == id:
            BOOKs.pop(index)
            return "deleted sucessfullly"
    raise HTTPException(
        status_code=status.HTTP__404_NOT_FOUND,
        detail=f'BOok with ID {id} not found'
    )







