import os
from datetime import datetime

from fastapi import APIRouter, Form, UploadFile, File, HTTPException
import uuid
import shutil

from sqlalchemy.orm import Session

from .. import schemas, models, OAuth2, database
from fastapi.params import Depends

router = APIRouter(prefix='/blogs', tags=['blogs'])


UPLOAD_DIR = 'app/uploads'
@router.post('/')
async def create_blog(title: str = Form(...), tags:str = Form(...), content:str = Form(...), file: UploadFile = File(...), get_current_user:schemas.User=Depends(OAuth2.get_current_user), db : Session = Depends(database.get_db)):
    try:
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        file_ext = file.filename.split('.')[-1]
        if file_ext not in ['jpg', 'jpeg', 'png']:
            raise HTTPException(status_code=201, detail='Unsupported file type')
        new_file_name = f"{uuid.uuid4()}.{file_ext}"
        file_path = os.path.join(UPLOAD_DIR, new_file_name)
        with open(file_path, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except FileExistsError:
        raise HTTPException(status_code=404, detail='Failed to upload the file')
    new_blog = models.Blog(title=title, content=content, tags=tags, created_at=datetime.now(), cover_image=file_path, user_id=get_current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# @router.get('/blogs')
# def get_alls(db: Session = Depends(database.get_db)):
#     return blogRepository

