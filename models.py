from sqlalchemy import Column, Integer, Boolean, String, DateTime
from datetime import datetime
import db # conecta el fichero db.py con models.py


class Tarea(db.Base):
    __tablename__ = "tarea"
    __table_args__ = {'sqlite_autoincrement': True} # Autoincrementa la PK de la tabla
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False) # esto hace que el campo contenido NO pueda estar vacio
    hecha = Column(Boolean)
    fecha_vencimiento = Column(DateTime)

    def __init__(self, contenido, hecha, fecha_vencimiento):
        self.contenido = contenido
        self.hecha = hecha
        self.fecha_vencimiento = fecha_vencimiento
        print(("(init-class) Tarea creada con exito"))

    def __str__(self):
        return 'Tarea {}: {} ({})'.format(self.id, self.contenido, self.hecha)



