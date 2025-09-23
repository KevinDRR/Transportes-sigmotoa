from db import SessionDep
from fastapi import APIRouter, HTTPException
from models import User, UserCreate

router = APIRouter()

@router.post("/", response_model=User, status_code=201)
async def create_user(new_user:UserCreate, session:SessionDep):
    user = User.model_validate(new_user)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/{user_id}", response_model=User)
async def get_one_user(user_id:int, session:SessionDep):
    user_db = session.get(User, user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    return user_db


@router.get("/", response_model=list[User])
async def get_all_users(session:SessionDep):
    users = session.query(User).all()
    return users




