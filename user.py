from db import SessionDep
from fastapi import APIRouter
from models import User, UserCreate

router = APIRouter()

@router.post("/", response_model=User)
async def create_user(new_user:UserCreate, session:SessionDep):
    user = User.model_validate(new_user)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user