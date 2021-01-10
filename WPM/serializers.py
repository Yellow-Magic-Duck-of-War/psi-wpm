
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

    50/50 4. Jeżeli dany model wymaga dodatkowej walidacji (np. data stworzenia zamówienia nie może być w przyszłości),
             tworzymy odpowiednie funkcje.

    50/50 5. Nadpisujemy odpowiednie funkcje create, update itp. w momencie gdy musimy zapisać obiekty w inny sposób
             (np. chcemy dodać użytkownika jako właściciela stworzonego modelu).

    ✓ 6. Sprawdzamy, które z utworzonych serializerów możemy zamienić na ModelSerializer,
         i implementujemy gdy to możliwe (Dokumentacja).
"""

from django.contrib.auth.models import User, Group

from rest_framework import serializers
from WPM.models import DaneOsobowe, Dok, Lokalizacja, PojazdMiejski, PojazdyWDokach, Rozliczenie, Stawka, Wypozyczenia

# requaet=True jeśli w kolumnie modelu jest not null

"""
    Różnica między gwiazdkami:
    
    validated_data - 
    
    *validated_data - dowolna liczba parametrów
    
    **validated_data - przekazanie słownika
    
    NA PRZYKŁAD:
    
    def create(self, validated_data):
        return NazwaModelu.object.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.nazwaKolumny = validated_data.get('nazwaKolumny', instance.nazwaKolumny)
        .
        .
        .
        instance.save()
        return instance
    
    Skończyłem 
"""

# Serializer użytkownika:
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


# Serializer grupy:
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class DaneOsoboweSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DaneOsobowe
        fields = ['url', 'id', 'imie', 'nazwisko', 'plec', 'dataUrodzenia', 'kraj', 'wojewodztwo', 'miasto', 'ulica',
                  'kodPocztowy', 'email', 'numerTelefonu']

class DokSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dok
        fields = ['url', 'id', 'nazwa', 'iloscMiejsc', 'kraj', 'wojewodztwo', 'miasto', 'ulica', 'narzedzia']


class LokalizacjaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lokalizacja
        fields = ['url', 'id', 'szerokoscGeograficzna', 'dlugoscGeograficzna', 'ostatniaAktualizacja', 'idPojazdMiejski_id']


class PojazdMiejskiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PojazdMiejski
        fields = ['url', 'id', 'typNapedu', 'rodzaj', 'kolor', 'kodSprzetu', 'wzrost']


class PojazdyWDokachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PojazdyWDokach
        fields = ['url', 'id', 'idDok_id', 'idPojazdMiejski_id']


class RozliczenieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rozliczenie
        fields = ['url', 'id', 'wplata', 'idStawka_id', 'idWypozyczenia_id']


class StawkaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stawka
        fields = ['url', 'id', 'stawka']


class WypozyczeniaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wypozyczenia
        fields = ['url', 'id', 'dataStart', 'dataStop', 'idDaneOsobowe_id', 'idPojazdMiejski_id']