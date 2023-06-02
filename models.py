from pydantic import BaseModel
from typing_extensions import Annotated
from fastapi import Query
from enum import Enum


class UserType(str, Enum):
    user:str= "ammar"
    mainUser:str="sara"
    superUser:str="joe"

class UserDetails(BaseModel):
    fullname: Annotated[str, Query(max_length=100)]
    age: Annotated[int, Query(ge=18)]
    job: Annotated[str, Query(max_length=20)]
    
