import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

directorio = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


# configuración de base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(directorio, 'datos.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# empezamos con el modelo de nuestra base

basededatos = SQLAlchemy(app)

# recomendación siempre poner despues de la base de datos
Migrate(app, basededatos)


class Mascota(basededatos.Model):
    __tablename__ = 'Mascotas'
    id = basededatos.Column(basededatos.Integer, primary_key=True)
    nombre = basededatos.Column(basededatos.Text)
    juguetes = basededatos.relationship(
        'Juguete', backref='mascota', lazy='dynamic')
    Propietario = basededatos.relationship(
        'Propietario', backref='mascota', uselist=False)

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        texto = f'Mascota: nombre {self.nombre}'
        return texto

    def mostrar_juguetes(self):
        for i in self.juguetes:
            print(i.nombre)


class Juguete(basededatos.Model):
    __tablename__ = 'Juguetes'
    id = basededatos.Column(basededatos.Integer, primary_key=True)
    nombre = basededatos.Column(basededatos.Text)
    mascota_id = basededatos.Column(
        basededatos.Integer, basededatos.ForeignKey('Mascotas.id'))

    # constructor

    def __init__(self, nombre, mascota_id):
        self.nombre = nombre
        self.mascota_id = mascota_id


class Propietario(basededatos.Model):
    __tablename__ = 'Propietarios'
    id = basededatos.Column(basededatos.Integer, primary_key=True)
    nombre = basededatos.Column(basededatos.Text)
    mascota_id = basededatos.Column(
        basededatos.Integer, basededatos.ForeignKey('Mascotas.id'))

    # constructor
    def __init__(self, nombre, mascota_id):
        self.nombre = nombre
        self.mascota_id = mascota_id
