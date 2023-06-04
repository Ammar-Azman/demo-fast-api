from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from models import UserInSystem, UserInCompany
from db import fakeDB
from dependencies.security_dep import (
    fake_hash_password,
    get_current_user,
    get_current_active_user,
)


db_user = fakeDB.fake_user_db
router = APIRouter(prefix="/token", tags=["token"])


@router.get("/users/me")
async def read_user_me(
    current_user: Annotated[UserInCompany, Depends(get_current_active_user)]
):
    return current_user


@router.post("/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = db_user.get(form_data.username)  # retrieved from database
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = UserInSystem(**user_dict)  # validation and pass the key as the schema

    # hashed the input pwd
    hashed_password = fake_hash_password(form_data.password)
    # pwd validation
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, details="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}
