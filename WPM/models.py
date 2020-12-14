from django.db import models

# Create your models here.

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
    email = models.CharField(max_length=100)
    numerTelefonu = models.CharField(max_length=12)


class Wypozyczenia(models.Model):
    idDaneOsobowe = models.ForeignKey('DaneOsobowe', on_delete=models.CASCADE)
    idPojazdMiejski = models.ForeignKey('PojazdMiejski', on_delete=models.CASCADE)

    dataStart = models.DateField()
    dataStop = models.DateField()


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
    rodzaj = models.CharField(max_length=20, choices=Rodzaj.choices)
    kolor = models.CharField(max_length=45)
    kodSprzetu = models.CharField(max_length=45)


class PojazdyWDokac(models.Model):
    idDok = models.ForeignKey('Dok', on_delete=models.CASCADE)
    idPojazdMiejski = models.ForeignKey('PojazdMiejski', on_delete=models.CASCADE)


class Dok(models.Model):
    nazwa = models.CharField(max_length=100)
    iloscMiejsc = models.IntegerField()
    kraj = models.CharField(max_length=100)
    wojewodztwo = models.CharField(max_length=100)
    miasto = models.CharField(max_length=100)
    ulica = models.CharField(max_length=100)
    narzedzia = models.CharField(max_length=200)


class Lokalizacja(models.Model):
    idPojazdMiejski = models.ForeignKey('PojazdMiejski', on_delete=models.CASCADE)

    szerokoscGeograficzna = models.DecimalField(max_digits=9, decimal_places=2)
    dlugoscGeograficzna = models.DecimalField(max_digits=9, decimal_places=2)
    ostatniaAktualizacja = models.DateTimeField()


class Rozliczenie(models.Model):
    idWypozyczenia = models.ForeignKey('Wypozyczenia', on_delete=models.CASCADE)
    idStawka = models.ForeignKey('Stawka', on_delete=models.CASCADE)

    wplata = models.DecimalField(max_digits=13, decimal_places=2)


class Stawka(models.Model):
    stawka = models.DecimalField(max_digits=4, decimal_places=2)