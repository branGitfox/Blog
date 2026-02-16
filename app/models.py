from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(100))
    password = Column(String(250))
    active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    avatar_url = Column(String(250))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)



