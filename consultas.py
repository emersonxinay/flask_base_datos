from Mascotas import basededatos, Mascota, Juguete, Propietario, app

with app.app_context():
    # creamos los objetos

    mascota1 = Mascota('Felipe')
    mascota2 = Mascota('Katy')

    basededatos.session.add_all([mascota1, mascota2])
    basededatos.session.commit()

    # buscamos todas las mascotas
    mascotas = Mascota.query.all()
    print(mascotas)

    # filtrar por un nombre, si tiene dato o si hay mas.
    mascota1 = Mascota.query.filter_by(nombre='Felipe').first()

    # ahora a propietario
    propietario1 = Propietario('pedro', mascota1.id)
    basededatos.session.add(propietario1)
    basededatos.session.commit()

    # ahora a juguetes

    juguete1 = Juguete('Pelota de futbol', mascota1.id)
    juguete2 = Juguete('oso de peluche', mascota1.id)
    basededatos.session.add_all([juguete1, juguete2])
    basededatos.session.commit()

    # filtrar mascotas
    mascota = Mascota.query.filter_by(nombre='Katy').first()
    print(mascota)
    mascota.mostrar_juguetes()
