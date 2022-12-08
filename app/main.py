"""
Summary:- This is the main file to a python API

Author:- Kennedy Mungai

Project:- Simple social media backend
"""
from typing import Optional
# from random import randrange
# import time
import mysql.connector

from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

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


def find_index_post(_id: int):
    """This function find posts bi index

    Args:
        _id (int): This is the id of the post

    Returns:
        post: Returns the post of the id indicated
    """
    for _i, _p in enumerate(my_posts):
        if _p['id'] == _id:
            return _i


@app.get("/")
def root():
    """
        This is an asynchronous function that functions as the root of the API

        Returns:
            JSON: Returns your typical JSON string although it is hardcoded
    """
    posts = cursor.execute('SELECT * FROM posts')
    return {"data": posts}


@app.get("/posts")
def get_posts():
    """
        This is a simple function that retrieves all the posts
    """
    posts = cursor.execute('SELECT * FROM posts')
    print(posts)

    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    """
        This is an API function thar creates posts
    """
    new_post = cursor.execute("""INSERT INTO posts(title, content, is_published) VALUES (%s, %s, %s)""",
                              (post.title, post.content, post.is_published))
    conn.commit()

    return {"data": new_post}


@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
def get_post(post_id: int):
    """
        This function is meant to fetch one individual post
    Args:
        id (int): The id of the post is passed here
    """
    get_post = cursor.execute(
        """SELECT * FROM posts WHERE id IS %s""", (str(post_id)))

    if not get_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    return {"Post": get_post}


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    """A simple function for deleting posts

    Args:
        post_id (int): The id of the post to be deleted
    """
    cursor.execute(
        """DELETE FROM posts WHERE id = %s""", (str(post_id)))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {post_id} does not exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{_id}")
def update_post(_id: int, _post: Post):
    """This is a function that executes at the update endpoint

    Args:
        _id (int): The identifier of the post
        _post (Post): The post itself

    Raises:
        HTTPException: This exception is raised if the post being looked for doesn't exist

    Returns:
        _type_: Returns a dictionary of the data that has been updated
    """
    cursor.execute("""UPDATE posts SET title= %s, content=%s, is_published=%s WHERE id = %s""",
                   (_post.title, _post.content, _post.is_published, str(_id)))

    conn.commit()

    updated_post = cursor.fetchone()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    return {"data": updated_post}
