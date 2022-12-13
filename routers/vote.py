from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from app import schemas, database, models, oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    if (vote.dir == 1):
        pass
    else:
        pass
