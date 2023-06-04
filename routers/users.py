from fastapi import APIRouter, Body, status, Depends
from models import UserName, UserDetails
from db import fakeDB
from typing import Dict
from typing_extensions import Annotated
from dependencies.users_dep import (
    choose_user,
    sara_only,
    update_user,
    add_user,
    delete_user,
    get_all_user_,
)

db = fakeDB.fake_db
router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{data}", status_code=status.HTTP_200_OK)
def get_type_user(data: Annotated[UserName, Depends(choose_user)]) -> Dict[str, str]:
    """
    Endpoint return the type of user
    based on their name\n

    Args:\n
    * user_name: Username that you want to see their type user

    """
    return data


@router.get("/{data}/details", status_code=status.HTTP_200_OK)
def get_user_details(data: Annotated[dict, Depends(sara_only)]):
    """
    Endpoint only return Main User information only.\n

    Args:\n
    * user_name: sara (default)

    """
    return data


@router.post("/{data}", status_code=status.HTTP_201_CREATED)
def add_new_user(
    data: Annotated[UserName, Depends(add_user)]
) -> Dict[str, Dict[str, str]]:
    """
    Endpoint used to add new user.\n
    Args:\n
    * new_user: New username
    * new_info: New information for the new user
    """
    return data


@router.put("/{data}", status_code=status.HTTP_201_CREATED)
def update_user(
    data: Annotated[dict, Depends(update_user)]
) -> Dict[str, Dict[str, str]]:
    """
    Endpoint used to update the information that has been posted. \n
    Args:
    * user_name: User that you want to update
    * update_info: User information (request body)
    """
    return data


@router.delete("/{data}", status_code=status.HTTP_200_OK)
def delete_user(
    data: Annotated[dict, Depends(delete_user)]
) -> Dict[str, Dict[str, str]]:
    """
    Endpoint used to delete user name.
    Args:
        * username: name of the user you want to delete

    """
    return data


@router.get("/get_all/{data}", status_code=status.HTTP_200_OK)
async def get_all_user(data: Annotated[dict, Depends(get_all_user_)]):
    """
    -> Dict[str, Dict[str, str]]
    Endpoint executed to return all user information.
    """
    return data
