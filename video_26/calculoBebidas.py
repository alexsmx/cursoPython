# vamos a ir a un picnic
# quiero un programa que calcule
# cuantos litros de agua necesito llevar
# el calculo se hará dependiendo del número
# de niños y de adultos que vayan al picnic

def calcularLitrosYLimones(n, a):
    # un adulto consume 2 l. de agua
    # un ninio consume 1 l. de agua
    num_litros = (n*1) + (a*2)
    num_limones = 2 * num_litros
    return num_litros, num_limones


ninios = int(input("Cuantos niños asistirán?"))
adultos = int(input("Cuantos adultos asistirán?"))

litros, limones = calcularLitrosYLimones(ninios, adultos)
print(f"El número de litros necesario es: {litros} lts.")
print(f"Nececistarás { limones } limones")
