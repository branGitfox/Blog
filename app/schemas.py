from pydantic import BaseModel
from pydantic.v1 import EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    active: bool = True
    is_superuser: bool = False

