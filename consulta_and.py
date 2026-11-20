
from sqlalchemy import and_
from configuracion import SessionLocal
from crear_base_entidades import Clinica, Consultorio, Veterinario

# Abrir la conexion con la base de datos
session = SessionLocal()

try:
    # Buscar veterinarios que cumplan dos condiciones
    veterinarios = (
        session.query(Veterinario)
        .join(Consultorio)
        .join(Clinica)
        .filter(
            and_(
                Clinica.id == 1,
                Veterinario.apellidos == "Mendoza"
            )
        )
        .all()
    )

    print("CONSULTA CON AND")
    print("-----------------------------")

    for veterinario in veterinarios:
        print("Nombre:", veterinario.nombres)
        print("Apellido:", veterinario.apellidos)
        print("Correo:", veterinario.correo)
        print("-----------------------------")

    if not veterinarios:
        print("No se encontraron resultados.")

except Exception as error:
    print("Error al consultar datos:", error)

finally:
    session.close() 
