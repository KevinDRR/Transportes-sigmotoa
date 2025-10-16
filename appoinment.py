from fastapi import APIRouter, Depends, HTTPException
from db import SessionDep
from models import AppointmentCreate, Pet, Vet, Appointment

router = APIRouter( )


@router.post("/", response_model=Appointment)
async def create_appoinment(new_appoinment: AppointmentCreate, session: SessionDep):
    data = new_appoinment.model_dump()
    vet_id = data.get("vet_id")
    pet_id = data.get("pet_id")
    vet_db=session.get(Vet,vet_id)
    pet_db=session.get(Pet,pet_id)

    if not vet_db or not pet_db:
        raise HTTPException(status_code=404, detail="Pet or Vet not found")

    appoinment=Appointment.model_validate(data)
    session.add(appoinment)
    session.commit()
    session.refresh(appoinment)


    return appoinment

