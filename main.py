from fastapi import FastAPI, APIRouter
from sqlalchemy.event import api

import pet
import estudiantes
import user
from db import create_tables
##from pet import APIRouter

app = FastAPI(lifespan=create_tables, title="Pet API")
app.include_router(pet.router, tags=["pet"], prefix="/pets")
app.include_router(user.router, tags=["user"], prefix="/users")
app.include_router(estudiantes.router, tags=["estudiantes"], prefix="/estudiantes" )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

