
# 🌐 Web Django Empresarial

**Web Django Empresarial** es una aplicación web desarrollada como parte de una formación en backend con Django. Este proyecto simula una página empresarial moderna, incorporando funcionalidades como un blog, servicios, formulario de contacto y más, todo estructurado de manera modular utilizando las capacidades del framework Django.

---

## 🚀 Características Principales

- 🔐 **Gestión de Usuarios y Autenticación**: Registro, inicio de sesión y gestión de perfiles de usuarios.
- 📝 **Blog Integrado**: Publicación y edición de artículos con editor de texto enriquecido (CKEditor).
- 💼 **Sección de Servicios**: Presentación de los servicios ofrecidos por la empresa.
- 📬 **Formulario de Contacto**: Permite a los visitantes enviar mensajes directamente desde la web.
- 🎨 **Diseño Modular**: Estructura basada en aplicaciones Django para facilitar la escalabilidad y mantenimiento.
- 📁 **Gestión de Archivos Multimedia**: Soporte para la carga y visualización de imágenes y otros archivos.

---

## 🛠️ Tecnologías Utilizadas

- **Backend**: [Django](https://www.djangoproject.com/) (Python)
- **Frontend**: HTML5, CSS3, Bootstrap
- **Editor de Texto**: [CKEditor](https://ckeditor.com/)
- **Base de Datos**: SQLite (configurable a otras bases de datos como PostgreSQL o MySQL)
- **Control de Versiones**: Git

---

## 📂 Estructura del Proyecto

```
web_django_empresarial/
├── blog/
├── contact/
├── core/
├── media/
├── pages/
├── services/
├── social/
├── static/
├── templates/
├── web_empresarial/
├── .env
├── .gitignore
├── LICENSE
├── manage.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Instalación y Ejecución

### 1. Clonar el Repositorio

```bash
git clone https://github.com/guizafj/web_django_empresarial.git
cd web_django_empresarial
```

### 2. Crear y Activar un Entorno Virtual

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

### 3. Instalar las Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto y definir las variables necesarias, por ejemplo:

```env
SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Aplicar Migraciones y Crear Superusuario

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

Accede a la aplicación en [http://localhost:8000](http://localhost:8000)

---

## 📸 Capturas de Pantalla

> *Nota: Aquí puedes incluir imágenes o gifs que muestren la interfaz de usuario, como la página de inicio, el blog, el formulario de contacto, etc.*

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request describiendo tus cambios.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 📬 Contacto

Para consultas o sugerencias:

- **Autor**: [guizafj](https://github.com/guizafj)
- **Correo**: contacto@dguiza.dev