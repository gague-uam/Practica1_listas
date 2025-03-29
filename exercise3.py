"""Escribe un programa que recorra una lista de cadenas y convierta cada
cadena a mayúsculas o minúsculas dependiendo de un criterio. Si la
longitud de la cadena es par, se convertirá a mayúsculas; si es impar, a
minúsculas."""

lista = ["You make me", "She smiled", "Tick Tock", "You Were Beautiful"]
print(lista)

for i in lista:
    contador = 1
    if len(i) % 2 == 0:
        print(i.upper())
    else:
        print(i.lower())