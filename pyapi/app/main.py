from typing import List
from fastapi import FastAPI, Depends , APIRouter
from . import dbmodels, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user


dbmodels.Base.metadata.create_all(bind=engine)

router =  APIRouter()

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
