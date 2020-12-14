import random

"""
    Stwórz funkcję, która jako parametry przyjmuje dwie listy a_list oraz b_list.
    Następnie zwróć listę, która będzie posiadać parzyste indeksy z listy a_list oraz nieparzyste z b_list.
"""

"""
    Funkcja 'randomowe_liczby':
    Wstawia do listy ('lista') określoną ilość ('ilosc_elemntów') liczb pseudolosowych
    z podanego zakresu ('od', 'do').
    
    * lista - lista, w którą wstawiamy elementy
    * ilosc_elementow - ilość elementów do wstawienia
    * od - początek zakresu
    * do - koniec zakresu
"""


def randomowe_liczby(lista, ilosc_elementow, od, do):
    for i in range(ilosc_elementow):
        lista.append(random.randrange(od, do))
        # print(lista)

    # Pętle 'while' robiąca to samo co powyżesz pętla 'for':
    """
        i = 0
        while i <= ilosc_elementow:
            lista.append(random.randrange(od, do))
            print(lista)
            i = i + 1
    """

# Tesowe działanie fukncji 'randomowe_liczby':
"""
    listaTestowa = list()
    randomowe_liczby(listaTestowa, 8, 4, 212)
    print(listaTestowa)
    listaTestowa.clear()
"""

"""
    Funkcja 'listy':
    Jako argumenty wprowadzane są dwie listy: 'lista_a', 'lista_b'.

    Z listy 'lista_a' pierwsza pętla 'for' wybiera wartości, które są przypisane do parzystych indeksów listy
    i dołącza je do listy 'lista_ab'.

    Następnie z listy 'lista_b' druga pętla 'for' wybiera wartości, które są przypisane do nieparzystych indeksów listy
    i dołącza je do listy 'lista_ab'.

    Funkcja zwraca listę 'lista_ab' będącą połączeniem wartości z indeksów parzystych listy 'lista_a' oraz 
    wartości z indeksów nieparzystych listy 'lista_b'.
"""


def listy(lista_a, lista_b):
    lista_ab = list()
    for i in range(len(lista_a)):
        if i % 2 == 0:
            lista_ab.append(lista_a[i])
            print("Indeks: {} | Wartość : {}".format(i, lista_a[i]))

    for i in range(len(lista_b)):
        if i % 2 != 0:
            lista_ab.append((lista_b[i]))
            print("Indeks: {} | Wartość: {}".format(i, lista_b[i]))

    return lista_ab


lista1 = list()
lista2 = list()

randomowe_liczby(lista1, 12, 65, 252)
# print(lista1)
randomowe_liczby(lista2, 19, -14, 57)
# print(lista2)

lista3 = list()
lista3 = listy(lista1, lista2)
print(lista3)

