from fastapi import APIRouter
from models import UserInput, UserOutput, BaseInfo, CredentialInfo

router = APIRouter(prefix="/login", tags=["login"])

### FILTERTING CREDENTIAL DATA ###


## METHOD 1
@router.post("/register1", response_model=UserOutput)
def register_user(user: UserInput):
    return user


## METHOD 2
@router.post("/register2", response_model=BaseInfo)
def register_user_two(user: CredentialInfo):
    return user


##  METHOD 3
@router.post(
    "/register3/", response_model=UserInput, response_model_exclude={"password"}
)
def register_user_three(user: UserInput):
    return user
