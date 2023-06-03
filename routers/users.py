from fastapi import APIRouter, Query, Body, status
from models import UserName, UserDetails
from db import fakeDB
from typing import Union, Dict
from typing_extensions import Annotated

db = fakeDB.fake_db
router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_name}", status_code=status.HTTP_200_OK)
def get_type_user(user_name: UserName) -> Dict[str, str]:
    """
    Endpoint return the type of user
    based on their name\n

    Args:\n
    * user_name: Username that you want to see their type user

    """

    if user_name is user_name.user:
        return {f"{user_name.user}": "Normal user"}
    elif user_name is user_name.superUser:
        return {f"{user_name.superUser}": "Super user"}
    elif user_name is user_name.mainUser:
        return {f"{user_name.mainUser}": "Main user"}


@router.get("/{user_name}/details", status_code=status.HTTP_200_OK)
def get_user_details(user_name: UserName):
    """
    Endpoint only return Main User information only.\n

    Args:\n
    * user_name: sara (default)

    """
    if user_name is user_name.mainUser:
        return {"status": 200, "mainUser information": db["sara"]}
    else:
        return {"status": 400, "message": "Cannot see other information than main user"}


@router.post("/{user_name}", status_code=status.HTTP_201_CREATED)
def add_new_user(
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
) -> Dict[str, Dict[str, str]]:
    """
    Endpoint used to add new user.\n
    Args:\n
    * new_user: New username
    * new_info: New information for the new user
    """

    db[new_user] = new_info.dict()
    return db


@router.put("/{user_name}", status_code=status.HTTP_201_CREATED)
def update_user(user_name: str, update_info: UserDetails) -> Dict[str, Dict[str, str]]:
    """
    Endpoint used to update the information that has been posted. \n
    Args:
    * user_name: User that you want to update
    * update_info: User information (request body)
    """

    db.update({user_name: update_info.dict()})
    return db


@router.delete("/{user_name}", status_code=status.HTTP_200_OK)
def delete_user(user_name: str) -> Dict[str, Dict[str, str]]:
    """
    Endpoint used to delete user name.
    Args:
        * username: name of the user you want to delete

    """
    del db[user_name]
    return db


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_user() -> Dict[str, Dict[str, str]]:
    """
    Endpoint executed to return all user information.
    """
    return db
