from fastapi import APIRouter, Depends, status, HTTPException, Response


router = APIRouter(
    tags=['Authentication']
)


@router.post("/login")
def login():
    pass
