from sqlalchemy.orm import Session
from .. schemas import User
from fastapi import HTTPException, Depends
from ..database import  get_db
from .. import models

class UserRepository:

    def create(self, request: User, db: Session = Depends(get_db)):
        check_user = db.query(models.User).filter(models.User.email == request.email).count()
        if check_user > 0:
            return HTTPException(status_code=201, detail="Email already registered")
        new_user = User(email=request.email, username=request.username, password=request.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user