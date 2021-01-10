from django.db import models


# Modele odpowiadają tabelom w bazie danych.

# TRZEBA ZMIENIĆ TE TABELE

class DaneOsobowe(models.Model):
    class Plec(models.TextChoices):  # Zdefiniowanie ENUM
        KOBIETA = 'K', ('Kobieta')
        MEZCZYZNA = 'M', ('Mężczyzna')

    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    plec = models.CharField(max_length=1, choices=Plec.choices)
    dataUrodzenia = models.DateField()
    kraj = models.CharField(max_length=100)
    wojewodztwo = models.CharField(max_length=100)
    miasto = models.CharField(max_length=100)
    ulica = models.CharField(max_length=100)
    kodPocztowy = models.CharField(max_length=9)
    email = models.CharField(max_length=100, unique=True)
    numerTelefonu = models.CharField(max_length=12, unique=True)

    class Meta:
        ordering = ('nazwisko',)

    # Wolne, niedokładne tłumaczenie:
    # Zwróci imię i nazwisko w panelu Adminostratora przy przegldzie danych w bazie danych.

    def __str__(self):
        return self.imie + ' ' + self.nazwisko


class Wypozyczenia(models.Model):
    idDaneOsobowe = models.ForeignKey('DaneOsobowe', on_delete=models.CASCADE)
    idPojazdMiejski = models.ForeignKey('PojazdMiejski', on_delete=models.CASCADE)

    dataStart = models.DateTimeField()
    dataStop = models.DateTimeField()

    class Meta:
        ordering = ('dataStart',)

    def __str__(self):
        return self.idDaneOsobowe.imie + ' ' + self.idDaneOsobowe.nazwisko + ' ' + self.idPojazdMiejski.rodzaj + ' ' + \
               self.idPojazdMiejski.kodSprzetu


class PojazdMiejski(models.Model):
    class Rodzaj(models.TextChoices):
        ROWER = 'rower'
        HULAJNOGA = 'hulajnoga'
        SKUTER = 'skuter'

    class TypNapedu(models.TextChoices):
        ZWYKLY = 'zwykły'
        ELEKTRYCZNY = 'elektryczny'
        HYBRYDA = 'hybryda'

    class Wzrost(models.TextChoices):
        DZIECI = 'dzieci'
        DOROSLI = 'dorośli'

    rodzaj = models.CharField(max_length=20, choices=Rodzaj.choices)
    typNapedu = models.CharField(max_length=20, choices=TypNapedu.choices)
    wzrost = models.CharField(max_length=20, choices=Wzrost.choices, default=Wzrost.DOROSLI)
    kolor = models.CharField(max_length=45)
    kodSprzetu = models.CharField(max_length=45, unique=True)

    class Meta:
        ordering = ('rodzaj',)

    def __str__(self):
        return self.rodzaj + ' ' + self.kodSprzetu

# OneToOneField zamiadt ForeignKey ?

class PojazdyWDokach(models.Model):
    idDok = models.ForeignKey('Dok', on_delete=models.CASCADE)
    idPojazdMiejski = models.OneToOneField('PojazdMiejski', on_delete=models.CASCADE, unique=True)

    """
    class Meta:
        ordering = ('idDok',)
    """

    def __str__(self):
        return self.idDok.nazwa + ' ' + self.idPojazdMiejski.kodSprzetu


class Dok(models.Model):
    nazwa = models.CharField(max_length=100, unique=True)
    iloscMiejsc = models.IntegerField()
    kraj = models.CharField(max_length=100)
    wojewodztwo = models.CharField(max_length=100)
    miasto = models.CharField(max_length=100)
    ulica = models.CharField(max_length=100)
    narzedzia = models.CharField(max_length=200)

    class Meta:
        ordering = ('nazwa',)

    def __str__(self):
        return self.nazwa


class Lokalizacja(models.Model):
    idPojazdMiejski = models.ForeignKey('PojazdMiejski', on_delete=models.CASCADE)

    szerokoscGeograficzna = models.DecimalField(max_digits=9, decimal_places=2)
    dlugoscGeograficzna = models.DecimalField(max_digits=9, decimal_places=2)
    ostatniaAktualizacja = models.DateTimeField()

    """
    class Meta:
        ordering = ('',)
    """

    def __str__(self):
        return self.idPojazdMiejski.kodSprzetu + ' ' + self.szerokoscGeograficzna + ' ' + self.dlugoscGeograficzna\
               + ' ' + self.ostatniaAktualizacja


class Rozliczenie(models.Model):
    idWypozyczenia = models.ForeignKey('Wypozyczenia', on_delete=models.CASCADE)
    idStawka = models.ForeignKey('Stawka', on_delete=models.CASCADE)

    wplata = models.DecimalField(max_digits=13, decimal_places=2)

    def __str__(self):
        return self.idWypozyczenia.idDaneOsobowe.imie + ' ' + self.idWypozyczenia.idDaneOsobowe.nazwisko


class Stawka(models.Model):
    stawka = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.stawka
