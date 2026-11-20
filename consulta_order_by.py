
from configuracion import SessionLocal
from crear_base_entidades import Veterinario

# Abrir la conexion con la base de datos
session = SessionLocal()

try:
    # Consultar veterinarios ordenados por apellido
    veterinarios = (
        session.query(Veterinario)
        .order_by(Veterinario.apellidos.asc())
        .all()
    )

    print("VETERINARIOS ORDENADOS POR APELLIDO")
    print("-----------------------------------")

    for veterinario in veterinarios:
        print("Nombre:", veterinario.nombres)
        print("Apellido:", veterinario.apellidos)
        print("Correo:", veterinario.correo)
        print("-----------------------------------")

except Exception as error:
    print("Error al consultar datos:", error)

finally:
    session.close() 
