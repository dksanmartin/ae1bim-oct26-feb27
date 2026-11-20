
from sqlalchemy import or_
from configuracion import SessionLocal
from crear_base_entidades import Veterinario

# Abrir la conexion con la base de datos
session = SessionLocal()

try:
    # Buscar veterinarios con uno de los dos apellidos
    veterinarios = (
        session.query(Veterinario)
        .filter(
            or_(
                Veterinario.apellidos == "Lopez",
                Veterinario.apellidos == "Mendoza"
            )
        )
        .all()
    )

    print("CONSULTA CON OR")
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
 