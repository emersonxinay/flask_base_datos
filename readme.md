# Primeros pasos en Flask 

### Como requisito, tener estas herramientas: 
<li>Editor de Código: <a href="https://code.visualstudio.com/">VsCode </a> </li>
<li>Lenguaje de Programación: <a href="https://www.python.org/downloads/">python </a> </li> 

<li>Framework Flask: <a href="https://www.manualweb.net/flask/instalar-flask/"> Flask </a> </li>
<li>Documentación Flask: 
<a href="https://flask-es.readthedocs.io/quickstart/#:~:text=Para%20ejecutar%20la%20aplicaci%C3%B3n%2C%20utiliza,aplicaci%C3%B3n%20con%20la%20opci%C3%B3n%20%2Dapp%20.&text=Como%20atajo%2C%20si%20el%20archivo,tienes%20que%20usar%20%2D%2Dapp%20.">documentación de  flask </a> 
</li>
<li>Para hacer peticiones de API: <a href="https://insomnia.rest/download">insomia </a> </li> 

## crear un entorno de trabajo para flask 

### iniciamos instalando virtualenv 
```bash
pip install virtualenv
```
### creamos una carpeta para nuestro proyecto
```bash 
mkdir miproyecto
```
```bash
cd miproyecto
```
### ahora creamos el entorno virtual del proyecto - suele utilizar venv
```bash
virtualenv mientornovirtual
```
#### suelen usar cambio de mientornovirtual por venv 

### Recuerda siempre activar el entorno virtual para trabajar con flask
```bash 
source mientornovirtual/bin/activate
```
### si deseas desactivar 
```bash 
deactivate
```
## instalamos flask 
```bash
pip install Flask 
```
## creamos un archivo nuevo index.py y agregamos este codigo base: 

```py
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### para correr el programa 
```bash 
flask run
```
o 
```bash
python3 index.py
```
### pero para que no estes apagando y volver a encender el servidor vamos hacer lo siguiente.

```bash 
$env:FLASK_ENV = "development"
```
o 
```bash 
export FLASK_ENV=development
```

# instalar Sqlchema
```bash
pip install flask_sqlalchemy
```

### iniciando crear base de datos desde el archivo intro.py 
```py
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
```

## Haciendo consultas desde el archivo de tabla.py 
```py
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
```

### ejecutar el archivo tabla.py
```bash
python3 tabla.py 
```
### y automaticamente se va crear en el raiz de archivos el archivo datos.sqlite


# haciendo migración al actualizar modelo
## primero instalamos 
```bash
pip install flask_migrate
```

## luego desde el archivo lo importamos 
```py
from flask_migrate import Migrate

# despues de la base de datos 
Migrate(app, basededatos)
```

### y para ejecutarlo ahora solo tienes que ejecutrar desde consola lo siguiente 
### desde mac 
```bash
export FLASK_APP=intro.py
```
### desde windows
```bash
set FLASK_APP = tuarchivo.py
```
## y  hacemos la inicializacion de la migración
```bash
flask db init
```
### y automaticamente aparece una carpeta de migrations 
## y ahora hacemos la migracion 
```bash 
flask db migrate -m "incluimos la columna de pais"
```

## y finalmente para mostrarnos la actualización de la base de datos con la migración
```bash
flask db upgrade
```









