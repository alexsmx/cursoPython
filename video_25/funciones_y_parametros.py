#!python

# agrupar comportamiento, instrucciones
def saludar(nombre, apellido=""):
    print(f"Hola {nombre} {apellido}:")
    print("Esto es un ejemplo de una función que agrupa instrucciones y utiliza un parámetro: " + nombre)

# composición de comportamiento


def despedirse(nombre2):
    print("Adios " + nombre2)


def imprimirConversacion(nombre_conversacion, apellido_conversacion=""):
    saludar(nombre_conversacion, apellido_conversacion)
    despedirse(nombre_conversacion)


imprimirConversacion("Alex")
