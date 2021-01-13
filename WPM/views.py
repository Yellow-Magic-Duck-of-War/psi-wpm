from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import status

# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

# Import modeli z pliku 'models.py':
from .models import DaneOsobowe, AdresZamieszkania, Dok, Lokalizacja, PojazdMiejski, PojazdWDoku, Rozliczenie, \
    Stawka, Wypozyczenie

# Import serializerów z pliku 'serializers.py':
from .serializers import DaneOsoboweSerializer, AdresZamieszkaniaSerializer, DokSerializer, LokalizacjaSerializer, \
    PojazdMiejskiSerializer, PojazdWDokuSerializer, RozliczenieSerializer, StawkaSerializer, WypozyczenieSerializer, \
    UserSerializer, GroupSerializer

# ĆWICZENIE 6
"""
    Celem ćwiczeń będzie stworzenie widoków (endpointów),
    dzięki którym użytkownik będzie mógł łączyć się z naszym API
    by pobierac, edytować czy usuwać dane.
    W tym celu zostanie użyte djangorestframework.

    ✓ 1. Odpal swoje środowisko virtualenv, w którym już masz zainstalowane django.
    ✓ 2. Za pomocą pip doinstaluj djangorestframework, jeżeli jeszcze tego nie zrobiłeś,
    ✓ 3. Dodaj 'rest_framework' do zainstalowanych aplikacji w swoim projekcie Django,
    ✓ 4. Dodaj widoki drf do urlpatterns swojego projektu: url(r'^api-auth/', include('rest_framework.urls'))

    ✓ 5. Stwórz widoki dla swoich modeli na podstawie dokumentacji. A następnie dodaj je do urlpatterns by wyświetliły
         się w liście dostępnych endpointów API.
    ✓  * Zwróć uwagę, które modele powinny mieć możliwość dodawania, usuwania czy edytowania informacji.
         Może niektóre powinny tylko wyświetlać dane?
    ✓  * Pamiętaj by zastosować serializery z poprzednich zajęć.

    6. Dodaj zezwolenia do aplikacji, tak by tylko zarejestrowani uzytkownicy mogli korzystać z endpointów.
    7. Dodaj endpointy, które są dostępne tylko dla administratora.
"""

# ĆWICZENIE 7
"""
    ✓ 1. Dodaj widok oparty na GenericAPIView pozwalający na nawigację po API.
    ? 2. Zamiast wartości kluczy obcych wstaw pole opisujące dany rekord.
       (np. nazwisko, nazwa, tytuł) - użyj SlugRelatedField z klasy HyperlinkedModelSerializer.
    3. W związach jeden do wielu po stronie jeden wstaw linki do rekordów,
       po stronie wiele - użyj HyperlinkedRelatedField z klasy HyperlinkedModelSerializer.
    ✓ 4. Ustaw globalną paginację z liczbą pozycji na stronę 5.
    ✓ 5. Ustaw filtry i sortowanie na poszczególne widoki.
    ✓ 6. Dodaj własne filtry na datę i liczby jako przedział od - do.
"""

# Widoki Genryczne:

"""
Biblioteki:
from .models import (...)
from .serializers import (...)
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
"""


# ----------------------------------------------------------------------------------------------------------------------


# Z wykładu 7:
class APIRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        # 'adres-o-nazwie-modelu': reverse(NazwaWidokuGenerycznegoList.name, request=request),

        return Response({'dane-osobowe': reverse(DaneOsoboweList.name, request=request),
                         'adres-zamieszkania': reverse(AdresZamieszkaniaList.name, request=request),
                         'dok': reverse(DokList.name, request=request),
                         'lokalizacja': reverse(LokalizacjaList.name, request=request),
                         'pojazd-miejski': reverse(PojazdMiejskiList.name, request=request),
                         'pojazdy-w-dokach': reverse(PojazdWDokuList.name, request=request),
                         'rozliczenie': reverse(RozliczenieList.name, request=request),
                         'stawka': reverse(StawkaList.name, request=request),
                         'wypozyczenia': reverse(WypozyczenieList.name, request=request),
                         })


# ----------------------------------------------------------------------------------------------------------------------

class DaneOsoboweFilter(FilterSet):
    from_data_urodzenia = DateTimeFilter(field_name='data_urodzenia', lookup_expr='gte')
    to_data_urodzenia = DateTimeFilter(field_name='data_urodzenia', lookup_expr='lte')

    class Meta:
        model = DaneOsobowe
        fields = ['from_data_urodzenia', 'to_data_urodzenia']


class DaneOsoboweList(generics.ListCreateAPIView):
    queryset = DaneOsobowe.objects.all()
    serializer_class = DaneOsoboweSerializer
    # permission_classes = [permissions.IsAdminUser]

    name = 'dane-osobowe-list'

    filter_class = DaneOsoboweFilter

    filter_fields = ['imie', 'nazwisko']
    search_fields = ['imie', 'nazwisko']
    ordering_fields = ['imie', 'nazwisko']

    """
    def list(self, request):
        queryset = self.get_queryset()
        serializer = DaneOsoboweSerializer(queryset, many=True)

        return Response(serializer.data)
    """


class DaneOsoboweDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DaneOsobowe.objects.all()
    serializer_class = DaneOsoboweSerializer
    # permission_classes = [permissions.IsAdminUser]

    name = 'dane-osobowe-detail'


# ----------------------------------------------------------------------------------------------------------------------


class AdresZamieszkaniaList(generics.ListCreateAPIView):
    queryset = AdresZamieszkania.objects.all()
    serializer_class = AdresZamieszkaniaSerializer
    # permission_classes = [permissions.IsAdminUser]

    name = 'adres-zamieszkania-list'

    filter_fields = ['ulica', 'miasto', 'kodPocztowy']
    search_fields = ['ulica', 'miasto', 'kodPocztowy']
    ordering_fields = ['ulica', 'miasto', 'kodPocztowy']


class AdresZamieszkaniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdresZamieszkania.objects.all()
    serializer_class = AdresZamieszkaniaSerializer
    # permission_classes = [permissions.IsAdminUser]

    name = 'adres-zamieszkania-detail'


# ----------------------------------------------------------------------------------------------------------------------


class DokList(generics.ListCreateAPIView):
    queryset = Dok.objects.all()
    serializer_class = DokSerializer

    name = 'dok-list'

    filter_fields = ['nazwa', 'iloscMiejsc', 'miasto', 'ulica']
    search_fields = ['nazwa', 'iloscMiejsc', 'miasto', 'ulica']
    ordering_fields = ['nazwa', 'iloscMiejsc', 'miasto', 'ulica']


class DokDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dok.objects.all()
    serializer_class = DokSerializer

    name = 'dok-detail'


# ----------------------------------------------------------------------------------------------------------------------


class LokalizacjaList(generics.ListCreateAPIView):
    queryset = Lokalizacja.objects.all()
    serializer_class = LokalizacjaSerializer

    name = 'lokalizacja-list'

    filter_fields = ['szerokoscGeograficzna', 'dlugoscGeograficzna', 'ostatniaAktualizacja']
    search_fields = ['szerokoscGeograficzna', 'dlugoscGeograficzna', 'ostatniaAktualizacja']
    ordering_fields = ['szerokoscGeograficzna', 'dlugoscGeograficzna', 'ostatniaAktualizacja']


class LokalizacjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lokalizacja.objects.all()
    serializer_class = LokalizacjaSerializer

    name = 'lokalizacja-Detail'


# ----------------------------------------------------------------------------------------------------------------------


class PojazdMiejskiList(generics.ListCreateAPIView):
    queryset = PojazdMiejski.objects.all()
    serializer_class = PojazdMiejskiSerializer

    name = 'pojazd-miejski-list'

    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


class PojazdMiejskiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PojazdMiejski.objects.all()
    serializer_class = PojazdMiejskiSerializer

    name = 'pojazd-miejski-detail'


# ----------------------------------------------------------------------------------------------------------------------


class PojazdWDokuList(generics.ListCreateAPIView):
    queryset = PojazdWDoku.objects.all()
    serializer_class = PojazdWDokuSerializer

    name = 'pojazd-w-doku-list'

    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


class PojazdWDokuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PojazdWDoku.objects.all()
    serializer_class = PojazdWDokuSerializer

    name = 'pojazd-w-dokau-detail'


# ----------------------------------------------------------------------------------------------------------------------


class RozliczenieList(generics.ListCreateAPIView):
    queryset = Rozliczenie.objects.all()
    serializer_class = RozliczenieSerializer

    name = 'rozliczenie-list'

    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


class RozliczenieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rozliczenie.objects.all()
    serializer_class = RozliczenieSerializer

    name = 'rozliczenie-detail'


# ----------------------------------------------------------------------------------------------------------------------


class StawkaFilter(FilterSet):
    min_stawka = NumberFilter(field_name='stawka', lookup_expr='gte')
    max_stawka = NumberFilter(field_name='stawka', lookup_expr='lte')

    class Meta:
        model = Stawka
        fields = ['min_stawka', 'max_stawka']


class StawkaList(generics.ListCreateAPIView):
    queryset = Stawka.objects.all()
    serializer_class = StawkaSerializer

    name = 'stawka-list'

    filter_class = StawkaFilter

    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


class StawkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stawka.objects.all()
    serializer_class = StawkaSerializer

    name = 'stawka-detail'


# ----------------------------------------------------------------------------------------------------------------------


class WypozyczenieList(generics.ListCreateAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer

    name = 'wypozyczenie-list'

    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


class WypozyczenieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer

    name = 'wypozyczenie-detail'


# ----------------------------------------------------------------------------------------------------------------------

"""STARE WIDOKI PRZENIESIONE TYMCZASOWO DO NOTATNIKA"""

# Widoki '@csrf_exempt' i '@api_view':

"""
Biblioteki:
from rest_framework.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import 
from rest_framework.response import Response
from .models import DaneOsobowe
from .serializers import DaneOsoboweSerializer
from rest_framework import status
from django.http import HttpResponse


# @csrf_exempt
@api_view(['GET', 'POST'])
def dane_osobwe_list(request):
    if request.method == 'GET':

        dane_osobowe = DaneOsobowe.objects.all()
        serializer = DaneOsoboweSerializer(dane_osobowe, many=True)

        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':

        # dane = JSONParser().parse(request)
        # serializer = DaneOsoboweSerializer(data=dane)
        serializer = DaneOsoboweSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status.HTTP_201_CREATED)

        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def dane_osobwe_detale(request, pk):
    try:
        dane_osobowe = DaneOsobowe.objects.get(pk=pk)
    except DaneOsobowe.DoesNotExist:

        # return HttpResponse(status=404)
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = DaneOsoboweSerializer(dane_osobowe)

        # return JsonResponse(serializer.data)
        return Response(serializer.data)

    elif request.method == 'PUT':

        # dane = JSONParser().parse(request)
        # serializer = DaneOsoboweSerializer(dane_osobowe, data=dane)
        serializer = DaneOsoboweSerializer(dane_osobowe, data=request.data)

        if serializer.is_valid():
            serializer.save()

            # return JsonResponse(serializer.data)
            return Response(serializer.data)

        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        dane_osobowe.delete()

        # return HttpResponse(status=204)
        return HttpResponse(status.HTTP_204_NO_CONTENT)
"""

# ----------------------------------------------------------------------------------------------------------------------

# Widoki - APIViews:

"""
Biblioteki:
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DaneOsobowe
from .serializers import DaneOsoboweSerializer
from rest_framework import status


class DaneOsoboweListAPIView(APIView):

    def get(self, request):
        dane_osobowe = DaneOsobowe.objects.all()
        serializer = DaneOsoboweSerializer(dane_osobowe, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = DaneOsoboweSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class DaneOsoboweDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return DaneOsobowe.objects.get(pk=pk)

        except DaneOsobowe.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):

        dane_osobwe = self.get_object(pk)
        serializer = DaneOsoboweSerializer(dane_osobwe)

        return Response(serializer.data)

    def put(self, request, pk):

        dane_osobwe = self.get_object(pk)
        serializer = DaneOsoboweSerializer(dane_osobwe, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        dane_osobwe = self.get_object(pk)

        dane_osobwe.delete()

        return Response(status.HTTP_204_NO_CONTENT)
"""
