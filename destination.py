from fastapi import APIRouter, HTTPException
from models import Destination, DestinationCreate
from db import SessionDep

router = APIRouter()

@router.post("/", response_model=Destination)
async def create_destination(new_destination: DestinationCreate, session: SessionDep):
    destination_data = new_destination.model_dump()
    destination = Destination.model_validate(destination_data)
    session.add(destination)
    session.commit()
    session.refresh(destination)
    return destination


@router.get("/", response_model=list[Destination], summary="Get all destinations from the DB")
async def all_destinations(session: SessionDep):
    return session.query(Destination).filter(Destination.archived == False).all()

@router.get("/{destination_id}", response_model=Destination)
async def get_one_destination(destination_id: int, session: SessionDep):
    destination_db = session.get(Destination, destination_id)
    if not destination_db:
        raise HTTPException(status_code=404, detail="Destination not found")
    return destination_db

@router.put("/{destination_id}", response_model=Destination)
async def update_destination(destination_id: int, destination_update: DestinationCreate, session: SessionDep):
    destination_db = session.get(Destination, destination_id)
    if not destination_db:
        raise HTTPException(status_code=404, detail="Destination not found")
    
    if destination_db.archived:
        raise HTTPException(status_code=400, detail="Cannot update archived destination")
    
    update_data = destination_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(destination_db, key, value)
    
    session.add(destination_db)
    session.commit()
    session.refresh(destination_db)
    return destination_db

@router.delete("/{destination_id}")
async def archive_destination(destination_id: int, session: SessionDep):
    destination_db = session.get(Destination, destination_id)
    if not destination_db:
        raise HTTPException(status_code=404, detail="Destination not found")
    
    if destination_db.archived:
        raise HTTPException(status_code=400, detail="Destination already archived")
    
    destination_db.archived = True
    session.add(destination_db)
    session.commit()
    return {"message": f"Destination {destination_id} archived successfully"}

@router.post("/{destination_id}/unarchive")
async def unarchive_destination(destination_id: int, session: SessionDep):
    destination_db = session.get(Destination, destination_id)
    if not destination_db:
        raise HTTPException(status_code=404, detail="Destination not found")
    
    if not destination_db.archived:
        raise HTTPException(status_code=400, detail="Destination is not archived")
    
    destination_db.archived = False
    session.add(destination_db)
    session.commit()
    return {"message": f"Destination {destination_id} unarchived successfully"}
