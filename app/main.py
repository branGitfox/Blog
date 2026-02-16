from fastapi import FastAPI
from routers import user
from models import  Base
from database import engine
app = FastAPI()

# creating all tables from models
Base.metadata.create_all(engine)


app.include_router(user.router)