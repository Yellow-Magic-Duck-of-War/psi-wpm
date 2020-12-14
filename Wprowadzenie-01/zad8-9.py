import datetime

"""
    Zad. 8: Za pomocą krotek stwórz listę studentów swojej grupy przypisując numer indeksu do imienia i nazwiska
            (dane nie muszą być prawdziwe).
"""

student = ("Michał Woźniak", "Roman Giertych", "Zbigniew Ziobro", "Zbgniew Stonoga")
indeks = (114253, 232451, 12223, 3325)

"""
listaStudentow = []

if len(student) == len(indeks):
    for i in range(len(student)):
        listaStudentow.append((student[i], indeks[i]))
"""

listaStudentow = [(indeks[i], student[i]) for i in range(len(student)) if len(student) == len(indeks)]

print(listaStudentow)

"""
    Zad. 9: Przekształć poprzednie zadanie na słownik, a następnie dodaj pary zawierające wiek, adres email,
            rok urodzenia oraz adres.
"""

email = ("MW@email.com", "RG@email.com", "ZZ@email.com", "69sweet16@mail.pl")
# print(email)

aktualnyRok = datetime.date.today().year
# print(aktualnyRok)

rokUrodzenia = (1923, 1985, 2001, 1832)
# print(rokUrodzenia)

wiek = tuple([aktualnyRok - rokUrodzenia[x] for x in range(len(rokUrodzenia))])
# print(wiek)

adres = ("ul.Jegiellona 56T/1", "ul.Gomułki 45V/8", "ul.Wiejska 4/6/8", "ul.Zamość 12")
# print(adres)

slownikStudentow = {}

for i in range(len(student)):
    slownikStudentow[indeks[i]] = {
        "Imię i nazwisko": student[i],
        "Rok urodzenia": rokUrodzenia[i],
        "Wiek": wiek[i],
        "Adres": adres[i],
        "Email": email[i]
    }

for klucz, wartosc in slownikStudentow.items():
    print(klucz, wartosc)