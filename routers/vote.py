from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter


router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)
