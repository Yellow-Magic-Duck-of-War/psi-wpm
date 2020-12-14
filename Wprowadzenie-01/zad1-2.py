czymjestLoremIpsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. " \
                     "Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej " \
                     "książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając " \
                     "praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy " \
                     "Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem " \
                     "Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, " \
                     "jak Aldus PageMaker "

imie = "Ryszard"
nazwisko = "Sudujko"

literaImie = imie[2]
literaNazwisko = nazwisko[3]

iloscLiteraImie = czymjestLoremIpsum.count(literaImie)
iloscLiteraNazwisko = czymjestLoremIpsum.count(literaNazwisko)

print("W tekście jest %d liter %s oraz %d liter %s." % (iloscLiteraImie, literaImie, iloscLiteraNazwisko, literaNazwisko))

# print("W tekście jest {} liter {} oraz {} liter {}.".format(czymjestLoremIpsum.count(imie[2]), imie[2],
#                                                             czymjestLoremIpsum.count(nazwisko[3]), nazwisko[3]))

