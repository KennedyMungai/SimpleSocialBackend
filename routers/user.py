from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from app import models, schemas, utils
from sqlalchemy.orm import Session

from app import schemas, models, utils
from app.database import get_db


router = APIRouter()


@router.get("/users/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id).first()

    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The user of id:{id} could not be found")

    return user


@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    A function to create users
    Args:
        user (schemas.UserCreate): This is the object that holds user information
        db (Session, optional): The db connection session

    Returns:
        user: The newly created user
    """
    # Hashing the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return user
