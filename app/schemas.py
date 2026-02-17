import datetime
from pydantic import BaseModel
from pydantic import EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    active: bool = True
    is_superuser: bool = False
    avatar_url: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

