# **Admin Site Example**

Este proyecto implementa una aplicación en Django basada en las funcionalidades descritas en el documento, enfocándose en la gestión de modelos mediante el sitio administrativo. Es ideal para administrar datos internos y explorar el uso del sistema de administración de Django.

---

## **Características del Proyecto**

### **1. Sitio Administrativo de Django**
- Proporciona una interfaz rápida y centrada en los modelos para administrar contenido.
- Permite crear, consultar, actualizar y eliminar registros desde el sitio administrativo.

### **2. Modelos Personalizados**
- Incluye un modelo de ejemplo (`Libro`) que permite gestionar información básica de libros como título, autor, fecha de publicación y disponibilidad.
- Los modelos están registrados en el sitio administrativo para una gestión completa.

### **3. Funcionalidades del Sitio Administrativo**
- Vistas personalizadas con campos adicionales, filtros y opciones de búsqueda.
- Facilidad para crear usuarios y grupos con permisos personalizados.
- Personalización de la URL administrativa para mejorar la seguridad.

### **4. Uso de `manage.py`**
- Comandos clave como `makemigrations`, `migrate`, `runserver`, y `createsuperuser` son fundamentales para la gestión del proyecto.

### **5. Mejora de la Seguridad**
- Se incluye un cambio en la URL administrativa para ocultarla de posibles atacantes.
- Se sugiere la integración de autenticación de dos factores (2FA) y otras medidas avanzadas de seguridad.

---

## **Instalación**

### **Requisitos Previos**
- Python 3.8 o superior
- Virtualenv (opcional, pero recomendado)
- Django 4.0 o superior

### **Pasos para la Instalación**

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/admin-site-example.git
   cd admin-site-example
   ```

2. Crear un entorno virtual e instalar dependencias:
   ```bash
   python -m venv env
   source env/bin/activate    # En Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Realizar las migraciones de la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Crear un superusuario para acceder al sitio administrativo:
   ```bash
   python manage.py createsuperuser
   ```

5. Iniciar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

6. Acceder al sitio administrativo en:  
   [http://127.0.0.1:8000/mi-admin-secreto/](http://127.0.0.1:8000/mi-admin-secreto/)

---

## **Uso**

### **Gestión de Modelos**
- Desde el sitio administrativo, puedes crear, editar, eliminar y visualizar registros del modelo `Libro`.

### **Gestión de Usuarios y Grupos**
- Accede a la sección "Autenticación y autorización" para administrar usuarios y permisos.

### **Filtros y Búsquedas**
- Usa los filtros y campos de búsqueda configurados para simplificar la gestión de datos.

---

## **Seguridad**

### **Recomendaciones Adicionales**
- Habilitar HTTPS en producción para proteger las credenciales.
- Configurar autenticación de dos factores (2FA) usando librerías como `django-two-factor-auth`.
- Implementar un honeypot en `/admin/` para capturar intentos de acceso no autorizado.

---

## **Tecnologías Usadas**

- **Django**: Framework web para Python.
- **SQLite**: Base de datos predeterminada para desarrollo rápido.

---

## **Contribuciones**

Las contribuciones son bienvenidas. Si deseas colaborar, por favor:
1. Crea un fork del repositorio.
2. Crea una rama nueva para tus cambios.
3. Envía un pull request detallando tus modificaciones.

---

## **Licencia**

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---
