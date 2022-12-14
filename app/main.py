"""
Summary:- This is the main file to a python API

Author:- Kennedy Mungai

Project:- Simple social media backend
"""
from typing import Optional
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, BaseSettings

from routers.vote import vote
from . import models
from .database import engine
from routers import post, user, auth
from config import settings

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    """
        This is an asynchronous function that functions as the root of the API

        Returns:
            JSON: Returns your typical JSON string although it is hardcoded
    """
    # posts = cursor.execute('SELECT * FROM posts')
    return "posts"
