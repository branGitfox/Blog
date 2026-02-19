from sqlalchemy.orm import Session
from .. import models
class BlogRepository:


    @staticmethod
    def alls(db: Session):
        return db.query(models.Blog).all()

    @staticmethod
    def get(blog_id:int, db: Session):
        return db.query(models.Blog).get(blog_id)