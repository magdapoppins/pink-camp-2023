from database import Base
from sqlalchemy import Column, Integer, String


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    content = Column(String)
