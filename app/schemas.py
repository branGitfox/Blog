import datetime
from typing import Optional, List

from fastapi import Form, UploadFile, File
from pydantic import BaseModel
from pydantic import EmailStr


class User(BaseModel):
    id: Optional[int] = None
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

class Creator(BaseModel):
    username: str
    avatar_url: str

class Comment(BaseModel):
    content: str
    created_at: datetime.datetime
    creator: Creator


class Blog(BaseModel):
    id: int
    title: str
    content: str
    tags: str
    cover_image:str
    created_at:datetime.datetime
    creator: Creator
    comments: List[Comment]


