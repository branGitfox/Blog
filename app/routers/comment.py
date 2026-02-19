from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database, OAuth2
from .. repository.commentRepository import CommentRepository

router = APIRouter(prefix="/comments", tags=["comments"])


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_comment(request: schemas.PostComment, db:Annotated[Session, Depends(database.get_db)], get_current_user: Annotated[schemas.User, Depends(OAuth2.get_current_user)]):
    user_id = get_current_user.id
    return CommentRepository.create(db, request,user_id )

