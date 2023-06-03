from pydantic import BaseModel
from typing import Union, Annotated
from fastapi import Query
from enum import Enum


class UserName(str, Enum):
    user: str = "ammar"
    mainUser: str = "sara"
    superUser: str = "joe"


class UserDetails(BaseModel):
    fullname: Annotated[str, Query(max_length=10)]
    age: Annotated[int, Query(ge=18)]
    job: Annotated[str, Query(max_length=20)]

    class Config:
        schema_extra = {"fullname": "Leya", "age": 21, "job": "tko"}


class UserInput(BaseModel):
    username: Annotated[str, Query(min_length=5, max_length=10)] = "Bryan"
    password: Annotated[str, Query(min_length=5, max_length=10)] = "pasw!023"
    fullname: Union[str, None] = None


class UserOutput(BaseModel):
    """
    No output returned
    """

    username: Annotated[str, Query(min_length=5, max_length=10)]
    fullname: Union[str, None] = None
