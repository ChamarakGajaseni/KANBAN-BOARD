from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Text
from sqlalchemy.orm import relationship


class Board(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)  # The whole Board"

    columns = relationship('BoardColumn', back_populates='board', cascade="all, delete")
    
class BoardColumn(Base):
    __tablename__ = 'board_columns'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    position = Column(Integer, default=0)  # Order of columns (optionally dragging)
    board_id = Column(Integer, ForeignKey('boards.id'))
    
    board = relationship("Board", back_populates="columns")
    tasks = relationship('Task', back_populates='column', cascade="all, delete")
    
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    description = Column(Text)
    status = Column(String(255), default="To Do")  # optional
    tags = Column(String(255))  # e.g., "frontend, urgent", comma-separated tags
    position = Column(Integer, default=0)  # for ordering tasks inside column

    # Relationships
    column_id = Column(Integer, ForeignKey('board_columns.id'), nullable=False)
    # assigned_user_id = Column(Integer, ForeignKey('users.id'), nullable=True)

    column = relationship('BoardColumn', back_populates='tasks')
    # assigned_user = relationship('User', back_populates='tasks')