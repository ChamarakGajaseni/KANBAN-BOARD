from pydantic import BaseModel
from typing import List, Optional

# === Board Schemas ===
class BoardBase(BaseModel):
    name: str
    
class BoardModel(BoardBase):
    id: int
    class Config:
        orm_mode = True
        from_attributes = True
        
# === Task Schemas ===
class TaskBase(BaseModel):
    title: str
    status: Optional[str] = "To Do"
    tags: Optional[str] = None
    position: Optional[int] = 0
    # assigned_user_id: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    column_id: int

    class Config:
        orm_mode = True

# === BoardColumn Schemas ===
class BoardColumnBase(BaseModel):
    name: str
    position: Optional[int] = 0

class BoardColumnModel(BoardColumnBase):
    id: int
    # class Config:
    #     orm_mode = True
    #     from_attributes = True

class BoardColumnOut(BoardColumnBase):
    id: int
    board_id: int
    tasks: List[TaskOut] = []

    class Config:
        orm_mode = True

# === Board Schemas ===
# class BoardBase(BaseModel):
#     name: str
#     description: Optional[str] = None

# class BoardCreate(BoardBase):
#     pass



# class BoardOut(BoardBase):
#     id: int
#     columns: List[BoardColumnOut] = []

#     class Config:
#         orm_mode = True
