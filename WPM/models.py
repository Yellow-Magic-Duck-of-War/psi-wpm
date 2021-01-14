from django.db import models

"""
Może się przydać do uprawmnieniń użytkownika.

from django.contrib.auth.models import User

autor = models.ForeignKey(User, default=None)
"""


# Modele odpowiadają tabelom w bazie danych.

class DaneOsobowe(models.Model):
    class Plec(models.TextChoices):  # Zdefiniowanie ENUM
        KOBIETA = 'K', ('Kobieta')
        MEZCZYZNA = 'M', ('Mężczyzna')

    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    plec = models.CharField(max_length=1, choices=Plec.choices)
    dataUrodzenia = models.DateField()
    email = models.CharField(max_length=100, unique=True)
    numerTelefonu = models.CharField(max_length=12, unique=True)
    idAdresZamieszkania = models.ForeignKey('AdresZamieszkania', related_name='dane_osobowe',
                                            on_delete=models.PROTECT, default=None)

    # Sortowanie po...

    class Meta:
        ordering = ('nazwisko', 'imie')

    # Wolne, niedokładne tłumaczenie:
    # Zwróci imię i nazwisko w panelu Adminostratora przy przegldzie danych w bazie danych.

    def __str__(self):
        return self.imie + ' ' + self.nazwisko


# ----------------------------------------------------------------------------------------------------------------------


class AdresZamieszkania(models.Model):

    ulica = models.CharField(max_length=100)
    miasto = models.CharField(max_length=100, default='Olsztyn')
    kodPocztowy = models.CharField(max_length=9)

    # Sortowanie po:

    class Meta:
        ordering = ('ulica', 'miasto')

    # Wyświetlanie informacji:

    def __str__(self):
        return self.ulica + ' ' + self.miasto + ' ' + self.kodPocztowy


# ----------------------------------------------------------------------------------------------------------------------


class Wypozyczenie(models.Model):
    idDaneOsobowe = models.ForeignKey('DaneOsobowe', related_name='wypozyczenia', on_delete=models.PROTECT)
    idPojazdMiejski = models.ForeignKey('PojazdMiejski', related_name='wypozyczenia', on_delete=models.PROTECT)

    dataStart = models.DateTimeField()
    dataStop = models.DateTimeField()

    # Sortowanie po:
    """
    class Meta:
        ordering = ('idDaneOsobwe.nazwisko', 'idDaneOsobowe.imie', 'idPojazdMiejski.kodSprzetu')
    """
    # Wyświetlanie informacji:

    def __str__(self):
        return self.idDaneOsobowe.imie + ' ' + self.idDaneOsobowe.nazwisko + ' ' + self.idPojazdMiejski.rodzaj + ' ' + \
               self.idPojazdMiejski.kodSprzetu


# ----------------------------------------------------------------------------------------------------------------------


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

    rodzaj = models.CharField(max_length=20, choices=Rodzaj.choices, default=Rodzaj.ROWER)
    typNapedu = models.CharField(max_length=20, choices=TypNapedu.choices, default=TypNapedu.ZWYKLY)
    wzrost = models.CharField(max_length=20, choices=Wzrost.choices, default=Wzrost.DOROSLI)
    kolor = models.CharField(max_length=45, default='czerwony')
    kodSprzetu = models.CharField(max_length=45, unique=True)

    # Sortowanie po:

    class Meta:
        ordering = ('rodzaj', 'typNapedu', 'kodSprzetu')

    # Wyświetlanie informacji:

    def __str__(self):
        return self.rodzaj + ' ' + self.kodSprzetu


# ----------------------------------------------------------------------------------------------------------------------
# OneToOneField zamiadt ForeignKey ?


class PojazdWDoku(models.Model):
    idDok = models.ForeignKey('Dok', related_name='pojazdy_w_dokach', on_delete=models.PROTECT)
    idPojazdMiejski = models.OneToOneField('PojazdMiejski', unique=True, related_name='pojazdy_w_dokach',
                                           on_delete=models.PROTECT)

    # Sortowanie po:
    """
    class Meta:
        ordering = ('idDok.nazwa', 'idPojazdMiejski.kodSprzetu')
    """
    # Wyświetlanie informacji:

    def __str__(self):
        return self.idDok.nazwa + ' ' + self.idPojazdMiejski.kodSprzetu


# ----------------------------------------------------------------------------------------------------------------------


class Dok(models.Model):
    nazwa = models.CharField(max_length=100, unique=True)
    iloscMiejsc = models.IntegerField(default=10)
    miasto = models.CharField(max_length=100, default='Olsztyn')
    ulica = models.CharField(max_length=100)
    narzedzia = models.CharField(max_length=200, default='Brak')

    # Sortowanie po:

    class Meta:
        ordering = ('nazwa', 'ulica', 'miasto')

    # Wyświetlanie informacji:

    def __str__(self):
        return self.nazwa


# ----------------------------------------------------------------------------------------------------------------------


class Lokalizacja(models.Model):
    idPojazdMiejski = models.ForeignKey('PojazdMiejski', related_name='lokalizacje', on_delete=models.PROTECT)

    szerokoscGeograficzna = models.DecimalField(max_digits=9, decimal_places=2)
    dlugoscGeograficzna = models.DecimalField(max_digits=9, decimal_places=2)
    ostatniaAktualizacja = models.DateTimeField()

    """
        Pomysł na pole ostatniaAktualizacaj() - co 10 min GPS wysyła sygnał z aktualizacją lokalizacji pojazdu
                                                i zapisuje ostatnią datę i godzinę
    """

    # Sortowanie po:
    """
    class Meta:
        ordering = ('idPojazdMiejski.kodSprzetu', 'ostatniaAktualizacja')
    """
    # Wyświetlanie informacji:

    def __str__(self):
        return self.idPojazdMiejski.kodSprzetu


# ----------------------------------------------------------------------------------------------------------------------


class Rozliczenie(models.Model):
    idWypozyczenie = models.ForeignKey('Wypozyczenie', related_name='rozliczenia', on_delete=models.PROTECT)
    idStawka = models.ForeignKey('Stawka', related_name='rozliczenia', on_delete=models.PROTECT)

    wplata = models.DecimalField(max_digits=13, decimal_places=2)

    # Sortowanie po:
    """
    class Meta:
        ordering = ('idWypozyczenie.idDaneOsobowe.nazwisko', 'idWypozyczenie.idPojazdMiejski.kodSprzetu')
    """
    # Wyświetlanie informacji:

    def __str__(self):
        return self.idWypozyczenie.idDaneOsobowe.nazwisko + ' ' + self.idWypozyczenie.idPojazdMiejski.kodSprzetu


# ----------------------------------------------------------------------------------------------------------------------


class Stawka(models.Model):
    stawka = models.DecimalField(max_digits=4, decimal_places=2)

    # Sortowanie po:

    class Meta:
        ordering = ('stawka',)

    # Wyświetlanie informacji:

    def __str__(self):
        return self.stawka
