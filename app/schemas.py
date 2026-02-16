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

