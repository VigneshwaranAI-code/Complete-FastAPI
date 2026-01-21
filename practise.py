from fastapi import FastAPI , status , HTTPException
from pydantic import BaseModel , Field
from uuid import UUID , uuid4
from typing import List


#initize the app 
app = FastAPI(title="Books", version=0.03)

