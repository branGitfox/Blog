from fastapi import HTTPException
from jwt import InvalidTokenError
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

def verify_token(token: str, credentials_exception: HTTPException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception
