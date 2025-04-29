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


""" Boards CRUD """

@app.get("/boards/", response_model=List[BoardModel])
async def read_boards(db: db_dependency, skip: int=0, limit: int=100):
    boards = db.query(models.Board).offset(skip).limit(limit).all()
    return boards

@app.post("/boards/", response_model=BoardModel)
async def create_boards(board: BoardBase, db: db_dependency):
    board = models.Board(**board.model_dump())
    db.add(board)
    db.commit()
    db.refresh(board)
    print('board created and save to database')
    return board

@app.put("/boards/{board_id}", response_model=BoardModel)
async def update_board(board_id: int, board: BoardBase, db: db_dependency):
    db_board = db.query(models.Board).filter(models.Board.id == board_id).first()
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    for key, value in board.model_dump().items():
        setattr(db_board, key, value)
    db.commit()
    db.refresh(db_board)
    return db_board

@app.delete("/boards/{board_id}")
async def delete_board(board_id: int, db: db_dependency):
    db_board = db.query(models.Board).filter(models.Board.id == board_id).first()
    if not db_board:
        raise HTTPException(status_code=404, detail="Board not found")
    db.delete(db_board)
    db.commit()
    return {"message": "Board deleted"}

""" Columns CRUD """

@app.get("/boards/{board_id}/columns/", response_model=List[BoardColumnModel])
async def read_columns(board_id: int, db: db_dependency):
    columns = db.query(models.BoardColumn).filter(models.BoardColumn.board_id == board_id).all()
    return columns

@app.post("/boards/{board_id}/columns/", response_model=BoardColumnModel)
async def create_column(board_id: int, column: BoardColumnBase, db: db_dependency):
    db_column = models.BoardColumn(**column.model_dump(), board_id=board_id)
    db.add(db_column)
    db.commit()
    db.refresh(db_column)
    return db_column

@app.put("/columns/{column_id}", response_model=BoardColumnModel)
async def update_column(column_id: int, column: BoardColumnBase, db: db_dependency):
    db_column = db.query(models.BoardColumn).filter(models.BoardColumn.id == column_id).first()
    if not db_column:
        raise HTTPException(status_code=404, detail="Column not found")
    for key, value in column.model_dump().items():
        setattr(db_column, key, value)
    db.commit()
    db.refresh(db_column)
    return db_column

@app.delete("/columns/{column_id}")
async def delete_column(column_id: int, db: db_dependency):
    db_column = db.query(models.BoardColumn).filter(models.BoardColumn.id == column_id).first()
    if not db_column:
        raise HTTPException(status_code=404, detail="Column not found")
    db.delete(db_column)
    db.commit()
    return {"message": "Column deleted"}

""" Tasks CRUD """

@app.get("/columns/{column_id}/tasks/", response_model=List[TaskModel])
async def read_tasks(column_id: int, db: db_dependency):
    tasks = db.query(models.Task).filter(models.Task.column_id == column_id).all()
    return tasks

@app.post("/columns/{column_id}/tasks/", response_model=TaskModel)
async def create_task(column_id: int, task: TaskBase, db: db_dependency):
    db_task = models.Task(**task.model_dump(), column_id=column_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.put("/tasks/{task_id}", response_model=TaskModel)
async def update_task(task_id: int, task: TaskBase, db: db_dependency):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.model_dump().items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: db_dependency):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted"}

