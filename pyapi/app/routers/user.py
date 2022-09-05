from typing import List
from fastapi import FastAPI, Depends, APIRouter
from .. import dbmodels, schemas
from ..database import engine, get_db
from sqlalchemy.orm import Session




router = APIRouter()



@router.get("/user", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):

    user=db.query(dbmodels.User).all()

    if user == None :
        print("no users found")
        return("no users found")
    
    return {user}



@router.post("/user",response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    #print(post)
    #print(post.dict())
    #new_user = models.User(title = post.title, content = post.content, published = post.published)
    #or
    new_user = dbmodels.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
