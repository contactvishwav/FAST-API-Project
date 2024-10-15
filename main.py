from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, User_Updated
from typing import List

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Vijayasankar", 
        last_name="Dhanapal",
        gender=Gender.male,
        roles=[Role.student]
    ),

    User(
        id=uuid4(),
        first_name="Shanthi",
        last_name="Kanakaraj",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return "Hello World"

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    if any(u.first_name == user.first_name and u.last_name == user.last_name for u in db):
        raise HTTPException(
        status_code=208,
        detail=f"the provided user already exists in database"
        )
    else:
        db.append(user)
        return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} does not exist in database"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user_updated: User_Updated):
    for user in db:
        if user.id == user_id:
            if (user_updated.first_name != None):
                user.first_name = user_updated.first_name
            if (user_updated.last_name != None):
                user.last_name = user_updated.last_name
            if (user_updated.middle_name != None):
                user.middle_name = user_updated.middle_name
            if (user_updated.roles != None):
                user.roles = user_updated.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} does not exist in database"
    )