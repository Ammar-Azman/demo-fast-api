from fastapi import APIRouter, Query, Body
from models import UserType, UserDetails
from db import fakeDB
from typing import Union
from typing_extensions import Annotated

db = fakeDB.fake_db
router = APIRouter(
        prefix="/users", 
        tags=["users"]
)


@router.get("/{userType}")
def get_user(userType:UserType):
    if userType is userType.user:
        return {"normal_user":userType.user}
    elif userType is userType.superUser:
        return {"super_user":userType.superUser}
    elif userType is userType.mainUser:
        return {"main_user":userType.mainUser}
    
@router.post("/")
def post_user_details(userType:Union[UserType, str]):
    if userType is userType.mainUser:
        return {"status":200, 
                "mainUser information":db["col1"]}
    else:
        return {"status":400, 
                "message":"Cannot see other information than main user"}
    
@router.post("/{col}")
def add_new_user(new_user:str,
                new_info:Annotated[UserDetails, 
                                    Body(examples={   
                                        "test":{
                                            "summary":"example 1", 
                                            "description":"Simple Example 1", 
                                            "value":{
                                            "fullname":"Jackie", 
                                            "age": 99, 
                                            "job": "gg"
                                            }
                                        }, 
                                        "test 2":{
                                            "summary":"example 2", 
                                            "description":"Simple Example 2", 
                                            "value":{
                                            "fullname":"Karen", 
                                            "age": 45, 
                                            "job": "haha"
                                            }
                                        }
                                    })]):
    
    db[new_user]= new_info.dict()
    return db

@router.put("/{col}")
def update_user(user_name:str, 
            update_info:UserDetails):

    db.update({
        user_name: update_info.dict()
    })
    return db

@router.delete("/")
def delete_user(username:str):
    del db[username]
    return db


@router.get("/")
async def get_all_user():
    return db