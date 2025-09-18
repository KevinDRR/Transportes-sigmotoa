from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from utils import Kind

class PetBase(SQLModel):
    name: str  | None = Field(description="Pet name")
    year: int  | None= Field(description="Pet year")
    kind: Kind  | None = Field(description="Pet kind", default=Kind.Dog)

class Pet(PetBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class PetCreate(PetBase):
    pass

class PetUpdate(PetBase):
    pass

class UserBase(SQLModel):
    name: str | None = Field(description="User name")
    year: int | None = Field(description="User year")
    status: bool | None = Field(description="User status", default=True)

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class UserCreate(UserBase):
    pass