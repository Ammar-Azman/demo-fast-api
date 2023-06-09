from pydantic import BaseModel
from typing import Union, Annotated
from fastapi import Query, Form
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


class UserInCompany(BaseModel):
    username: str
    age: int
    job: str
    disabled: Union[bool, None] = None


class UserInSystem(UserInCompany):
    hashed_password: str


##### FILTERING METHOD 1 ###
class UserInput(BaseModel):
    username: Annotated[str, Query(min_length=5, max_length=10)] = "Bryan"
    password: Annotated[str, Query(min_length=5, max_length=10)] = "dasd!982"
    fullname: Union[str, None] = None


class UserOutput(BaseModel):
    """
    No output returned
    """

    username: Annotated[str, Query(min_length=5, max_length=10)]
    fullname: Union[str, None] = None


#### FILTERING METHOD 2 ####


class BaseInfo(BaseModel):
    username: Annotated[str, Form()]


class CredentialInfo(BaseInfo):
    password: str


##### JWT TOKEN AUTHENTICATION SCHEMA #####


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
