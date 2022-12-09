"""
Summary:- This is the main file to a python API

Author:- Kennedy Mungai

Project:- Simple social media backend
"""
from typing import Optional
import mysql.connector
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

from . import models
from .database import engine

from routers import post, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

router = APIRouter()


try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='xknightmare12873',
        database='simple_social_db'
    )

    if conn.is_connected():
        print("Connected to the mysql database")

    cursor = conn.cursor(dictionary=True)
except mysql.connector.Error as error:
    print(error)
    exit(1)


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


@app.get("/")
def root():
    """
        This is an asynchronous function that functions as the root of the API

        Returns:
            JSON: Returns your typical JSON string although it is hardcoded
    """
    posts = cursor.execute('SELECT * FROM posts')
    return posts
