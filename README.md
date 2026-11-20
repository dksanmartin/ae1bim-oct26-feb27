# Actividad B1 - Sistema de Clínicas Veterinarias

## Descripción del proyecto

En esta actividad se desarrolló una base de datos para administrar la información de una red de clínicas veterinarias. El sistema permite registrar clínicas, consultorios, veterinarios e historias clínicas de las mascotas.

Para realizar el proyecto se utilizó Python, SQLAlchemy y SQLite, trabajando desde Visual Studio Code.

## Archivos del proyecto

**configuracion.py:** Establece la conexión con la base de datos SQLite y permite crear las sesiones necesarias para trabajar con la información.

**crear_base_entidades.py:** Define las entidades del sistema, sus atributos y las relaciones entre las tablas.

**poblar_base.py:** Permite ingresar información de prueba sobre las clínicas, consultorios, veterinarios e historias clínicas.

**consulta_all.py:** Consulta información de las clínicas y muestra la cantidad de historias clínicas asociadas.

**consulta_filter.py:** Filtra los veterinarios que pertenecen a una clínica determinada.

**consulta_order_by.py:** Ordena los veterinarios alfabéticamente por sus apellidos.

**consulta_and.py:** Busca veterinarios que cumplan dos condiciones al mismo tiempo.

**consulta_or.py:** Busca veterinarios que cumplan al menos una de las condiciones establecidas.

**clinicas_veterinarias.db:** Archivo donde se almacena la base de datos del proyecto.

## Ejecución del proyecto

Para ejecutar los archivos se utiliza la terminal de Visual Studio Code, desde la carpeta del proyecto.

Primero se crea la base de datos:

`py crear_base_entidades.py`

Después se ingresan los datos:

`py poblar_base.py`

Finalmente, se pueden realizar las consultas:

`py consulta_all.py`

`py consulta_filter.py`

`py consulta_order_by.py`

`py consulta_and.py`

`py consulta_or.py`

## Conclusión

Mediante esta actividad se aprendió a crear una base de datos utilizando Python y SQLAlchemy. También se comprendió cómo relacionar las diferentes entidades y realizar consultas para obtener información específica. Esto permitió poner en práctica el manejo de datos y las operaciones de búsqueda, filtrado y ordenamiento.