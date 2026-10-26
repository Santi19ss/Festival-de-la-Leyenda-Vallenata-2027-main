Plataforma de Votaciones - Festival de la Leyenda Vallenata 2027

Este repositorio contiene la estructura backend (Django) y la lógica inicial para el sistema de votaciones de la 60.ª edición del Festival Vallenato.

Requisitos Previos

Python 3.11 instalado en tu sistema.

Git.

Instrucciones para levantar el entorno local

Sigue estos pasos cuidadosamente para ejecutar el proyecto en tu máquina y comenzar con la integración de los estilos (CSS):

1. Clonar el repositorio

Abre tu terminal y clona el proyecto en tu carpeta de preferencia:

git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DE_LA_CARPETA>


2. Crear y activar el entorno virtual (venv)

Es indispensable usar un entorno virtual para no causar conflictos con las versiones de Python de tu sistema.

# Crear el entorno
python -m venv venv

# Activar el entorno (Windows)
venv\Scripts\activate

# Activar el entorno (Mac/Linux)
source venv/bin/activate


3. Instalar las dependencias

Asegúrate de que tu entorno virtual esté activado (deberías ver (venv) al inicio de tu terminal) e instala Django:

pip install django


(Nota: Más adelante instalaremos mysqlclient o pymysql para la base de datos de producción).

4. Ejecutar las migraciones

Actualmente estamos utilizando SQLite para agilizar el desarrollo local. Para construir tu base de datos local y sus tablas, ejecuta:

python manage.py migrate


5. Crear tu usuario administrador (Opcional, pero recomendado)

Para poder entrar al panel de administración y crear datos de prueba, ejecuta:

python manage.py createsuperuser


(Sigue las instrucciones en la terminal para definir tu usuario y contraseña).

6. Ejecutar el servidor

Finalmente, levanta el servidor de desarrollo local:

python manage.py runserver


Ingresa a http://127.0.0.1:8000/ en tu navegador. Deberías ver las pantallas iniciales del proyecto.

🎨 Notas para el Equipo de Frontend / Diseño

La lógica de vistas (V) y los modelos (M) ya están terminados. Su trabajo se concentrará en las plantillas (T).

Los archivos HTML se encuentran en las rutas:

votaciones/templates/votaciones/ (index.html, categorias.html)

usuarios/templates/registration/ (login.html)

usuarios/templates/usuarios/ (registro.html)

Para añadir CSS, recuerden crear la carpeta static/ dentro de la app correspondiente o en la raíz del proyecto, configurándola correctamente en el archivo base, y utilizar la etiqueta {% load static %} en los HTML. ¡Mucho éxito dándole vida e identidad cultural a la plataforma!