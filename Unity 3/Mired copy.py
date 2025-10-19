# Bienvenida
print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

# Datos del usuario
nombre = input("Para empezar, dime cómo te llamas: ")
print("\nHola", nombre, ", bienvenido a Mi Red\n")

# Edad
agno = int(input("¿En qué año naciste?: "))
edad = 2017 - agno - 1

# Estatura
estatura = float(input("¿Cuánto mides en metros? "))
estatura_m = int(estatura)
estatura_cm = int((estatura - estatura_m) * 100)

# Amigos
num_amigos = int(input("¿Cuántos amigos tienes? "))

# Perfil
print("\nMuy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red\n")

# Menú interactivo
continuar = True

while continuar:
    print("\n¿Qué deseas hacer?")
    print("  1. Escribir un mensaje")
    print("  2. Modificar tu nombre")
    print("  0. Salir")

    opcion = input("Ingresa una opción: ")

    if opcion == "1":
        mensaje = input("¿Qué piensas hoy? ")
        print("\n--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")

    elif opcion == "2":
        nombre = input("Ingresa tu nuevo nombre: ")
        print("Tu nombre ha sido actualizado a:", nombre)

    elif opcion == "0":
        continuar = False
        print("Gracias por usar Mi Red. ¡Hasta pronto!")

    else:
        print("Opción no válida. Por favor selecciona 1, 2 o 0.")
