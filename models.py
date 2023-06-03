from pydantic import BaseModel, Field
from typing_extensions import Annotated
from fastapi import Query
from enum import Enum


class UserName(str, Enum):
    user:str= "ammar"
    mainUser:str="sara"
    superUser:str="joe"

class UserDetails(BaseModel):
    fullname: Annotated[str, Query(max_length=10)]
    age: Annotated[int, Query(ge=18)]
    job: Annotated[str, Query(max_length=20)]

    class Config:
        schema_extra = {
                "fullname":"Leya", 
                "age":21, 
                "job":"tko"
        }
    
