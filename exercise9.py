"""Escribe un programa que recorra una lista de cadenas y elimine aquellas
que estén vacías. Imprime la lista resultante."""

lista = ["", "Gabriela", "", "Steven", "Casados", "", ":3"]
print(lista)

listacorrecta = []

for i in lista:
    if i:
        listacorrecta.append(i)

print(listacorrecta)