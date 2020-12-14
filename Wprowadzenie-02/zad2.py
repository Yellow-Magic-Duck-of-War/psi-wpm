"""
    Stwórz funkcję, która przyjmuje parametr 'data_text',
    a następnie zwróci następujące informacje o parametrze w formie słownika (dict):

    * 'length': długość podanego tekstu,
    * 'letters': lista znaków w wyrazie np. ['D', 'o', 'g'],
    * 'big_letters': zamieniony parametr w kapitaliki np. DOG
    * 'small_letters': zamieniony parametr w małe litery np. dog
"""

"""
    Funkcja 'informacjeOTekscie':
    Jako argument wprowadza się string lub zmienną zawierającą string.
    
    * length - zmienna zawiera długość podanego stringa
    * letters - lista, do której pętla 'for' wstawia znaki z podanego stringa
    * big_letters - zmienna zawiera podanego stringa po zamianie wszyskich liter na wielkie
    * small_letters - zmienna zawiera podanego stringa po zamianie wszyskich liter na małe
    * dane - słownik gdzie kluczami są nazwy zmiennych, a wartościami zawartość zmiennch
    
    Funkcja zwraca słownik 'dane'.
"""


def informacjeOTekscie(data_text):
    length = len(data_text)
    # print(length)

    letters = list()
    for i in range(length):
        letters.append(data_text[i])
        # print(letters)

    big_letters = data_text.upper()
    # print(big_letters)

    small_letters = data_text.lower()
    # print((small_letters))

    dane = \
        {
            'length': length,
            'letters': letters,
            'big_letters': big_letters,
            'small_letters': small_letters
        }

    return dane


def wyswietlSlownik(slownik):
    for klucz, wartosc in slownik.items():
        print("{} : {}".format(str(klucz), str(wartosc)))


tekst = "Coś tam, coś tam, bla bla bla!"

info = informacjeOTekscie(tekst)

wyswietlSlownik(info)
