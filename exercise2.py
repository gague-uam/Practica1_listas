"""Escribe un programa que recorra una lista de cadenas y calcule la longitud
de cada cadena, almacenando el resultado en una nueva lista."""

lista = ["Cinnamoroll", "Chiffon", "Moka", "Milk", "Capuccino"]
print(lista)

lista2 = []

for i in lista:
    lista2.append(len(i))

print(lista2)