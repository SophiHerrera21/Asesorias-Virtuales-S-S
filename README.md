# S&S - Sistema de Asesorías Virtuales

Sistema de gestión de asesorías virtuales para aprendices SENA.

## Características Principales

- Gestión de usuarios (Aprendices, Asesores y Coordinadores)
- Sistema de componentes/materias
- Gestión de grupos y asesorías
- Sistema de pruebas y evaluaciones
- Sistema de PQRS
- Notificaciones por correo electrónico
- Gestión de perfiles y documentos

## Requisitos

- Python 3.8+
- MySQL 8.0+
- Virtualenv (recomendado)

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
- Crear archivo `.env` basado en `.env.example`
- Configurar credenciales de base de datos y correo

5. Realizar migraciones:
```bash
python manage.py migrate
```

6. Crear superusuario:
```bash
python manage.py createsuperuser
```

7. Iniciar el servidor:
```bash
python manage.py runserver
```

## Estructura del Proyecto

- `core/` - Aplicación principal
- `users/` - Gestión de usuarios
- `asesorias/` - Gestión de asesorías
- `grupos/` - Gestión de grupos
- `pruebas/` - Sistema de pruebas
- `pqrs/` - Sistema de PQRS

## Licencia

Este proyecto es propiedad del SENA. 