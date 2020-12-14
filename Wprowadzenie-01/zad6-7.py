"""
    Zad.6  Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak, aby pierwsze 5 liczb zostało w
           oryginalnej liście a pozostałe 5 znalazło się w nowej liście.
"""

lista1 = list(range(1, 11))

lista2 = lista1[5:]
del lista1[5:]

print(lista1)
print(lista2)

"""
    Zad 7. Połącz te listy ponownie. Dodaj do listy wartość „0” na początku.
           Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco. 
"""
# lista1 = lista1 + lista2
lista1.extend(lista2)

print(lista1)

lista1.insert(0, 0)

print(lista1)

kopiaLista1 = lista1.copy()
kopiaLista1.sort(reverse=True)

print(kopiaLista1)
