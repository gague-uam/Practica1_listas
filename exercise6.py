"""Escribe un programa que recorra una lista de cadenas y elimine los
espacios en blanco al principio y al final de cada cadena."""

lista = [" HP ", " DELL ", " Lenovo ", " Mac "]
print(lista)

listacorrecta = []

for i in lista:
    borrar_espacios = i.strip()
    listacorrecta.append(borrar_espacios)

print(listacorrecta)