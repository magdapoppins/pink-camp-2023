import models
import schemas
from sqlalchemy.orm import Session


def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def get_post_by_title(db: Session, title: str):
    return db.query(models.Post).filter(models.Post.title == title).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
