import os
from Alta_Baja_Form import FormularioAlta, FormularioBaja
from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

directorio = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'miclavesecreta'
# configuración de base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(directorio, 'mascotas_vistas.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# empezamos con el modelo de nuestra base

basededatos = SQLAlchemy(app)

# recomendación siempre poner despues de la base de datos
Migrate(app, basededatos)


class Mascota(basededatos.Model):
    __tablename__ = 'Mascotas'
    id = basededatos.Column(basededatos.Integer, primary_key=True)
    nombre = basededatos.Column(basededatos.Text)

    # constructor de la class
    def __init__(self, nombre):
        self.nombre = nombre

    # el retorno que nos va entregar
    def __repr__(self):
        texto = f'Mascota: nombre {self.nombre} '
        return texto


# rutas para las vistas

@app.route('/')
def inicio():
    return render_template('vistainicio.html')


@app.route('/listas')
def lista():
    # obtener todo lo que tiene la base de datos de mascota
    mascota = Mascota.query.all()
    return render_template('vistalista.html', mascota=mascota)


@app.route('/alta')
def alta():
    formulario = FormularioAlta()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        mascota = Mascota(nombre)
        basededatos.session.add(mascota)
        basededatos.session.commit()

        return redirect(url_for('lista'))
    return render_template('vista_alta', formulario=formulario)

# nueva ruta


@app.route('/eliminar')
def eliminar():
    formulario = FormularioBaja()
    if formulario.validate_on_submit:
        id = formulario.id.data
        borrar_mascota = Mascota.query.get(id)
        basededatos.session.delete(borrar_mascota)
        basededatos.session.commit()

        return redirect(url_for('lista'))
    return render_template('eliminar_vista', formulario=formulario)


if __name__ == '__main__':
    app.run(debug=True)
