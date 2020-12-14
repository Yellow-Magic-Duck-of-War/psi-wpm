"""
    Stwórz funkcję, która przyjmie jako parametry 'text' oraz 'letter',
    a następnie zwróci wynik usunięcia wszytkich wystąpień wartości w 'letter' z tekstu 'text'.
"""


def usunLitere(text, letter):
    litera = str(letter)
    tekstPoZmianie = text.replace(litera.upper(), "").replace(litera.lower(), "")

    return tekstPoZmianie


tekst = "Coś tam, coś tam, bla bla bla, pozrdo 600!"

tekstPoZmianie = usunLitere(tekst, 'b')
print(tekstPoZmianie)