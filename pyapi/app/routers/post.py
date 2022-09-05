from typing import List
from fastapi import FastAPI, Depends , APIRouter
from .. import dbmodels, schemas
from ..database import engine, get_db
from sqlalchemy.orm import Session

router = APIRouter()





@router.get("/posts", response_model= List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    post = db.query(dbmodels.Post).all()

    print(post)
    return { post}



@router.post("/posts", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):

    new_post = dbmodels.Post(**post.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post