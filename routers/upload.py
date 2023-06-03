from fastapi import APIRouter, UploadFile, HTTPException, status

router = APIRouter(prefix="/upload", tags=["upload"])


@router.post("/file")
async def upload_file(file: UploadFile):
    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No file uploaded"
        )
    return {
        "filename": file.filename,
        "content-type": file.content_type,
    }
