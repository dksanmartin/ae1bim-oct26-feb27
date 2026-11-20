
from datetime import date
from configuracion import SessionLocal
from crear_base_entidades import (
    Clinica, Consultorio, Veterinario, HistoriaClinica
)

# Abrir una sesion con la base de datos
session = SessionLocal()

try:
    # Evitar ingresar los mismos datos dos veces
    if session.query(Clinica).count() > 0:
        print("La base de datos ya contiene clinicas.")
    else:
        # Registrar las clinicas
        clinica1 = Clinica(
            nombre="Veterinaria Patitas Felices",
            direccion="Machala, El Oro",
            veterinario_responsable="Carlos Mendoza"
        )

        clinica2 = Clinica(
            nombre="Centro Veterinario Mundo Animal",
            direccion="Guayaquil, Guayas",
            veterinario_responsable="Maria Torres"
        )

        session.add_all([clinica1, clinica2])
        session.flush()

        # Registrar los consultorios
        consultorio1 = Consultorio(
            nombre="Consultorio 1",
            especialidad="Medicina general",
            clinica_id=clinica1.id
        )

        consultorio2 = Consultorio(
            nombre="Consultorio 2",
            especialidad="Cirugia",
            clinica_id=clinica1.id
        )

        consultorio3 = Consultorio(
            nombre="Consultorio 3",
            especialidad="Dermatologia",
            clinica_id=clinica2.id
        )

        session.add_all([
            consultorio1, consultorio2, consultorio3
        ])
        session.flush()

        # Registrar los veterinarios
        veterinario1 = Veterinario(
            nombres="Carlos",
            apellidos="Mendoza",
            correo="carlos@example.com",
            licencia="VET001",
            consultorio_id=consultorio1.id
        )

        veterinario2 = Veterinario(
            nombres="Ana",
            apellidos="Lopez",
            correo="ana@example.com",
            licencia="VET002",
            consultorio_id=consultorio2.id
        )

        veterinario3 = Veterinario(
            nombres="Maria",
            apellidos="Torres",
            correo="maria@example.com",
            licencia="VET003",
            consultorio_id=consultorio3.id
        )

        session.add_all([
            veterinario1, veterinario2, veterinario3
        ])
        session.flush()

        # Registrar las historias clinicas
        historia1 = HistoriaClinica(
            fecha_atencion=date(2026, 11, 10),
            diagnostico="Infeccion estomacal",
            tratamiento="Medicacion y dieta",
            nombre_mascota="Max",
            veterinario_id=veterinario1.id
        )

        historia2 = HistoriaClinica(
            fecha_atencion=date(2026, 11, 12),
            diagnostico="Herida en una pata",
            tratamiento="Curacion y reposo",
            nombre_mascota="Luna",
            veterinario_id=veterinario2.id
        )

        historia3 = HistoriaClinica(
            fecha_atencion=date(2026, 11, 15),
            diagnostico="Alergia en la piel",
            tratamiento="Tratamiento dermatologico",
            nombre_mascota="Rocky",
            veterinario_id=veterinario3.id
        )

        historia4 = HistoriaClinica(
            fecha_atencion=date(2026, 11, 18),
            diagnostico="Control general",
            tratamiento="Vitaminas y seguimiento",
            nombre_mascota="Toby",
            veterinario_id=veterinario1.id
        )

        session.add_all([
            historia1, historia2, historia3, historia4
        ])

        session.commit()
        print("Datos ingresados correctamente.")
        print("2 clinicas registradas.")
        print("3 consultorios registrados.")
        print("3 veterinarios registrados.")
        print("4 historias clinicas registradas.")

except Exception as error: 
    session.rollback()
    print("Error al ingresar datos:", error)

finally:
    session.close() 
