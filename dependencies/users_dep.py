from models import UserName, UserDetails
from db import fakeDB
from typing import Annotated
from fastapi import Body

db = fakeDB.fake_db


async def choose_user(user_name: UserName):
    if user_name is user_name.user:
        return {f"{user_name.user}": "Normal user"}
    elif user_name is user_name.superUser:
        return {f"{user_name.superUser}": "Super user"}
    elif user_name is user_name.mainUser:
        return {f"{user_name.mainUser}": "Main user"}


async def sara_only(user_name: UserName):
    if user_name is user_name.mainUser:
        return {"status": 200, "mainUser information": db["sara"]}
    else:
        return {"status": 400, "message": "Cannot see other information than main user"}


async def update_user(user_name: str, update_info: UserDetails):
    db.update({user_name: update_info.dict()})

    return db


async def add_user(
    new_user: str,
    new_info: Annotated[
        UserDetails,
        Body(
            examples={
                "test": {
                    "summary": "example 1",
                    "description": "Simple Example 1",
                    "value": {"fullname": "Jackie", "age": 99, "job": "gg"},
                },
                "test 2": {
                    "summary": "example 2",
                    "description": "Simple Example 2",
                    "value": {"fullname": "Karen", "age": 45, "job": "haha"},
                },
            }
        ),
    ],
):
    db[new_user] = new_info.dict()
    return db


async def delete_user(user_name):
    del db[user_name]
    return db


async def get_all_user_():
    return db
