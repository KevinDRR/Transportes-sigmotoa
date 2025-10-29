from fastapi import APIRouter, Depends, HTTPException
from db import SessionDep
from models import AppointmentCreate, Vehicle, Destination, Appointment

router = APIRouter( )


@router.post("/", response_model=Appointment)
async def create_appoinment(new_appoinment: AppointmentCreate, session: SessionDep):
    data = new_appoinment.model_dump()
    destination_id = data.get("destination_id")
    vehicle_id = data.get("vehicle_id")
    vehicle_db=session.get(Vehicle,vehicle_id)
    destination_db=session.get(Destination,destination_id)

    if not destination_db or not vehicle_db:
        raise HTTPException(status_code=404, detail="Vehicle or destination not found")

    appointment = Appointment.model_validate(data)
    session.add(appointment)
    session.commit()
    session.refresh(appointment)

    return appointment

