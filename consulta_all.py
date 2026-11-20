
from configuracion import SessionLocal
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

# Abrir la conexion con la base de datos
session = SessionLocal()

try:
    # Obtener todas las clinicas usando all()
    clinicas = session.query(Clinica).all()

    print("CLINICAS VETERINARIAS E HISTORIAS CLINICAS")
    print("------------------------------------------")

    for clinica in clinicas:
        # Contar las historias clinicas de cada clinica
        total_historias = (
            session.query(HistoriaClinica)
            .join(Veterinario, HistoriaClinica.veterinario_id == Veterinario.id)
            .join(Consultorio, Veterinario.consultorio_id == Consultorio.id)
            .filter(Consultorio.clinica_id == clinica.id)
            .count()
        )

        print("Clinica:", clinica.nombre)
        print("Direccion:", clinica.direccion)
        print("Numero de historias clinicas:", total_historias)
        print("------------------------------------------")

finally:
    session.close() 
 