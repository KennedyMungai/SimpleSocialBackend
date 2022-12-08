from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str


class CreatePost(BaseModel):
    title: str
    content: str
    is_published: bool


class UpdatePost(BaseModel):
    title: str
    content: str
    is_published: bool = True
