from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Licitacion(Base):
    __tablename__ = "licitaciones"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    entidad = Column(String)
    monto = Column(Float)
    rubro = Column(String)
    fecha_publicacion = Column(DateTime)
    enlace = Column(String)

