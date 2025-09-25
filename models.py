import datetime
from sqlmodel import SQLModel, Field, Relationship
from utils import Kind


class UserBase(SQLModel):
    name: str | None = Field(description="User name")
    year: int | None = Field(description="User year")
    status: bool | None = Field(description="User status", default=True)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    pets: list["Pet"] = Relationship(back_populates="user")

class UserCreate(UserBase):
    pass


class PetBase(SQLModel):
    name: str  | None = Field(description="Pet name")
    year: int  | None= Field(description="Pet year")
    kind: Kind  | None = Field(description="Pet kind", default=Kind.Dog)
    alive: bool | None = Field(description="Pet alive", default=True)

class Pet(PetBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id:int =Field(foreign_key="user.id")
    user: User = Relationship(back_populates="pets")

    vets: list["Vet"] = Relationship(back_populates="pets", link_model="Appointment")

class PetCreate(PetBase):
    user_id:int =Field(foreign_key="user.id")


class PetUpdate(PetBase):
    pass

class VetBase(SQLModel):
    name: str | None = Field(description="Vet name")

class Vet(VetBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    pets: list["Pet"] = Relationship(back_populates="vets", link_model="Appointment")


class Appointment(SQLModel, table=True):
    pet_id: int | None = Field(default=None, foreign_key="pet.id", primary_key=True)
    vet_id: int | None = Field(default=None, foreign_key="vet.id", primary_key=True)
    date: datetime.datetime | None = Field(default=datetime.datetime.now())



