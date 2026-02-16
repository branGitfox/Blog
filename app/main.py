from fastapi import FastAPI
from app.routers import user
from app.models import  Base
from app.database import engine
app = FastAPI()

# creating all tables from models
Base.metadata.create_all(engine)


app.include_router(user.router)