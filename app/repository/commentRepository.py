from sqlalchemy.orm import Session
from app import schemas, models


class CommentRepository:
    @staticmethod
    def create(db: Session, request: schemas.PostComment, user_id:int):
        new_comment = models.Comment(content=request.content, user_id=user_id, blog_id=request.blog_id)
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)
        return new_comment