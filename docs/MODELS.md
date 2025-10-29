# Diseño de Modelos

## Diagrama de Modelos

```mermaid
classDiagram
    class DestinationBase {
        +int id
        +string city
        +float distance
        +float price
        +bool archived
    }
    
    class VehicleBase {
        +string plate
        +string model
        +int capacity
        +string driver
        +string origin
        +int destination_id
    }
    
    class AppointmentBase {
        +int vehicle_id
        +int destination_id
    }
    
    class Destination {
        +int id
        +string city
    }
    
    class Vehicle {
        +int id
        +string driver
    }
    
    class Appointment {
        +int destination_id
        +int vehicle_id
        +datetime date
    }
    
    DestinationBase <|-- Destination
    VehicleBase <|-- Vehicle
    AppointmentBase <|-- Appointment
    Vehicle --> Destination : destination_id
    Appointment --> Vehicle : vehicle_id
    Appointment --> Destination : destination_id

```

## Detalles de los Modelos

### Destination
- Modelo para gestionar destinos de viaje
- **Atributos**:
  - `id`: Identificador único (PK)
  - `city`: Nombre de la ciudad destino
  - `distance`: Distancia en kilómetros
  - `price`: Precio del viaje
  - `archived`: Estado de archivo del destino

### Vehicle
- Modelo para gestionar vehículos
- **Atributos**:
  - `id`: Identificador único (PK)
  - `plate`: Placa del vehículo
  - `model`: Modelo del vehículo
  - `capacity`: Capacidad de pasajeros
  - `driver`: Nombre del conductor
  - `origin`: Ciudad de origen (default: "Bogotá")
  - `destination_id`: FK a Destination

### Appointment
- Modelo para gestionar citas/reservas
- **Atributos**:
  - `destination_id`: FK a Destination (PK)
  - `vehicle_id`: FK a Vehicle (PK)
  - `date`: Fecha y hora de la cita

## Relaciones

1. **Vehicle - Destination**
   - Un vehículo está asignado a un destino
   - Relación muchos a uno (N:1)

2. **Appointment - Vehicle/Destination**
   - Una cita conecta un vehículo con un destino
   - Relación muchos a muchos (N:M)
   - Incluye fecha y hora de la cita