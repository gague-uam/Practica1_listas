"""Escribe un programa que recorra una lista de cadenas y divida cada cadena
en subcadenas utilizando un delimitador específico (por ejemplo, una coma
o un espacio)."""

lista = ["Lee Jooyeon", "Han Hyeongjun", "Oh Seungmin", "Kwak Jiseok", "Kim Jungsu", "Goo Gunil"]
print(lista)

cadenas = []

for i in lista:
    dividir_cadena = i.split(" ")
    cadenas.append(dividir_cadena)

print(cadenas)
