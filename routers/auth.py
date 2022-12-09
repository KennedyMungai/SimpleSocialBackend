from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session


router = APIRouter(
    tags=['Authentication']
)


@router.post("/login")
def login():
    pass
