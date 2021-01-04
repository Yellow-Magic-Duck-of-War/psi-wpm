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

from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import  permissions
from WPM.models import DaneOsobowe, Dok, Lokalizacja, PojazdMiejski, PojazdyWDokach, Rozliczenie, Stawka, Wypozyczenia
from WPM.serializers import DaneOsoboweSerializer, DokSerializer, LokalizacjaSerializer, PojazdMiejskiSerializer,\
                            PojazdyWDokachSerializer, RozliczenieSerializer, StawkaSerializer, WypozyczeniaSerializer,\
                            UserSerializer, GroupSerializer


class UserWidok(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupWidok(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class DaneOsoboweWidok(viewsets.ModelViewSet):
    queryset = DaneOsobowe.objects.all()
    serializer_class = DaneOsoboweSerializer
    # permission_classes = [permissions.IsAuthenticated]


class DokWidok(viewsets.ModelViewSet):
    queryset = Dok.objects.all()
    serializer_class = DokSerializer


class LokalizacjaWidok(viewsets.ModelViewSet):
    queryset = Lokalizacja.objects.all()
    serializer_class = LokalizacjaSerializer


class PojazdMiejskiWidok(viewsets.ModelViewSet):
    queryset = PojazdMiejski.objects.all()
    serializer_class = PojazdMiejskiSerializer


class PojazdyWDokachWidok(viewsets.ModelViewSet):
    queryset = PojazdyWDokach.objects.all()
    serializer_class = PojazdyWDokachSerializer


class RozliczenieWidok(viewsets.ModelViewSet):
    queryset = Rozliczenie.objects.all()
    serializer_class = RozliczenieSerializer


class StawkaWidok(viewsets.ModelViewSet):
    queryset = Stawka.objects.all()
    serializer_class = StawkaSerializer


class WypozyczeniaWidok(viewsets.ModelViewSet):
    queryset = Wypozyczenia.objects.all()
    serializer_class = WypozyczeniaSerializer

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