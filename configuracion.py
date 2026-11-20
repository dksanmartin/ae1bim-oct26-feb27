
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Conexion a la base de datos SQLite
DATABASE_URL = "sqlite:///clinicas_veterinarias.db"

# Crear el motor de conexion
engine = create_engine(DATABASE_URL, echo=False)

# Crear las sesiones para trabajar con la base de datos
SessionLocal = sessionmaker(bind=engine)

# Clase base para las entidades
Base = declarative_base()
