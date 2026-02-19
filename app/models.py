from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import  Relationship
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
    blogs = Relationship('Blog', back_populates='creator')



class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = Relationship('User',back_populates='blogs')
    title = Column(String(50))
    content = Column(String(250))
    tags = Column(String(250))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    cover_image = Column(String(250))
    comments = Relationship('Comment', back_populates='post')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    blog_id = Column(Integer, ForeignKey('blogs.id'))
    creator = Relationship('User', back_populates='comments')
    blog = Relationship('Blog', back_populates='post')
    content = Column(String(250))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
