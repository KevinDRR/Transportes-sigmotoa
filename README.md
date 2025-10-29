# Transport Management System

Este es un sistema de gestión de transporte desarrollado con FastAPI que permite administrar destinos, vehículos y citas de transporte.

## Características

- Gestión de destinos (crear, editar, listar, archivar y desarchivar)
- Gestión de vehículos (crear, editar, listar y eliminar)
- Sistema de citas para reservas de transporte

## Requisitos

- Python 3.14.0
- FastAPI
- SQLModel
- Uvicorn 

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/sigmotoa/Dev_25_3_projectMars.git
cd Dev_25_3_projectMars
```

2. Crear y activar un entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\activate

```

3. Instalar dependencias:
```bash
pip install fastapi sqlmodel uvicorn
```

## Uso

1. Iniciar el servidor:
```bash
uvicorn main:app --reload
```

2. Acceder a la documentación de la API:
- http://localhost:8000/docs

## Endpoints

### Destinos

- `POST /`: Crear nuevo destino
- `GET /`: Listar todos los destinos activos
- `GET /{destination_id}`: Obtener un destino específico
- `PUT /{destination_id}`: Actualizar un destino
- `DELETE /{destination_id}`: Archivar un destino
- `POST /{destination_id}/unarchive`: Desarchivar un destino

### Vehículos

- `POST /`: Crear nuevo vehículo
- `GET /`: Listar todos los vehículos
- `GET /{vehicle_id}`: Obtener un vehículo específico
- `PUT /{vehicle_id}`: Actualizar un vehículo
- `DELETE /{vehicle_id}`: Eliminar un vehículo

## Ejemplos de Uso

### Crear un Destino

```json
POST /
{
    "city": "Medellín",
    "distance": 420.5,
    "price": 150000
}
```

### Crear un Vehículo

```json
POST /
{
    "plate": "ABZ-532",
    "model": "Mercedez",
    "capacity": 15,
    "driver": "John",
    "destination_id": 1
}
```

## Base de Datos

El sistema utiliza SQLite como base de datos, almacenada en el archivo `Transport.sqlite3`, la estructura de la base de datos se maneja automáticamente a través de SQLModel.