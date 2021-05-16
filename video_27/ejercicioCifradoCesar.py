# https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar

def cifre(cadena, desplazamiento=3):
    return ""


def descifre(cadena_cifrada, desplazamiento=3):
    return ""


accion = input("Que deseas hacer? Cifrar(c)/Descifrar(d)")
desplazamiento = input("Que desplazamiento vas a utilizar? (1-10)")
frase = input("Dame la frase:")
while frase != "":
    texto_cifrado = ""
    if accion == "c":
        texto_cifrado = cifre(frase, desplazamiento)
    elif accion == "d":
        texto_cifrado = descifre(frase, desplazamiento)
    print(texto_cifrado)
    frase = input("Dame la siguiente frase:")

print("Hasta luego")
