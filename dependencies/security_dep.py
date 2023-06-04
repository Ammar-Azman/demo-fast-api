from models import BaseInfo
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from models import UserInCompany, UserInSystem
from db import fakeDB


outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")
db_user = fakeDB.fake_user_db


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInSystem(**user_dict)


def fake_decode_token(token):
    user = get_user(db_user, token)
    return user


def fake_hash_password(pwd: str):
    return "fakehashed" + pwd


async def get_current_user(token: Annotated[str, Depends(outh2_scheme)]):
    user = fake_decode_token(token)
    print("user", user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credential",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
    current_user: Annotated[UserInCompany, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive User")
    return current_user
