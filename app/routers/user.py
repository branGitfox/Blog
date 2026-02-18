from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, models
from .. schemas import CreateUser, User
from .. repository import userRepository
from .. import OAuth2
from .. repository.userRepository import UserRepository
router  =  APIRouter(prefix="/user", tags=["users"])


@router.post('/')
def create(request: CreateUser, db: Session = Depends(database.get_db)):
    return UserRepository.create_user(request, db)


@router.get('/')
def get_users(db: Session = Depends(database.get_db), get_current_user: User = Depends(OAuth2.get_current_user)):
    return UserRepository.alls(db)