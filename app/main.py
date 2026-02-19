from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.routers import user, authentification, blog, comment
from app.models import  Base
from app.database import engine
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.mount('/uploads', StaticFiles(directory='app/uploads'), name='uploads')

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)


app.include_router(user.router)
app.include_router(authentification.router)
app.include_router(blog.router)
app.include_router(comment.router)
