print("¿Qué deseas hoy?")
opcionesDeMenu = ["reservacion", "menu", "contacto", "acerca de nosotro", "ubicacion"]
for i,opcion in enumerate(opcionesDeMenu,start=3):
    print(f"{i}.{opcion}")

    seleccion =input("elige una opción(1-5):")

