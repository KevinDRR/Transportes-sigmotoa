from fastapi import FastAPI

import appoinment
import vehicle
import destination
from db import create_tables
##from pet import APIRouter

app = FastAPI(lifespan=create_tables, title="Vehicle API")
app = FastAPI(lifespan=create_tables, title="Destination API")
app.include_router(vehicle.router, tags=["vehicle"], prefix="/vehicles")
app.include_router(appoinment.router, tags=["appointment"], prefix="/appointments")
app.include_router(destination.router, tags=["destination"], prefix="/destinations")

