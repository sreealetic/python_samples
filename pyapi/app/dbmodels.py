from xmlrpc.client import Boolean
from .database import Base
from sqlalchemy import Column , Integer, String , Boolean,  ForeignKey

from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class User(Base):

    __tablename__= "user"
    
    id = Column(Integer, primary_key=True, nullable=False)
    fname = Column(String,nullable=False)
    sname = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    

class Post(Base):

    __tablename__= "posts"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String,nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    uid = Column(Integer, ForeignKey("user.id"),nullable=False)


