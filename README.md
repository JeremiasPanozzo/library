# Flask Book API

Una API RESTful creada con Flask que maneja la información de autores y libros. Utiliza autenticación JWT para las rutas que requieren permisos de acceso.

## Descripción

Esta API permite gestionar la información de autores y libros. Las funcionalidades incluyen:

- **Autenticación de usuario**: Registro, login y logout con JWT.
- **Gestión de autores**: Crear, obtener, y eliminar autores.
- **Gestión de libros**: Crear, obtener, y eliminar libros asociados a autores.

## Tecnologías utilizadas

- **Python** 3.x
- **Flask**: Microframework para crear aplicaciones web
- **Flask-JWT-Extended**: Manejo de autenticación JWT
- **Flask-Bcrypt**: Encriptación de contraseñas
- **SQLAlchemy**: ORM para interactuar con la base de datos

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)

## Endpoints disponibles

| Ruta                   | Método | Descripción                        |
| ---------------------- | ------ | ---------------------------------- |
| `/login`               | POST   | Iniciar sesión y obtener token JWT |
| `/register`            | POST   | Registrar un nuevo usuario         |
| `/authors`             | GET    | Obtener todos los autores          |
| `/authors`             | POST   | Crear un nuevo autor               |
| `/authors/<author_id>` | GET    | Obtener un autor por ID            |
| `/authors/<author_id>` | DELETE | Eliminar un autor                  |
| `/books`               | GET    | Obtener todos los libros           |
| `/books`               | POST   | Crear un nuevo libro               |
| `/books/<book_id>`     | GET    | Obtener un libro por ID            |
| `/books/<book_id>`     | DELETE | Eliminar un libro                  |



