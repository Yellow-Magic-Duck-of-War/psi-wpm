książki = []
książka = {}

warunek = True
print("Wprowadź kilka książek:")

indeksKsiążki = 0
while warunek == True:

    książka[indeksKsiążki] = \
        {
            'tytuł': input("Tytuł: "),
            'autor': input("Autor: "),
            'wydawca': input("Wydawca: "),
            'miejsce': input("Miejsce wydania: "),
            'rok': input("Rok wydania: ")
        }

    książki.append(książka[indeksKsiążki])

    indeksKsiążki = indeksKsiążki + 1

    decyzja = input("Czy chcesz wprowadzić następną książkę? (T/N): ")

    while decyzja != 'T' and decyzja != 'N':
        decyzja = input("Czy chcesz wprowadzić następną książkę? (T/N): ")
        if decyzja == 'N':
            break

    if decyzja == 'N':
        break

def wypiszSpis (spisKsiążek):
    tekst = "Książka \"{}\" autorstwa {} wydana przez {} w {} {} roku."

    for wartosc in spisKsiążek:
        print(tekst.format(wartosc['tytuł'],wartosc['autor'],wartosc['wydawca'],wartosc['miejsce'], wartosc['rok']))

wypiszSpis(książki)
