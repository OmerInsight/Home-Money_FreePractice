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
print(f"Compras de Herber {Herber:*>12,.2f}")
print(f"Compras de Lucas {Lucas:*>12,.2f}")
print(f"Compras de Omer {Omer:*>12,.2f}")

print(f"Gastos del Mes {mes} {año} : {gasto_del_mes:*>12,.2f} ")
print()
print(f"Gasto Individual de {mes} {año} : {gasto_individual:*>12,.2f} ")
print()
print()
d_Herber = gasto_individual - Herber
print(f"Diferencia Herber: {d_Herber:*>12,.2f} ")
d_lucas = gasto_individual - Lucas
print(f"Diferencia Lucas:  {d_lucas:*>12,.2f} ")
d_omer = gasto_individual - Omer
print(f"Diferencia Omer: {d_omer:12,.2f}")
print()
print("♫♪♬🎶 Paga lo que debe come Chocolate ♫♪♬🎶")
