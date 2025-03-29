"""Escribe un programa que busque si una sub cadena está presente en cada
una de las cadenas de una lista. El programa debe devolver una lista con
valores booleanos que indiquen si la sub cadena fue encontrada en cada
cadena."""

lista = ["Precious love", "Wish", "I loved you", "Fall in love again", "Espresso"]
print(lista)

sublista = []

for i in lista:
    sublista.append("love" in i)
    
print(sublista)
