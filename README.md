# Children Management API (Árbol ABB)

API REST para gestionar información de niños utilizando una estructura de datos de **Árbol Binario de Búsqueda (ABB)**.

## 📋 Descripción

Esta API permite realizar operaciones CRUD (Create, Read, Update, Delete) sobre registros de niños. Los datos se almacenan internamente en un Árbol Binario de Búsqueda ordenado por ID, proporcionando búsquedas eficientes.

## 🚀 Características

- ✅ Crear nuevos registros de niños
- ✅ Listar todos los niños (en orden)
- ✅ Buscar niño por ID
- ✅ Actualizar información de niños
- ✅ Eliminar registros
- ✅ Estructura de datos: Árbol Binario de Búsqueda (BST)
- ✅ API RESTful con FastAPI
- ✅ Documentación interactiva con Swagger

## 📦 Requisitos

- Python 3.8+
- pip (gestor de paquetes)

## 🔧 Instalación

1. **Clonar el repositorio**:
```bash
git clone https://github.com/josscard/Api_abb_children.git
cd Api_abb_children
```

2. **Crear entorno virtual** (opcional pero recomendado):
```bash
python -m venv .venv
```

3. **Activar entorno virtual**:
   - **Windows**:
   ```bash
   .venv\Scripts\activate
   ```
   - **macOS/Linux**:
   ```bash
   source .venv/bin/activate
   ```

4. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

## ▶️ Ejecutar la aplicación

```bash
uvicorn main:app --reload
```

La API estará disponible en: `http://127.0.0.1:8000`

### Documentación interactiva:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 📚 Endpoints

### Base URL
```
http://127.0.0.1:8000/api
```

### 1. Crear un niño
**POST** `/children/`

**Headers**:
```
Content-Type: application/json
```

**Body** (raw JSON):
```json
{
  "name": "Juan Pérez",
  "age": 10,
  "grade": "5th"
}
```

**Respuesta** (201 Created):
```json
{
  "id": 1,
  "name": "Juan Pérez",
  "age": 10,
  "grade": "5th"
}
```

---

### 2. Listar todos los niños
**GET** `/children/`

**Respuesta** (200 OK):
```json
[
  {
    "id": 1,
    "name": "Juan Pérez",
    "age": 10,
    "grade": "5th"
  },
  {
    "id": 2,
    "name": "María García",
    "age": 9,
    "grade": "4th"
  }
]
```

---

### 3. Obtener niño por ID
**GET** `/children/{child_id}`

**Ejemplo**:
```
GET /children/1
```

**Respuesta** (200 OK):
```json
{
  "id": 1,
  "name": "Juan Pérez",
  "age": 10,
  "grade": "5th"
}
```

**Respuesta si no existe** (404 Not Found):
```json
{
  "detail": "Child with ID 1 not found"
}
```

---

### 4. Actualizar niño
**PUT** `/children/{child_id}`

**Headers**:
```
Content-Type: application/json
```

**Body** (raw JSON, todos los campos son opcionales):
```json
{
  "name": "Juan Carlos Pérez",
  "age": 11,
  "grade": "6th"
}
```

O actualizar solo algunos campos:
```json
{
  "name": "Juan Carlos"
}
```

**Respuesta** (200 OK):
```json
{
  "id": 1,
  "name": "Juan Carlos Pérez",
  "age": 11,
  "grade": "6th"
}
```

---

### 5. Eliminar niño
**DELETE** `/children/{child_id}`

**Ejemplo**:
```
DELETE /children/1
```

**Respuesta** (204 No Content)

---

## 🧪 Pruebas con Postman

### Crear niño
```
POST http://127.0.0.1:8000/api/children/
Content-Type: application/json

{
  "name": "Carlos López",
  "age": 12,
  "grade": "7th"
}
```

### Listar niños
```
GET http://127.0.0.1:8000/api/children/
```

### Obtener niño específico
```
GET http://127.0.0.1:8000/api/children/1
```

### Actualizar niño
```
PUT http://127.0.0.1:8000/api/children/1
Content-Type: application/json

{
  "age": 13,
  "grade": "8th"
}
```

### Eliminar niño
```
DELETE http://127.0.0.1:8000/api/children/1
```

## 📁 Estructura del Proyecto

```
ArbolAbbApi/
├── main.py                          # Punto de entrada de FastAPI
├── requirements.txt                 # Dependencias del proyecto
├── README.md                        # Este archivo
│
├── app/
│   ├── __init__.py
│   │
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── child_controller.py      # Lógica de negocio (CRUD + BST)
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── child_model.py           # Modelos Pydantic
│   │   └── tree_node.py             # Nodo del Árbol Binario
│   │
│   └── views/
│       ├── __init__.py
│       └── child_routes.py          # Endpoints de la API
│
└── tests/
    └── test_main.http               # Pruebas HTTP
```

## 🏗️ Arquitectura

### Patrón MVC
- **Models** (`app/models/`): Estructuras de datos (ChildModel, TreeNode)
- **Views** (`app/views/`): Endpoints REST
- **Controllers** (`app/controllers/`): Lógica de negocio y operaciones BST

### Árbol Binario de Búsqueda (BST)
- Los niños se almacenan en un BST ordenado por ID
- Operaciones de búsqueda, inserción y eliminación en O(log n) en promedio
- Recorrido in-order para listar niños ordenados

## 📝 Dependencias

```
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
python-dotenv==1.0.0
```

## 👨‍💻 Autor

**Estudiante de Ingeniería - 4to Semestre**

## 📄 Licencia

Este proyecto es de uso educativo.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## ❓ Preguntas o Problemas

Si tienes preguntas o encuentras problemas, abre un issue en el repositorio.

---

**Última actualización**: 2025-10-23
