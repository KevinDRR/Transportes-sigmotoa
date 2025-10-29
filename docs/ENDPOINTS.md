# Documentación de Endpoints de la API

## Estructura General de la API

```plaintext
/
├── /destinations/
│   ├── POST /                    # Crear nuevo destino
│   ├── GET /                     # Listar todos los destinos activos
│   ├── GET /{destination_id}     # Obtener un destino específico
│   ├── PUT /{destination_id}     # Actualizar un destino
│   ├── DELETE /{destination_id}  # Archivar un destino
│   └── POST /{destination_id}/unarchive  # Desarchivar un destino
│
├── /vehicles/
│   ├── POST /                    # Crear nuevo vehículo
│   ├── GET /                     # Listar todos los vehículos
│   ├── GET /{vehicle_id}        # Obtener un vehículo específico
│   ├── PUT /{vehicle_id}        # Actualizar un vehículo
│   └── DELETE /{vehicle_id}     # Eliminar un vehículo
│
└── /appointments/
    ├── POST /                    # Crear nueva cita
    └── GET /                     # Listar todas las citas
```

## Endpoints Detallados

### Destinos (Destinations)

#### 1. Crear Destino
- **Método**: POST
- **Ruta**: `/destinations/`
- **Descripción**: Crea un nuevo destino en el sistema
- **Body**:
  ```json
  {
    "city": "string",
    "distance": float,
    "price": float
  }
  ```
- **Respuesta Exitosa** (200):
  ```json
  {
    "id": int,
    "city": "string",
    "distance": float,
    "price": float,
    "archived": false
  }
  ```

#### 2. Listar Destinos
- **Método**: GET
- **Ruta**: `/destinations/`
- **Descripción**: Obtiene todos los destinos no archivados
- **Respuesta Exitosa** (200):
  ```json
  [
    {
      "id": int,
      "city": "string",
      "distance": float,
      "price": float,
      "archived": false
    }
  ]
  ```

#### 3. Obtener Destino Específico
- **Método**: GET
- **Ruta**: `/destinations/{destination_id}`
- **Parámetros URL**: destination_id (integer)
- **Respuesta Exitosa** (200):
  ```json
  {
    "id": int,
    "city": "string",
    "distance": float,
    "price": float,
    "archived": boolean
  }
  ```
- **Errores**:
  - 404: Destino no encontrado

#### 4. Actualizar Destino
- **Método**: PUT
- **Ruta**: `/destinations/{destination_id}`
- **Parámetros URL**: destination_id (integer)
- **Body**:
  ```json
  {
    "city": "string",
    "distance": float,
    "price": float
  }
  ```
- **Respuesta Exitosa** (200): Destino actualizado
- **Errores**:
  - 404: Destino no encontrado
  - 400: No se puede actualizar un destino archivado

#### 5. Archivar Destino
- **Método**: DELETE
- **Ruta**: `/destinations/{destination_id}`
- **Parámetros URL**: destination_id (integer)
- **Respuesta Exitosa** (200):
  ```json
  {
    "message": "Destination {destination_id} archived successfully"
  }
  ```
- **Errores**:
  - 404: Destino no encontrado
  - 400: Destino ya archivado

#### 6. Desarchivar Destino
- **Método**: POST
- **Ruta**: `/destinations/{destination_id}/unarchive`
- **Parámetros URL**: destination_id (integer)
- **Respuesta Exitosa** (200):
  ```json
  {
    "message": "Destination {destination_id} unarchived successfully"
  }
  ```
- **Errores**:
  - 404: Destino no encontrado
  - 400: El destino no está archivado

### Vehículos (Vehicles)

#### 1. Crear Vehículo
- **Método**: POST
- **Ruta**: `/vehicles/`
- **Body**:
  ```json
  {
    "plate": "string",
    "model": "string",
    "capacity": integer,
    "driver": "string",
    "destination_id": integer
  }
  ```
- **Respuesta Exitosa** (200):
  ```json
  {
    "id": int,
    "plate": "string",
    "model": "string",
    "capacity": integer,
    "driver": "string",
    "origin": "string",
    "destination_id": integer
  }
  ```

#### 2. Listar Vehículos
- **Método**: GET
- **Ruta**: `/vehicles/`
- **Descripción**: Obtiene todos los vehículos registrados
- **Respuesta Exitosa** (200):
  ```json
  [
    {
      "id": int,
      "plate": "string",
      "model": "string",
      "capacity": integer,
      "driver": "string",
      "origin": "string",
      "destination_id": integer
    }
  ]
  ```

#### 3. Obtener Vehículo Específico
- **Método**: GET
- **Ruta**: `/vehicles/{vehicle_id}`
- **Parámetros URL**: vehicle_id (integer)
- **Respuesta Exitosa** (200):
  ```json
  {
    "id": int,
    "plate": "string",
    "model": "string",
    "capacity": integer,
    "driver": "string",
    "origin": "string",
    "destination_id": integer
  }
  ```
- **Errores**:
  - 404: Vehículo no encontrado

#### 4. Actualizar Vehículo
- **Método**: PUT
- **Ruta**: `/vehicles/{vehicle_id}`
- **Parámetros URL**: vehicle_id (integer)
- **Body**:
  ```json
  {
    "plate": "string",
    "model": "string",
    "capacity": integer,
    "driver": "string",
    "destination_id": integer
  }
  ```
- **Respuesta Exitosa** (200): Vehículo actualizado
- **Errores**:
  - 404: Vehículo no encontrado

#### 5. Eliminar Vehículo
- **Método**: DELETE
- **Ruta**: `/vehicles/{vehicle_id}`
- **Parámetros URL**: vehicle_id (integer)
- **Respuesta Exitosa** (200):
  ```json
  {
    "message": "Vehicle {vehicle_id} deleted successfully"
  }
  ```
- **Errores**:
  - 404: Vehículo no encontrado

### Citas (Appointments)

#### 1. Crear Cita
- **Método**: POST
- **Ruta**: `/appointments/`
- **Body**:
  ```json
  {
    "vehicle_id": integer,
    "destination_id": integer
  }
  ```
- **Respuesta Exitosa** (200):
  ```json
  {
    "vehicle_id": integer,
    "destination_id": integer,
    "date": "datetime"
  }
  ```

#### 2. Listar Citas
- **Método**: GET
- **Ruta**: `/appointments/`
- **Descripción**: Obtiene todas las citas registradas
- **Respuesta Exitosa** (200):
  ```json
  [
    {
      "vehicle_id": integer,
      "destination_id": integer,
      "date": "datetime"
    }
  ]
  ```

## Códigos de Estado HTTP

- **200**: Operación exitosa
- **201**: Recurso creado exitosamente
- **400**: Error en la solicitud del cliente
- **404**: Recurso no encontrado
- **500**: Error interno del servidor

## Notas Adicionales

1. Todos los endpoints retornan JSON
2. Las fechas se manejan en formato ISO 8601
3. Los IDs son enteros positivos
4. El campo `origin` en vehículos tiene "Bogotá" como valor predeterminado
5. Los destinos archivados no aparecen en el listado general
