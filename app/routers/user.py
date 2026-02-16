from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database
from .. schemas import User
from .. repository import userRepository
router  =  APIRouter(prefix="/user", tags=["users"])


@router.post('/')
def create(request: User, db: Session = Depends(database.get_db)):
    return userRepository.UserRepository.create_user(request, db)
