from fastapi import APIRouter, HTTPException
from models import Vehicle, VehicleCreate
from db import SessionDep


router = APIRouter()

@router.post("/", response_model=Vehicle)
async def create_vehicle(new_vehicle: VehicleCreate, session: SessionDep):
    vehicle_data = new_vehicle.model_dump()
    vehicle = Vehicle.model_validate(vehicle_data)
    session.add(vehicle)
    session.commit()
    session.refresh(vehicle)
    return vehicle


@router.get("/", response_model=list[Vehicle], summary="Get all vehicles from the DB")
async def all_vehicles(session: SessionDep):
    return session.query(Vehicle).all()

@router.get("/{vehicle_id}", response_model=Vehicle)
async def get_one_vehicle(vehicle_id: int, session: SessionDep):
    vehicle_db = session.get(Vehicle, vehicle_id)
    if not vehicle_db:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle_db

@router.put("/{vehicle_id}", response_model=Vehicle)
async def update_vehicle(vehicle_id: int, vehicle_update: VehicleCreate, session: SessionDep):
    vehicle_db = session.get(Vehicle, vehicle_id)
    if not vehicle_db:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    update_data = vehicle_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(vehicle_db, key, value)
    
    session.add(vehicle_db)
    session.commit()
    session.refresh(vehicle_db)
    return vehicle_db

@router.delete("/{vehicle_id}")
async def delete_vehicle(vehicle_id: int, session: SessionDep):
    vehicle = session.get(Vehicle, vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    session.delete(vehicle)
    session.commit()
    return {"message": f"Vehicle {vehicle_id} deleted successfully"}