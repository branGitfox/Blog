from fastapi import HTTPException, Depends
from jwt import InvalidTokenError
from sqlalchemy.orm import Session
from starlette import status

from app import database, models
from app.schemas import TokenData

SECRET_KEY = "622a41549d2fd8dcfd0b6c4664a1cfeedbb6e221d3c8c4f39f7d6646b5d25ff6"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
import jwt
from datetime import datetime, timedelta, timezone

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception: HTTPException, db: Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
        user = db.query(models.User).filter(models.User.email == token_data.email).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token")
        return user
    except InvalidTokenError:
        raise credentials_exception


