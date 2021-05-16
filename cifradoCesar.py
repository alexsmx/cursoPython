# https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar

def cifre(cadena, desplazamiento=3):
    abecedario = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    texto_cifrado = ""
    for letra in cadena:
        # deplaza esa letra en un numero de posiciones indicadas por la variable desplazamiento
        posicion = abecedario.find(letra)
        if posicion == -1:
            texto_cifrado += letra
        else:
            posicion_final = posicion + desplazamiento
            nueva_letra = abecedario[posicion_final]
            texto_cifrado += nueva_letra

    return texto_cifrado


def descifre(cadena_cifrada, desplazamiento=3):
    return ""


accion = input("Que deseas hacer? Cifrar(c)/Descifrar(d)")
desplazamiento = int(input("Que desplazamiento vas a utilizar? (1-10)"))
frase = input("Dame la frase:")
while frase != "":
    texto_cifrado = ""
    if accion == "c":
        texto_cifrado = cifre(frase, desplazamiento)
    elif accion == "d":
        texto_cifrado = descifre(frase, desplazamiento)
    print(f"La frase cifrada es: {texto_cifrado}")
    frase = input("Dame la siguiente frase:")

print("Hasta luego")
