from django.contrib.auth.models import User, Group

from rest_framework import serializers

from WPM.models import DaneOsobowe, AdresZamieszkania, Dok, Lokalizacja, PojazdMiejski, PojazdWDoku, Rozliczenie,\
                       Stawka, Wypozyczenie

"""
    Ćwiczenie 5.

    Celem ćwiczeń będzie stworzenie klas odpowiedzialnych
    za serializację danych w naszym projekcie API.

    Następujące polecenia powinny być wykonane dla każdego modelu w projekcie,
    do którego będziemy mieli dostęp zewnętrzny (przez wykonanie endpointu, np. tworzenie zamówienia).

    ✓ 1. W aplikacji, w której znajduje się nasz model otwieramy/tworzymy plik 'serializers.py'.

    ✓ 2. W nagłówku pliku dodajemy import: from rest_framework import serializers.

    ✓ 3. Tworzymy klasę dziedziczącą po 'serializers.Serializer',
         a następnie tworzymy odpowiednie pola, jako odpowiednik naszego modelu, które powinny zostać sprawdzone
         (praktycznie wszystkie, musimy sprawdzić czy przychodzące dane są dobrego typu np.
          do pola modelu z datą nie podajemy stringa z przepisem na barszcz).

    X 4. Jeżeli dany model wymaga dodatkowej walidacji (np. data stworzenia zamówienia nie może być w przyszłości),
             tworzymy odpowiednie funkcje.

    50/50 5. Nadpisujemy odpowiednie funkcje create, update itp. w momencie gdy musimy zapisać obiekty w inny sposób
             (np. chcemy dodać użytkownika jako właściciela stworzonego modelu).

    ✓ 6. Sprawdzamy, które z utworzonych serializerów możemy zamienić na ModelSerializer,
         i implementujemy gdy to możliwe (Dokumentacja).
"""
# ----------------------------------------------------------------------------------------------------------------------


# Serializer użytkownika:
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User

        fields = ['url', 'username', 'email', 'groups']


# ----------------------------------------------------------------------------------------------------------------------


# Serializer grupy:
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group

        fields = ['url', 'name']


# ----------------------------------------------------------------------------------------------------------------------


class DaneOsoboweSerializer(serializers.HyperlinkedModelSerializer):

    wypozyczenie = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='wypozyczenie-detail')
    rozliczenie = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rozliczenie-detail')
    adres_zamieszkania = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                             view_name='adres-zamieszkania-detail')

    class Meta:
        model = DaneOsobowe

        fields = ['url', 'id', 'imie', 'nazwisko', 'plec', 'dataUrodzenia', 'email', 'numerTelefonu',
                  'idAdresZamieszkania', 'adres_zamieszkania', 'wypozyczenie', 'rozliczenie']


# ----------------------------------------------------------------------------------------------------------------------


class AdresZamieszkaniaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AdresZamieszkania

        fields = ['url', 'id', 'ulica', 'miasto', 'kodPocztowy']


# ----------------------------------------------------------------------------------------------------------------------


class DokSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dok

        fields = ['url', 'id', 'nazwa', 'iloscMiejsc', 'ulica', 'miasto', 'narzedzia']


# ----------------------------------------------------------------------------------------------------------------------


class LokalizacjaSerializer(serializers.HyperlinkedModelSerializer):
    pojazd_miejski = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='pojazd-miejski-detail')

    class Meta:
        model = Lokalizacja

        fields = ['url', 'id', 'szerokoscGeograficzna', 'dlugoscGeograficzna', 'ostatniaAktualizacja',
                  'idPojazdMiejski', 'pojazd_miejski']


# ----------------------------------------------------------------------------------------------------------------------


class PojazdMiejskiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PojazdMiejski

        fields = ['url', 'id', 'typNapedu', 'rodzaj', 'kolor', 'kodSprzetu', 'wzrost']


# ----------------------------------------------------------------------------------------------------------------------


class PojazdWDokuSerializer(serializers.HyperlinkedModelSerializer):
    dok = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='dok-detail')
    pojazd_miejski = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='pojazd-miejski-detail')

    class Meta:
        model = PojazdWDoku

        fields = ['url', 'id', 'idDok_id', 'idPojazdMiejski', 'dok', 'pojazd_miejski']


# ----------------------------------------------------------------------------------------------------------------------


class RozliczenieSerializer(serializers.HyperlinkedModelSerializer):
    wypozyczenia = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='wypozyczenia-detail')
    stawka = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='stawka-detail')

    class Meta:
        model = Rozliczenie

        fields = ['url', 'id', 'wplata', 'idWypozyczenia', 'idStawka', 'wypozyczenia', 'stawka']


# ----------------------------------------------------------------------------------------------------------------------


class StawkaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stawka

        fields = ['url', 'id', 'stawka']


# ----------------------------------------------------------------------------------------------------------------------


class WypozyczenieSerializer(serializers.HyperlinkedModelSerializer):
    dane_osobowe = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='dane_osobowe-detail')
    pojazd_miejski = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='pojazd-miejski-detail')

    class Meta:
        model = Wypozyczenie

        fields = ['url', 'id', 'dataStart', 'dataStop', 'idDaneOsobowe', 'idPojazdMiejski', 'dane_osobowe',
                  'pojazd_miejski']

# ----------------------------------------------------------------------------------------------------------------------
