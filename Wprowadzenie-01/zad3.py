czymjestLoremIpsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. " \
                     "Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej " \
                     "książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając " \
                     "praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy " \
                     "Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem " \
                     "Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, " \
                     "jak Aldus PageMaker "

imie = "Ryszard"
nazwisko = "Sudujko"

print("W tekście jest {} liter {} oraz {} liter {}.".format(czymjestLoremIpsum.count(imie[2]), imie[2],
                                                            czymjestLoremIpsum.count(nazwisko[3]), nazwisko[3]))

print("Pierwsze 5 liter: {:.5}".format(czymjestLoremIpsum))

print("{0} {1} {3} {2} {5} {3}".format(imie[0], imie[1], imie[2], imie[3], imie[4], imie[5]))
