from fastapi import APIRouter, File, UploadFile
from typing import Annotated

router = APIRouter(prefix="/upload", tags=["upload"])


@router.post("/file")
async def upload_file(file: UploadFile):
    return {"filename": file.filename}
