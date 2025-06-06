from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, Annotated
from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True 
    # rating: Optional[int] = None

class PostCreate(PostBase):
    pass

#pass means that we are not adding any new fields, just inheriting from PostBase

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True

class Post(PostBase):
    id : int
    created_at: datetime
    owner_id: int
    owner: UserOut
    # owner is a UserOut model, which is the user who created the post

    class Config:
        orm_mode = True
    
# orm_mode = True allows us to convert the SQLAlchemy model to a Pydantic model
# so that we can return the Post model in the response
# else while pydantic expects a dictionary, we would be returning a SQLAlchemy model object

class PostOut(BaseModel):
    Post: Post
    votes: int

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    

        

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[int] = None
    
class Vote(BaseModel):
    post_id: int
    # dir: Annotated[int, Field(strict=True, gt=0, le= 1)]  # dir can only be 0 or 1, 0 means not voting, 1 means voting
    dir: conint(ge=0, le=1)  # dir can only be 0 or 1, 0 means not voting, 1 means voting
    # conint is a Pydantic type that allows us to specify constraints on integers