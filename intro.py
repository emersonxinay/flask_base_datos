import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
directorio = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# configuración de base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(directorio, 'datos.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# empezamos con el modelo de nuestra base

basededatos = SQLAlchemy(app)


class Persona(basededatos.Model):
    __tablename__ = 'personas'
    id = basededatos.Column(basededatos.Integer, primary_key=True)
    nombre = basededatos.Column(basededatos.Text)
    edad = basededatos.Column(basededatos.Integer)

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        texto = f'Perons: nombre= {self.nombre} y edad= {self.edad} '

        return texto
