from models import BaseInfo
from typing import Annotated, Union
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from models import UserInCompany, UserInSystem, Token, TokenData
from db import fakeDB
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from config.security_conf import TokenConfig


outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# NOTE: "token" is used as it become the url path operation, the endpoint must use "token" to setup the OAuth2
# if the tokenUrl="yahoo", hence the endpoint that reponsible for Authorization must use "/yahoo" too
db_user = fakeDB.fake_user_db
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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
    """
    # Simple version (fakehashed)
    user = fake_decode_token(token)
    print("user", user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credential",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
    """
    # JWT Token version
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, TokenConfig.SECRET_KEY, algorithms=[TokenConfig.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user = get_user(db=db_user, username=token_data.username)
    if user is None:
        raise credential_exception
    return user


async def get_current_active_user(
    current_user: Annotated[UserInCompany, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive User")
    return current_user


##################################################
########## JWT token authentication ##############
##################################################


def verify_password(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd, hashed_pwd)


def get_password_hash(pwd):
    return pwd_context.hash(pwd)


def authenticate_user(fake_db: dict, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    """
    Return encoded jtw_token based on
    the secret_key

    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, TokenConfig.SECRET_KEY, algorithm=TokenConfig.ALGORITHM
    )
    return encoded_jwt
