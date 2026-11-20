
from configuracion import SessionLocal
from crear_base_entidades import Clinica, Consultorio, Veterinario

# Abrir la conexion
session = SessionLocal()

try:
    # Buscar los veterinarios de la clinica con ID 1
    veterinarios = (
        session.query(Veterinario)
        .join(Consultorio)
        .join(Clinica)
        .filter(Clinica.id == 1)
        .all()
    )

    print("VETERINARIOS DE LA CLINICA 1")
    print("--------------------------------")

    for veterinario in veterinarios:
        print("Nombre:", veterinario.nombres)
        print("Apellido:", veterinario.apellidos)
        print("Correo:", veterinario.correo)
        print("--------------------------------")

finally:
    session.close() 
 