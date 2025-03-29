"""Escribe un programa que recorra una lista de cadenas y reemplace todas
las apariciones de un carácter específico con otro carácter, luego imprime la
lista modificada."""

listabuena = ["Test me", "Help me Rock&Roll", "Save me", "Let me love You"]
print(listabuena)

listamala = []

for i in listabuena:
    listamala.append(i.replace("me", "him"))

print(listamala)