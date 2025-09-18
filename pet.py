from fastapi import APIRouter
from models import Pet, PetCreate
from db import SessionDep


router = APIRouter()

@router.post("/", response_model=Pet)
async def create_pet(new_pet: PetCreate, session: SessionDep):
    pet = Pet.model_validate(new_pet)
    session.add(pet)
    session.commit()
    session.refresh(pet)
    return pet


@router.get("/", response_model=list[Pet], summary="Get all pets from the DB")
async def all_pets(session: SessionDep):
    return session.query(Pet).all()
