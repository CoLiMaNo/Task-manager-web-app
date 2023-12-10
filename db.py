from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# El engine permite a SQLAlchemy comunicarse con la base de datos en un dialogo concreto
# https://docs.sqlalchemy.org/en/14/core/engines.html
engine = create_engine('sqlite:///database/tareas.db',
                       connect_args={"check_same_thread": False})# flask por defecto ejecuta los procesos
# sobre un solo hilo pero con esta linea le permitimos hacerlo en mas de un hilo

# Advertencia: crear el engine no conecta inmediatamente con la DB, eso lo hacemos despues

# Creamos la session, lo que permite realizar transacciones (operaciones) dentro de nuestra DB
Session = sessionmaker(bind=engine)
session = Session()

# Ahora vamos al fichero models.py en los modelos (clases) donde queremos
# que se transformen en tablas, le añadiremos esta variable y esto se encargara de mapear
# y vincular cada clase a cada tabla
Base = declarative_base()
