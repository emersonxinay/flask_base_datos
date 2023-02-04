from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class FormularioAlta(FlaskForm):
    nombre = StringField('Nombre de la mascota: ')
    boton = SubmitField('Agregar')


class FormularioBaja(FlaskForm):
    id = IntegerField('Identificador de mascota: ')
    boton = SubmitField('eliminar')
