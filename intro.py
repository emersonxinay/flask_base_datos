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


class Persona(basededatos.Model):
    __tablename__ = 'personas'
    id = basededatos.Column(basededatos.Integer, primary_key=True)
    nombre = basededatos.Column(basededatos.Text)
    edad = basededatos.Column(basededatos.Integer)
    pais = basededatos.Column(basededatos.Text)

    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def __repr__(self):
        texto = f'Perons: nombre= {self.nombre} y edad= {self.edad} y pais= {self.pais} '

        return texto
