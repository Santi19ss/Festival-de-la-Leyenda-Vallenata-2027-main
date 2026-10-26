Estado del Proyecto - Eje 2 (Festival Vallenato 2027)

📌 Lo que ya está terminado (Backend & Infraestructura)

La base lógica y estructural requerida por la rúbrica ha sido completada:

Configuración Django: Arquitectura MVT, apps separadas (votaciones, usuarios).

Modelos de Datos: Creadas las entidades Edicion, Categoria, Votacion, Opcion ajustadas al feedback del cliente (permitiendo múltiples fases por categoría).

Autenticación Base: Sistema de Login, Logout y Registro completamente funcional y seguro.

Django Admin: Habilitado para gestionar los datos sin modificar código.

Vistas Públicas: Conexión de la base de datos a las plantillas HTML (listado de ediciones y categorías).

🛠️ Lo que hace falta (Tareas de Equipo)

Para alcanzar los 20/20 puntos de esta entrega, el equipo debe dividirse las siguientes tareas:

1. Diseño e Interfaz Pública (CSS) - Prioridad Alta

Responsables: Equipo de Frontend.

Tarea: Los HTML actuales están "crudos". Necesitamos aplicar estilos CSS para que se vean presentables para el cliente, utilizando los colores y la identidad cultural del Festival.

Nota: No tiene que ser el diseño final y perfecto, pero debe mostrar una propuesta visual coherente.

2. Migración a MySQL - Obligatorio para la Nota Técnica

Responsable: Desarrollador Backend / Infraestructura.

Tarea: Aunque actualmente usamos SQLite para velocidad, la rúbrica exige que los datos persistan en MySQL. Antes de la entrega final, debemos cambiar el diccionario DATABASES en settings.py, instalar el driver correspondiente y correr las migraciones en el servidor de MySQL.

3. Documento PDF Final - Entregable del Cliente

Responsables: Todos (Redacción colaborativa).

Contenido a redactar:

Introducción y objetivos (ya se tiene un borrador).

Desarrollo Técnico (Explicar cómo funciona nuestro patrón MVT y la conexión a la base de datos).

Código relevante (Pegar el código de nuestros models.py y views.py).

Capturas de pantalla comentadas: Debemos tomar fotos del Django Admin, las interfaces ya estilizadas, y explicar qué demuestra cada captura.

4. Video Demostrativo - Requisito de Evaluación

Responsables: Todos los integrantes del grupo (obligatorio).

Tarea: Grabar un video (puede ser por Zoom, Teams, Meet) donde los cuatro hablemos, mostremos el repositorio, cómo se ejecuta el proyecto, cómo funciona el inicio de sesión y cómo se ven los datos en la pantalla pública.