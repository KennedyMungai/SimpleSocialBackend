"""
Summary:- This is the main file to a python API

Author:- Kennedy Mungai

Project:- Simple social media backend
"""
from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException

import mysql.connector

app = FastAPI()

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='xknightmare12873',
        database='fastapicoursedb'
    )

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
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "title of post 1", "content": "Content of post 1", "id": 1},
    {"title": "Favorite foods", "content": "I like pizza", "id": 2}
]


def find_post(_id: int):
    """
    This is the function that finds posts
    Args:
        _id (int): This is the id of the post in the database
    """
    for _p in my_posts:
        if _p["id"] == _id:
            return _p
