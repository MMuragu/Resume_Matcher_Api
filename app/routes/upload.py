import os
from typing import Annotated
from fastapi import UploadFile, HTTPException, File, APIRouter

router = APIRouter()
accepted_extensions = ['.pdf', '.docx', '.txt', '.doc', '.png', '.jpg', '.jpeg']

@router.post("/upload_resume")
async def upload_resume(
    file: Annotated[UploadFile, File(description="Upload a resume file")],
):
    filename = file.filename
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension not in accepted_extensions:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF, DOCX, TXT, DOC, PNG, JPG, and JPEG files are accepted.")
    
    contents = await file.read()

    if not contents:
        raise HTTPException(status_code=400, detail="File is empty.")

    os.makedirs("temp_uploads", exist_ok=True)
    save_path = f"temp_uploads/{filename}"

    with open(save_path, "wb") as f:
        f.write(contents)

    return {"filename": filename, "message": "File uploaded and saved successfully."}
