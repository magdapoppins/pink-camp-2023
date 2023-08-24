import crud
import models
import schemas
from config import Settings
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
settings = Settings()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = crud.get_post_by_title(db, title=post.title)
    if db_post:
        raise HTTPException(status_code=400, detail="Post with title already exists")
    return crud.create_post(db=db, post=post)


@app.get("/posts/", response_model=list[schemas.Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    post = crud.get_posts(db, skip=skip, limit=limit)
    return post


@app.get("/posts/{post_id}", response_model=schemas.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@app.get("/")
async def root():
    return {"message": "Hello Pink Camp!"}
