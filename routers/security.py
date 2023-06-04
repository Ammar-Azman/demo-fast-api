from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from models import BaseInfo, UserInSystem
from db import fakeDB


db = fakeDB.fake_user_db
router = APIRouter(prefix="/token", tags=["token"])

outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/credential")
async def get_credential(token: Annotated[str, Depends(outh2_scheme)]):
    return {"token": token}


def fake_decode_token(token):
    return BaseInfo(username=token + "fakedecoded")


async def get_current_user(token: Annotated[str, Depends(outh2_scheme)]):
    user = fake_decode_token(token)
    return user


@router.get("/current/user")
async def read_user_me(current_user: Annotated[BaseInfo, Depends(get_current_user)]):
    return current_user


@router.post("/token")
async def login_form(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = db.get(form_data.username)  # retrieved from database
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = UserInSystem(**user_dict)  # validation
