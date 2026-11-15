HelpDesk, Sistema de Gestion de Incidencias Tecnicas

Practica de evaluacion MF0227_3 (UF2404, UF2405, UF2406).

Requisitos
Python 3.10 o superior y Git.

Instalacion y despliegue local
1. Clonar o descomprimir el proyecto y entrar en la carpeta.
2. Crear el entorno virtual
   python -m venv venv
3. Activarlo
   Linux o macOS: source venv/bin/activate
   Windows: venv\Scripts\activate
4. Instalar dependencias
   pip install -r requirements.txt
5. Aplicar migraciones
   python manage.py migrate
6. Crear un superusuario para el panel de administracion
   python manage.py createsuperuser
7. Levantar el servidor
   python manage.py runserver
8. Abrir en el navegador
   Listado de incidencias: http://127.0.0.1:8000/
   Nueva incidencia: http://127.0.0.1:8000/nueva/
   Administracion: http://127.0.0.1:8000/admin/

Ejecutar el modulo POO
python core_modelos.py

Ejecutar los tests de Django
python manage.py test

Estructura del proyecto
core_modelos.py          Bloque 1, clases POO independientes
helpdesk_project/        Configuracion del proyecto Django
incidencias/             App con models, admin, views, forms, urls y tests
templates/               base.html y plantillas de lista y formulario
requirements.txt         Dependencias
pruebas.txt              Plan de pruebas ejecutadas

Arquitectura y relacion entre las UF
UF2404 (POO). core_modelos.py define TicketTecnico con atributos protegidos, validacion de transiciones de estado y excepciones propias. TicketHardware y TicketSoftware heredan y sobrescriben calcular_sla (polimorfismo).

UF2405 (Django y base de datos). La app incidencias traslada ese dominio a la web. Los modelos Tecnico e Incidencia usan el ORM con una ForeignKey y choices de estado y prioridad. El panel de administracion, el ListView, el CreateView con ModelForm y las plantillas que heredan de base.html forman la capa web.

UF2406 (ciclo de vida). El trabajo se organiza con Git en las ramas main y desarrollo, con commits por etapa. El README y pruebas.txt documentan la instalacion y la validacion.