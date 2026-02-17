from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from fastapi.security import  OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database
from .. schemas import User
from .. schemas import  Token
from ..  import models, hashing
from .. token import create_access_token
from .. import OAuth2

router  =  APIRouter(prefix='/token',tags=["authentification"])


@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid email or password")
    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get('/me')
def get_current_user(me: User = Depends(OAuth2.get_current_user)):
    return me