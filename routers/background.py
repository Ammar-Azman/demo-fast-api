from fastapi import APIRouter, BackgroundTasks
import random

router = APIRouter(prefix="/notification", tags=["background"])


def write_noti(email: str, message=""):
    random_num = random.randint(1, 1000)
    with open(f"noti.txt", mode="w") as noti_file:
        content = f"notification_{random_num} for {email}: {message}"
        noti_file.write(content)


@router.post("/{email}")
async def send_notification(email: str, background_task: BackgroundTasks):
    background_task.add_task(write_noti, email, message="some noti")
    return {"message": "noti sent in the background"}
