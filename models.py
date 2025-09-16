from pydantic import BaseModel
from utils import Kind


class PetBase(BaseModel):
    name: str
    year: int
    kind: Kind

class Pet(PetBase):
    id: int

class PetCreate(PetBase):
    pass

class PetUpdate(PetBase):
    pass