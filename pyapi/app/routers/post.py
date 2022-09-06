from typing import List
from fastapi import FastAPI, Depends , APIRouter  , status  , HTTPException
from .. import dbmodels, schemas
from ..database import engine, get_db
from sqlalchemy.orm import Session


router = APIRouter()





@router.get("/posts", response_model= List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    post = db.query(dbmodels.Post).all()
    print(post)
    return  post

@router.get("/posts/{id}", response_model= schemas.Post)
def get_posts(id: int , db: Session = Depends(get_db)):
    post = db.query(dbmodels.Post).filter(dbmodels.Post.id == id).first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id: {id} doesnt not exist")
    return  post


@router.put("/posts/{id}", response_model= schemas.Post)
def update_posts(id: int , up_post : schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(dbmodels.Post).filter(dbmodels.Post.id == id)
    post  = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id: {id} doesnt not exist")
    
    post_query.update(up_post.dict(), synchronize_session=False)

    db.commit()

    return  post_query.first()
    
@router.post("/posts", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):

    new_post = dbmodels.Post(**post.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post