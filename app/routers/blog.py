import os
from fastapi import APIRouter, Form, UploadFile, File, HTTPException
import uuid
import shutil
router = APIRouter(prefix='/blogs', tags=['blogs'])

from .. import schemas

UPLOAD_DIR = 'app/uploads'
@router.post('/')
async def create_blog(title: str = Form(...), tags:str = Form(...), content:str = Form(...), file: UploadFile = File(...)):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_ext = file.filename.split('.')[-1]
    if file_ext not in ['jpg', 'jpeg', 'png']:
        raise HTTPException(status_code=201, detail='Unsupported file type')
    new_file_name = f"{uuid.uuid4()}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, new_file_name)

    with open(file_path, 'wb') as f:
        shutil.copyfileobj(file.file, f)

    return {"message": "Blog created successfully!"}

