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

    50/50 5. Stwórz widoki dla swoich modeli na podstawie dokumentacji.
             A następnie dodaj je do urlpatterns by wyświetliły się w liście dostępnych endpointów API.
           * Zwróć uwagę, które modele powinny mieć możliwość dodawania, usuwania czy edytowania informacji.
             Może niektóre powinny tylko wyświetlać dane?
           * Pamiętaj by zastosować serializery z poprzednich zajęć.

    6. Dodaj zezwolenia do aplikacji, tak by tylko zarejestrowani uzytkownicy mogli korzystać z endpointów.
    7. Dodaj endpointy, które są dostępne tylko dla administratora.
"""

# ĆWICZENIE 7
"""
    1. Dodaj widok oparty na GenericAPIView pozwalający na nawigację po API.
    2. Zamiast wartości kluczy obcych wstaw pole opisujące dany rekord.
       (np. nazwisko, nazwa, tytuł) - użyj SlugRelatedField z klasy HyperlinkedModelSerializer.
    3. W związach jeden do wielu po stronie jeden wstaw linki do rekordów,
       po stronie wiele - użyj HyperlinkedRelatedField z klasy HyperlinkedModelSerializer.
    4. Ustaw globalną paginację z liczbą pozycji na stronę 5.
    5. Ustaw filtry i sortowanie na poszczególne widoki.
    6. Dodaj własne filtry na datę i liczby jako przedział od - do.
"""


from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet

from rest_framework import viewsets, generics, response, authentication, permissions, reverse

# Import modeli z pliku 'models.py':
from WPM.models import DaneOsobowe, Dok, Lokalizacja, PojazdMiejski, PojazdyWDokach, Rozliczenie, Stawka, Wypozyczenia

# Import serializerów z pliku 'serializers.py':
from WPM.serializers import DaneOsoboweSerializer, DokSerializer, LokalizacjaSerializer, PojazdMiejskiSerializer,\
                            PojazdyWDokachSerializer, RozliczenieSerializer, StawkaSerializer, WypozyczeniaSerializer,\
                            UserSerializer, GroupSerializer

# Widoki Genryczne:

# ----------------------------------------------------------------------------------------------------------------------


class DaneOsoboweList(generics.ListCreateAPIView):
    queryset = DaneOsobowe.objects.all()
    serializer_class = DaneOsoboweSerializer
    permission_classes = [permissions.IsAdminUser]

    name = 'dane-osobowe-list'
    filter_fields = ['imie', 'nazwisko']
    search_fields = ['imie', 'nazwisko']
    ordering_fields = ['imie', 'nazwisko']

    """
    def list(self, request):
        queryset = self.get_queryset()
        serializer = DaneOsoboweSerializer(queryset, many=True)

        return response(serializer.data)
    """


class DaneOsoboweDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DaneOsobowe.objects.all()
    serializer_class = DaneOsoboweSerializer
    # permission_classes = [permissions.IsAdminUser]

    name = 'dane-osobowe-detail'
    filter_fields = ['imie', 'nazwisko']
    search_fields = ['imie', 'nazwisko']
    ordering_fields = ['imie', 'nazwisko']


# ----------------------------------------------------------------------------------------------------------------------


class DokList(generics.ListCreateAPIView):
    queryset = Dok.objects.all()
    serializer_class = DokSerializer

    name = 'dok-list'
    filter_fields = ['nazwa', 'iloscMiejsc']
    search_fields = ['nazwa', 'kraj', 'wojewodztwo', 'miasto', 'ulica']
    ordering_fields = ['nazwa']


class DokDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dok.objects.all()
    serializer_class = DokSerializer

    name = 'dok-detail'
    filter_fields = ['imie', 'nazwisko']
    search_fields = ['imie', 'nazwisko']
    ordering_fields = ['imie', 'nazwisko']


# ----------------------------------------------------------------------------------------------------------------------


class LokalizacjaList(generics.ListCreateAPIView):
    queryset = Lokalizacja.objects.all()
    serializer_class = LokalizacjaSerializer

    name = 'lokalizacja-list'
    filter_fields = ['szerokoscGeograficzna', 'dlugoscGeograficzna', 'ostatniaAktualizacja']
    search_fields = ['szerokoscGeograficzna', 'dlugoscGeograficzna', 'ostatniaAktualizacja']
    ordering_fields = ['ostatniaAktualizacja']


class LokalizacjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lokalizacja.objects.all()
    serializer_class = LokalizacjaSerializer

    name = 'lokalizacja-Detail'
    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


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
    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


# ----------------------------------------------------------------------------------------------------------------------


class PojazdyWDokachList(generics.ListCreateAPIView):
    queryset = PojazdyWDokach.objects.all()
    serializer_class = PojazdyWDokachSerializer

    name = 'pojazdy-w-dokach-list'
    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


class PojazdyWDokachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PojazdyWDokach.objects.all()
    serializer_class = PojazdyWDokachSerializer

    name = 'pojazdy-w-dokach-detail'
    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


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
    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


# ----------------------------------------------------------------------------------------------------------------------


class StawkaList(generics.ListCreateAPIView):
    queryset = Stawka.objects.all()
    serializer_class = StawkaSerializer

    name = 'stawka-list'
    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


class StawkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stawka.objects.all()
    serializer_class = StawkaSerializer

    name = 'stawka-detail'
    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


# ----------------------------------------------------------------------------------------------------------------------


class WypozyczeniaList(generics.ListCreateAPIView):
    queryset = Wypozyczenia.objects.all()
    serializer_class = WypozyczeniaSerializer

    name = 'wypozyczenia-list'
    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


class WypozyczeniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wypozyczenia.objects.all()
    serializer_class = WypozyczeniaSerializer

    name = 'wypozyczenia-detail'
    filter_fields = ['']
    search_fields = ['']
    ordering_fields = ['']


# ----------------------------------------------------------------------------------------------------------------------














# Widok Użytkowników:
class UserWidok(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # authentication_classes = [authentication.TokenAuthentication]   # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAdminUser]                  # Poziom dostępu: Admin

    def lista(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)

        return response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)

        return response(serializer.data)


# Widok Grup:
class GroupWidok(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAdminUser]                 # Poziom dostępu: Admin


# Widok Danych Osobowych:
class DaneOsoboweWidok(viewsets.ModelViewSet):
    queryset = DaneOsobowe.objects.all()
    serializer_class = DaneOsoboweSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticated]             # Poziom dostępu: Każdy zarejestrowany

    # def list(self, request): pass # Lista obiaktów z bazy danych

    # def create(self, request): pass  # Strorzenie obiektu w bazie danych

    # def retrieve(self, request, pk=None): pass # Konkretny obiekt z bazy danych

    # def update(self, request, pk=None): pass  # Aktualizacja obiektu z bazy danych

    # def partial_update(self, request, pk=None): pass  #

    # def destroy(self, request, pk=None): pass  # Usunięcie obiktu z bazy danych

    """
        Jeżeli [akcja] == list lub create to ma do niej dostęp tylko administrator.
        Do pozostałych ma dostęp każdy użytkownik.
    """
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]



class DokWidok(viewsets.ModelViewSet):
    queryset = Dok.objects.all()
    serializer_class = DokSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Poziom dostępu: Każdy zarejestrowany


class LokalizacjaWidok(viewsets.ModelViewSet):
    queryset = Lokalizacja.objects.all()
    serializer_class = LokalizacjaSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Poziom dostępu: Każdy zarejestrowany


class PojazdMiejskiWidok(viewsets.ModelViewSet):
    queryset = PojazdMiejski.objects.all()
    serializer_class = PojazdMiejskiSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Poziom dostępu: Każdy zarejestrowany


class PojazdyWDokachWidok(viewsets.ModelViewSet):
    queryset = PojazdyWDokach.objects.all()
    serializer_class = PojazdyWDokachSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Poziom dostępu: Każdy zarejestrowany


class RozliczenieWidok(viewsets.ModelViewSet):
    queryset = Rozliczenie.objects.all()
    serializer_class = RozliczenieSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticated]  # Poziom dostępu: Każdy zarejestrowany


class StawkaWidok(viewsets.ModelViewSet):
    queryset = Stawka.objects.all()
    serializer_class = StawkaSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAdminUser]  # Poziom dostępu: Każdy zarejestrowany


class WypozyczeniaWidok(viewsets.ModelViewSet):
    queryset = Wypozyczenia.objects.all()
    serializer_class = WypozyczeniaSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticated]  # Poziom dostępu: Każdy zarejestrowany


# Inny sposób na widoki:
"""
@csrf_exempt
def DaneOsobweLista(request):

    if request.method == 'GET':
        daneOsobowe = DaneOsobowe.objects.all()
        serializer = DaneOsoboweSerializer(daneOsobowe, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DaneOsoboweSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def DaneOsobweDetale(request, pk):
    try:
        daneOsobowe = DaneOsobowe.objects.get(pk=pk)
    except DaneOsobowe.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DaneOsoboweSerializer(daneOsobowe)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DaneOsoboweSerializer(daneOsobowe, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        daneOsobowe.delete()
        return HttpResponse(status=204)

@csrf_exempt
def DaneOsobweLista(request):

    if request.method == 'GET':
        daneOsobowe = DaneOsobowe.objects.all()
        serializer = DaneOsoboweSerializer(daneOsobowe, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DaneOsoboweSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def DaneOsobweDetale(request, pk):
    try:
        daneOsobowe = DaneOsobowe.objects.get(pk=pk)
    except DaneOsobowe.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DaneOsoboweSerializer(daneOsobowe)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DaneOsoboweSerializer(daneOsobowe, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        daneOsobowe.delete()
        return HttpResponse(status=204)


# https://youtu.be/DiSoVShaOLI

@api_view(['GET', ])
def WPMdaneOsoboweView(request, slug):

    try:
        dane_osobwe = DaneOsobowe.objects.get(slug=slug)

    except DaneOsobowe.DoesNotExist:
        return response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DaneOsoboweSerializer(dane_osobwe)
        return response(serializer.data)
"""