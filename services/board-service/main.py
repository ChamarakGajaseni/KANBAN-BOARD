from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from schemas import *

app = FastAPI()

@app.get('/')
async def check():
    return 'hello'

@app.get("/api")
async def root():
    return {"message": "Another Backend Test"}

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

    

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)



@app.get("/boards/", response_model=List[BoardModel])
async def read_boards(db: db_dependency, skip: int=0, limit: int=100):
    boards = db.query(models.Board).offset(skip).limit(limit).all()
    return boards

@app.post("/boards/", response_model=BoardModel)
async def create_boards(board: BoardBase, db: db_dependency, skip: int=0, limit: int=100):
    board = models.Board(**board.model_dump())
    db.add(board)
    db.commit()
    db.refresh(board)
    print('board created and save to database')
    return board
