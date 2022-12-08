@app.get("/users/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id).first()

    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The user of id:{id} could not be found")

    return user
