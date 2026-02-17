import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException
from .. import hashing, schemas, models
from .. token import create_access_token

def random_user_avatar(username: str):
    return f"https://ui-avatars.com/api/?name={username.replace(' ', '+')}"

class UserRepository:
    @staticmethod
    def create_user(request: schemas.User, db: Session):
        check_user = db.query(models.User).filter(models.User.email == request.email).count()
        if check_user > 0:
            return HTTPException(status_code=201, detail="Email already registered")
        new_user = models.User(email=request.email, username=request.username, password=hashing.hash_password(request.password), active=request.active, is_superuser=request.is_superuser, created_at=datetime.datetime.now(), avatar_url= random_user_avatar(request.username))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user




