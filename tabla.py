# importando la base de datos y la class Persona
from intro import basededatos, Persona, app


# creando modelo
with app.app_context():
    basededatos.create_all()

    # creando objetos para class Persona
    persona1 = Persona('Pedro', 33)
    persona2 = Persona('Juana', 30)

    # agregando todo
    basededatos.session.add_all([persona1, persona2])

    # agregando 1
    persona3 = Persona('teresa', 34)
    basededatos.session.add(persona3)

    # buscando a todos
    personas = Persona.query.all()
    print('veremos todas las personas')
    print(personas)

    # filtrar datos
    filtro1 = Persona.query.filter_by(nombre='Pedro')
    print('Buscamos a nombre por filtro')
    print(filtro1.all())

    # buscando por id
    seleccionID = Persona.query.get(2)
    print("busqueda por id")
    print(seleccionID)

    # actualizamos un objeto
    persona5 = Persona.query.get(2)
    persona5.edad = 34
    basededatos.session.add(persona5)
    basededatos.session.commit()

    # para borrar de a base
    persona_borrar = Persona.query.get(2)
    basededatos.session.delete(persona_borrar)
    basededatos.session.commit()
    print(f'se acaba de borrar {persona_borrar} ')

    # para obtener todos los datos de las personas
    persona6 = Persona.query.all()
    print(f'Resultado final de todas las persona: {persona6} ')
