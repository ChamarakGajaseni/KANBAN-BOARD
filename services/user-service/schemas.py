from pydantic import BaseModel, EmailStr

# Shared properties
class UserBase(BaseModel):
    username: str
    email: EmailStr

# For creating user (registration)
class UserCreate(UserBase):
    password: str

# For showing user (without password)
class UserDisplay(UserBase):
    id: int

    class Config:
        orm_mode = True

# For login
class UserLogin(BaseModel):
    username: str
    password: str

# For token response
class Token(BaseModel):
    access_token: str
    token_type: str
