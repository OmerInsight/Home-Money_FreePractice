mes = str(input("Ingresa el mes: "))
año = int(input("Ingresa el año: "))
Herber = int(input("Ingresa tu gasto Herber: "))
Lucas = int(input("Ingresa tu gasto Lucas: "))
Omer = int(input("Ingresa tu gasto Omer: "))


def gasto_real(x, y, z):
    gasto_del_mes = x + y + z
    gasto_individual = gasto_del_mes / 3

    return gasto_del_mes, gasto_individual


gasto_del_mes, gasto_individual = gasto_real(Herber, Lucas, Omer)

gasto_del_mes, gasto_individual = gasto_real(Herber, Lucas, Omer)
print()
print(f"Gastos del Mes {mes} {año} : {gasto_del_mes} ")
print()
print(f"Gasto Individual de {mes} {año} : {gasto_individual} ")
print()
print("Diferencia Herber:", (gasto_individual - Herber))
print("Diferencia Lucas:", (gasto_individual - Lucas))
print("Diferencia Omer:", (gasto_individual - Omer))
print()
print("♫♪♬🎶 Paga lo que debe come Chocolate ♫♪♬🎶")