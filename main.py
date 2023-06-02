from fastapi import FastAPI
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

@app.get("/user/{info}")
def get_user(userType:UserType):
    if userType is userType.user:
        return {"normal_user":userType.user}
    elif userType is userType.superUser:
        return {"super_user":userType.superUser}
    elif userType is userType.mainUser:
        return {"main_user":userType.mainUser}
    
@app.post("/user/details")
def post_user_details(userType:Union[UserType, str]):
    if userType is userType.mainUser:
        return {"status":200, 
                "mainUser information":db["col1"]}
    else:
        return {"status":400, 
                "message":"Cannot see other information than main user"}
