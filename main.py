from fastapi import FastAPI, Query, Body
from models import UserType, UserDetails
from db import fakeDB
from typing_extensions import Annotated
from typing import Union

app = FastAPI()
db = fakeDB.fake_db

@app.get("/")
def root():
    return {
        "Health test":"Good!"
    }

@app.get("/user/{userType}")
def get_user(userType:UserType):
    if userType is userType.user:
        return {"normal_user":userType.user}
    elif userType is userType.superUser:
        return {"super_user":userType.superUser}
    elif userType is userType.mainUser:
        return {"main_user":userType.mainUser}
    
@app.post("/user")
def post_user_details(userType:Union[UserType, str]):
    if userType is userType.mainUser:
        return {"status":200, 
                "mainUser information":db["col1"]}
    else:
        return {"status":400, 
                "message":"Cannot see other information than main user"}
    
@app.post("/user/{col}")
def add_new_user(new_user:str,
                new_info:Annotated[UserDetails, 
                                    Body(examples={   
                                        "test":{
                                            "summary":"example 1", 
                                            "description":"exaample Madey", 
                                            "value":{
                                            "fullname":"Madey", 
                                            "age": 99, 
                                            "job": "gg"
                                            }
                                        }, 
                                        "test 2":{
                                            "summary":"example 2", 
                                            "description":"example Paklah", 
                                            "value":{
                                            "fullname":"Pak Lah", 
                                            "age": 45, 
                                            "job": "haha"
                                            }
                                        }
                                    })]):
    
    db[new_user]= new_info.dict()
    return db

@app.put("/user/{col}")
def update_user(user_name:str, 
            update_info:UserDetails):

    db.update({
        user_name: update_info.dict()
    })
    return db

@app.delete("/user")
def delete_user(username:str):
    del db[username]
    return db


@app.get("/user")
async def get_all_user():
    return db