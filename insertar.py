from intro import basededatos, Persona, app

with app.app_context():
    # agregando dato a un usuario
    persona = Persona.query.get(3)
    persona.pais = 'Chile'
    # agregamos los cambios
    basededatos.session.add(persona)
    # guardamos cambios
    basededatos.session.commit()
