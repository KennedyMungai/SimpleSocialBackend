from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from app import schemas, database, models, oauth2


router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote():
