from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from models import UserInSystem, UserInCompany
from db import fakeDB
from datetime import datetime, timedelta
from dependencies.security_dep import (
    fake_hash_password,
    get_current_user,
    get_current_active_user,
    authenticate_user,
    create_access_token,
)
from config.security_conf import TokenConfig


db_user = fakeDB.fake_user_db
router = APIRouter(prefix="/token", tags=["token"])


@router.get("/users/me")
async def read_user_me(
    current_user: Annotated[UserInCompany, Depends(get_current_active_user)]
):
    return current_user


@router.post("/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
    # OLDER VERSION
    user_dict = db_user.get(form_data.username)  # retrieved from database
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = UserInSystem(**user_dict)  # validation and pass the key as the schema

    # hashed the input pwd
    hashed_password = fake_hash_password(form_data.password)
    # pwd validation
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, details="Incorrect username or password")
    """
    # NOTE: Validation occured here where hashed_pwd from database is compare
    # with input password from user that will be hashed
    # hashed(user_pwd) == hashed_pwd_db
    user = authenticate_user(
        fake_db=db_user, username=form_data.username, password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # NOTE: Token expires time for authenticated user
    access_token_expires = timedelta(minutes=TokenConfig.ACCESS_TOKEN_EXPIRE_MINUTE)

    # note: the sub, access_token, token_type is constant (cannot customize name)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
