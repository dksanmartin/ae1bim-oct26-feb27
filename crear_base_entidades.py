
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from configuracion import Base, engine


# Entidad Clinica
class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(100), nullable=False)

    consultorios = relationship("Consultorio", back_populates="clinica")


# Entidad Consultorio
class Consultorio(Base):
    __tablename__ = "consultorios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)
    clinica_id = Column(Integer, ForeignKey("clinicas.id"), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship("Veterinario", back_populates="consultorio")


# Entidad Veterinario
class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False)
    licencia = Column(String(50), nullable=False)
    consultorio_id = Column(
        Integer, ForeignKey("consultorios.id"), nullable=False
    )

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias = relationship("HistoriaClinica", back_populates="veterinario")


# Entidad Historia Clinica
class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico = Column(String(200), nullable=False)
    tratamiento = Column(String(200), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)
    veterinario_id = Column(
        Integer, ForeignKey("veterinarios.id"), nullable=False
    )

    veterinario = relationship("Veterinario", back_populates="historias")


# Crear las tablas en SQLite
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Base de datos y tablas creadas correctamente.")
 