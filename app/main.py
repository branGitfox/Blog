from fastapi import FastAPI
from app.routers import user, authentification
from app.models import  Base
from app.database import engine
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
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
# creating all tables from models
Base.metadata.create_all(engine)


app.include_router(user.router)
app.include_router(authentification.router)
