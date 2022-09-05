
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
      fname: str
      sname: str

class UserCreate(UserBase):
      class Config:
            orm_mode = True

class User(UserBase):
      id: str      
      class Config:
            orm_mode = True

class PostBase(BaseModel):
      title: str
      content: str
      published: bool = True
      uid: int

class PostCreate(PostBase):
     pass

class Post(PostBase):

      id: int
      created_at: datetime
      class Config:
            orm_mode = True