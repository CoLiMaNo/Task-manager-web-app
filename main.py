from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import db # nos da acceso al fichero db.py
from models import Tarea # nos da acceso al fichero models.py

app = Flask(__name__) # es el objeto de nuestro servidor web

@app.route("/") # decorador que debe ir justo encima, en este caso para vincular la accion desde nuestro navegador
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    #for i in todas_las_tareas:
    #    print(i)
    return render_template("index.html", lista_de_tareas = todas_las_tareas) # fichero pagina web

@app.route("/crear_tarea", methods=["POST"]) # con esta cabecera creamos un enpoint (conexion) para vincular la
def crear():                                     # funcion con la web
    contenido_tarea = request.form["contenido_tarea"]
    fecha_vencimiento_str = request.form["fecha_vencimiento"]
    #convierte la cadena de fecha y hora en un objeto datetime
    fecha_vencimiento = datetime.strptime(fecha_vencimiento_str, "%Y-%m-%dT%H:%M")
    tarea = Tarea(contenido=contenido_tarea, hecha=False, fecha_vencimiento=fecha_vencimiento)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home")) # con el url_for le digo a que funcion de mi programa quiero ir home()


@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id))
    tarea.delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
# en esta linea estamos indicando a SQLAlchemy que cree sino existen, las tablas de todos los modelos que encuentre en
# models.py (crea el fichero)
    db.Base.metadata.create_all(db.engine) # crea la base de datos de tarea
    app.run(debug=True) # es la instruccion que pone en marcha el servidor web y va siempre al final