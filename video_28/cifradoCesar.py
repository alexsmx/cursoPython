# https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar
abecedario = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def cifrado_generico(cadena, accion, desplazamiento=3):
    if accion == "descifrado":
        desplazamiento = desplazamiento * -1
    texto_cifrado = ""
    for letra in cadena:
        # deplaza esa letra en un numero de posiciones indicadas por la variable desplazamiento
        posicion = abecedario.find(letra)
        if posicion == -1:
            texto_cifrado += letra
        else:
            posicion_final = (posicion + desplazamiento) % len(abecedario)
            nueva_letra = abecedario[posicion_final]
            texto_cifrado += nueva_letra

    return texto_cifrado


def cifre(cadena, desplazamiento=3):
    return cifrado_generico(cadena, "cifrado", desplazamiento)


def descifre(cadena_cifrada, desplazamiento=3):
    return cifrado_generico(cadena_cifrada, "descifrado", desplazamiento)


accion = input("Que deseas hacer? Cifrar(c)/Descifrar(d)")
accion = accion.lower()
desplazamiento = int(input("Que desplazamiento vas a utilizar? (1-10)"))
frase = input("Dame la frase:")
while frase != "":
    texto_cifrado = ""
    if accion == "c" or accion == "cifrar":
        texto_cifrado = cifre(frase, desplazamiento)
    elif accion == "d" or accion == "descifrar":
        texto_cifrado = descifre(frase, desplazamiento)
    else:
        print("Acción errónea")
        break
    print(f"La frase cifrada es: {texto_cifrado}")
    frase = input("Dame la siguiente frase:")

print("Hasta luego")
