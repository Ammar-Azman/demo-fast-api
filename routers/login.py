from fastapi import APIRouter, status
from models import UserInput, UserOutput, BaseInfo, CredentialInfo

router = APIRouter(prefix="/login", tags=["login"])

### FILTERTING CREDENTIAL DATA ###


## METHOD 1
@router.post(
    "/register1", response_model=UserOutput, status_code=status.HTTP_201_CREATED
)
def register_user(user: UserInput):
    return user.dict()


## METHOD 2
@router.post("/register2", response_model=BaseInfo)
def register_user_two(user: CredentialInfo):
    return user.dict()


##  METHOD 3
@router.post(
    "/register3/", response_model=UserInput, response_model_exclude={"password"}
)
def register_user_three(user: UserInput):
    return user.dict()
