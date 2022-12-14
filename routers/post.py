from typing import List, Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db

from app import oauth2, schemas, models


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get(
    "/",
    response_model=List[schemas.PostOut]
)
def get_posts(
        db: Session = Depends(get_db),
        current_user: int = Depends(oauth2.get_current_user),
        limit: int = 10,
        skip: int = 0,
        search: Optional[str] = ""
):
    """
        This is a simple function that retrieves all the posts
    """
    # posts = cursor.execute('SELECT * FROM posts')
    # print(posts)

    # posts = db.query(models.Post).filter(
    #     models.Post.title.contains(search)).limit(limit).offset(skip).all()

    posts = db.query(models.Post, func.count(models.Vote.post_id).label("Votes")).join(models.Vote, models.Vote.post_id ==
                                                                                       models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    """
        This is an API function thar creates posts
    """
    # new_post = cursor.execute("""INSERT INTO posts(title, content, is_published) VALUES (%s, %s, %s)""",
    #                           (post.title, post.content, post.is_published))
    # conn.commit()

    new_post = models.Post(owner_id=current_user.id,  ** post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/{post_id}", status_code=status.HTTP_200_OK, response_model=schemas.PostOut)
def get_post(post_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    """
        This function is meant to fetch one individual post
    Args:
        id (int): The id of the post is passed here
    """
    # get_post = cursor.execute(
    #     """SELECT * FROM posts WHERE id IS %s""", (str(post_id)))

    # if not get_post:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"post with id: {id} was not found")
    # post = db.query(models.Post).filter(models.Post.id == id).first()

    post = db.query(models.Post, func.count(models.Vote.post_id).label("Votes")).join(models.Vote, models.Vote.post_id ==
                                                                                      models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found.")

    # if post.owner_id != current_user.id:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform the requested action")

    return post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    """A simple function for deleting posts

    Args:
        post_id (int): The id of the post to be deleted
    """
    # cursor.execute(
    #     """DELETE FROM posts WHERE id = %s""", (str(post_id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    # if deleted_post is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Post with id: {post_id} does not exist")
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")

    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{_id}", response_model=schemas.Post)
def update_post(_id: int, _post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    """This is a function that executes at the update endpoint

    Args:
        _id (int): The identifier of the post
        _post (Post): The post itself

    Raises:
        HTTPException: This exception is raised if the post being looked for doesn't exist

    Returns:
        _type_: Returns a dictionary of the data that has been updated
    """
    # cursor.execute("""UPDATE posts SET title= %s, content=%s, is_published=%s WHERE id = %s""",
    #                (_post.title, _post.content, _post.is_published, str(_id)))

    # conn.commit()

    # updated_post = cursor.fetchone()

    # if updated_post == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"post with id: {id} does not exist")
    # return updated_post

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The post with id = {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform the requested action")

    post_query.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return post_query.first()
