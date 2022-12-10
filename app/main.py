"""
Summary:- This is the main file to a python API

Author:- Kennedy Mungai

Project:- Simple social media backend
"""
from typing import Optional
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, BaseSettings
from . import models
from .database import engine
from routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

router = APIRouter()


class Post(BaseModel):
    """
    This is the base model for the Post objects
    Args:
        BaseModel: The library that makes ot easy to model data
    """
    title: str
    content: str
    is_published: bool = True
    rating: Optional[int] = None


class Settings(BaseSettings):
    database_password: str = "localhost"
    database_username: str = "root"
    secret_key: str = "123456789"


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    """
        This is an asynchronous function that functions as the root of the API

        Returns:
            JSON: Returns your typical JSON string although it is hardcoded
    """
    # posts = cursor.execute('SELECT * FROM posts')
    return "posts"
