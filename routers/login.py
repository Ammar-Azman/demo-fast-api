from fastapi import APIRouter
from models import UserInput, UserOutput

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/register", response_model=UserOutput)
def register_user(user: UserInput):
    return user
