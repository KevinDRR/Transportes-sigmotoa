import datetime
from sqlmodel import SQLModel, Field

class DestinationBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    city: str | None = Field(description="Destination city")
    distance: float | None = Field(description="Distance in km")
    price: float | None = Field(description="Destination price")
    archived: bool | None = Field(default=False, description="Destination is archived?")

class VehicleBase(SQLModel):
    plate: str  | None = Field(description="Vehicle plate")
    model: str  | None= Field(description="Vehicle model")
    capacity: int  | None = Field(description="Vehicle capacity")
    driver: str | None = Field(description="Vehicle driver")
    origin: str = "Bogotá"
    
    destination_id: int = Field(foreign_key="destination.id")

class AppointmentBase(SQLModel):
    vehicle_id: int
    destination_id: int

class Appointment(AppointmentBase, table=True):
    destination_id: int | None = Field(default=None, foreign_key="destination.id", primary_key=True)
    vehicle_id: int | None = Field(default=None, foreign_key="vehicle.id", primary_key=True)
    date: datetime.datetime | None = Field(default_factory=datetime.datetime.now)

class Vehicle(VehicleBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    driver: str | None = Field(description="Vehicle driver")

class Destination(DestinationBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    city: str | None = Field(description="Destination city")

class DestinationCreate(DestinationBase):
    pass

class DestinationUpdate(DestinationBase):
    pass

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(VehicleBase):
    pass

class AppointmentCreate(AppointmentBase):
    pass
