from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DCamara(Base):
    __tablename__ = "d_camara"
    __table_args__ = {"schema": "usr_p360"}  

    d_camara_id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    latitud = Column(Float, nullable=False)
    longitud = Column(Float, nullable=False)
    fecha_alta = Column(DateTime, nullable=False)
    fecha_modificacion = Column(DateTime, nullable=False)

__all__ = ["DCamara"]
