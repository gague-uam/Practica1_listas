"""Escribe un programa que recorra una lista de cadenas y cuente cuántas
veces aparece un carácter específico en cada cadena. Al final, muestra el
conteo para cada cadena."""

lista = ["Snoopy", "Charlie Brown", "Peanuts", "Woodstock", "Linus"]
print(lista)

for i in lista:
    letra = "o"
    conteo = i.count(letra)
    print(f"La letra '{letra}' aparece {conteo} veces en la cadena")