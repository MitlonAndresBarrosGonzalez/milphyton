print("¿Qué deseas hoy?")
opcionesDeMenu = ["reservacion", "menu", "contacto", "acerca de nosotro", "ubicacion","salir"]
for i,opcion in enumerate(opcionesDeMenu,start=1):
    print(f"{i}.{opcion}") 

seleccion =input("elige una opción(1-6):")

def pedir_numero_personas():
    while True:
        try:
            personas = int(input("Número de personas: "))
            return personas
        except ValueError:
            print("Eso no es un número válido. Por favor ingresa solo dígitos (ej: 4).")


def pedir_codigo_reserva():
    while True:
        try:
            codigo = int(input("Ingresa tu código de reserva (solo números): "))
            return codigo
        except ValueError:
            print("Código inválido. Debe contener solo números, sin letras ni símbolos.")


print("¿Qué deseas hoy?")
opcionesDeMenu = ["reservacion", "menu", "contacto", "acerca de nosotro", "ubicacion", "salir"]
for i, opcion in enumerate(opcionesDeMenu, start=1):
    print(f"{i}.{opcion}")

seleccion = input("elige una opción(1-6):")

if seleccion == "1":
    print("--- Reservación en loquendocasa ---")
    print("1. Hacer una reservación")
    print("2. Cancelar una reservación")
    tipo = input("¿Qué deseas hacer? ")

    if tipo == "1":
        nombre = input("nombre completo:")
        fecha = input("fecha de la reservacion (dd/mm/aaaa):")
        hora = input("hora de la reservacion (hh:mm): ")
        personas = pedir_numero_personas()
        telefono = input("numero de telefono:")
        print(f"\n¡Gracias {nombre} !Tu mesa para {personas} personas quedo reservada para el dia {fecha} fecha a las horas {hora}.")

    elif tipo == "2":
        codigo = pedir_codigo_reserva()
        print(f"\nTu reservación con código {codigo} ha sido cancelada exitosamente.")
        print("Esperamos verte en otra ocasión en Loquendocasa.")

    else:
        print("Opción no válida, por favor elige 1 o 2.")

elif seleccion == "2":
    platos = {
        "Ternera a la llanera": 32000,
        "Mamona (carne a la vara)": 35000,
        "Costilla de res a la llanera": 30000,
        "Chuzo de carne de res": 20000,
        "Chuzo mixto (res, cerdo y pollo)": 24000,
        "Cachama frita": 28000,
        "Cachama asada a la llanera": 29000,
        "Carne oreada llanera": 27000,
        "Costillas de cerdo a la brasa": 26000,
        "Pollo a la llanera": 22000,
        "Morcilla llanera": 10000,
        "Chorizo llanero": 9000,
        "Yuca cocida": 6000,
        "Arepa llanera": 5000,
        "Papas criollas con suero costeño": 8000
    }

    for plato, precio in platos.items():
        print(f"{plato}...........${precio:,}")

elif seleccion == "3":
    print("Nombre:Milton andres barros gonzalez")
    print("Edad:18")
    print("Correo:mitonandresbarrosgonzalez@gmail.com")
    print("Telefono:3237877263")
    print("-------------------------------------------------")
    print("Nombre:Sally gonzalez de la rans")
    print("Edad:41")
    print("Correo:btamil0907@gmail.com")
    print("Telefono:3014199997")
    print("-------------------------------------------------")
    print("Nombre:william artigas")
    print("Edad:37")
    print("Correo:williamartigas@gmail.com")

elif seleccion == "4":
    print("--- Acerca de nosotros ---")
    print("Somos tres costeños que llegamos a Medellín hace algunos años y,")
    print("aunque cambiamos de ciudad, nunca quisimos dejar atrás el sabor")
    print("de nuestra tierra. Así nació Loquendocasa: un espacio donde la")
    print("cocina de la costa Caribe colombiana se prepara con la misma")
    print("dedicación de siempre, lejos de casa pero fiel a sus raíces.")
    print("")
    print("Cada plato que sale de nuestra cocina lleva años de tradición")
    print("familiar detrás. Para nosotros, cocinar así es una forma de")
    print("mantener viva nuestra cultura, y de compartirla con quienes nos visitan.")
    print("")
    print("En Loquendocasa buscamos que cada visita se sienta completa:")
    print("buena comida, buen ambiente, y un pedazo de la costa en medio")
    print("de la montaña.")

elif seleccion == "5":
    print("--- Ubicación ---")
    print("")
    print("Nos encontramos en el Poblado, Medellín, Antioquia.")
    print("Dirección: Calle 10 # 40-15")
    print("Horario: martes a domingo, de 12:00 m. a 10:00 p.m.")
    print("Teléfono: 300-123-4567")

elif seleccion == "6":
    print("¡Gracias por visitar loquendocasa! Hasta pronto.")

else:
    print("Opcion no encontrada, porfavor elegir entre nuestras opciones")