from django.urls import path, include
from . import views  # Import wszystkich widoków z 'views.py'.

"""
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'UserWidok', views.UserWidok)
# router.register(r'GroupWidok', views.GroupWidok)

router.register(r'DaneOsoboweWidok', views.DaneOsoboweList)
# router.register(r'DaneOsoboweWidok/<int:pk>', views.DaneOsoboweDetail)

router.register(r'DokWidok', views.DokList)
# router.register(r'DokWidok/<int:pk>', views.DokDetail)

router.register(r'LokalizacjaWidok', views.LokalizacjaList)
# router.register(r'LokalizacjaWidok/<int:pk>', views.LokalizacjaDetailList)

router.register(r'PojazdMiejskiWidok', views.PojazdMiejskiList)
# router.register(r'PojazdMiejskiWidok/<int:pk>', views.PojazdMiejskiDetail)

router.register(r'PojazdyWDokachWidok', views.PojazdyWDokachList)
# router.register(r'PojazdyWDokachWidok/<int:pk>', views.PojazdyWDokachDetail)

router.register(r'RozliczenieWidok', views.RozliczenieList)
# router.register(r'RozliczenieWidok/<int:pk>', views.RozliczenieDetail)

router.register(r'StawkaWidok', views.StawkaList)
# router.register(r'StawkaWidok/<int:pk>', views.StawkaDetail)

router.register(r'WypozyczeniaWidok', views.WypozyczeniaList)
# router.register(r'WypozyczeniaWidok/<int:pk>', views.WypozyczeniaDetail)
"""

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.APIRoot.as_view(), name=views.APIRoot.name),

    path('dane-osobowe', views.DaneOsoboweList.as_view(), name=views.DaneOsoboweList.name),
    path('dane-osobowe/<int:pk>', views.DaneOsoboweDetail.as_view(), name=views.DaneOsoboweDetail.name),

    path('aders-zamieszkania', views.AdresZamieszkaniaList.as_view(), name=views.AdresZamieszkaniaList.name),
    path('aders-zamieszkania/<int:pk>', views.AdresZamieszkaniaDetail.as_view(), name=views.AdresZamieszkaniaDetail.name),

    path('dok', views.DokList.as_view(), name=views.DokList.name),
    path('dok/<int:pk>', views.DokDetail.as_view(), name=views.DokDetail.name),

    path('lokalizacja', views.LokalizacjaList.as_view(), name=views.LokalizacjaList.name),
    path('lokalizacja/<int:pk>', views.LokalizacjaDetail.as_view(), name=views.LokalizacjaDetail.name),

    path('pojazd-miejski', views.PojazdMiejskiList.as_view(), name=views.PojazdMiejskiList.name),
    path('pojazd-miejski/<int:pk>', views.PojazdMiejskiDetail.as_view(), name=views.PojazdMiejskiDetail.name),

    path('pojazdy-w-dokach', views.PojazdWDokuList.as_view(), name=views.PojazdWDokuList.name),
    path('pojazdy-w-dokach/<int:pk>', views.PojazdWDokuDetail.as_view(), name=views.PojazdMiejskiDetail.name),

    path('rozliczenie', views.RozliczenieList.as_view(), name=views.RozliczenieList.name),
    path('rozliczenie/<int:pk>', views.RozliczenieDetail.as_view(), name=views.RozliczenieDetail.name),

    path('stawka', views.StawkaList.as_view(), name=views.StawkaList.name),
    path('stawka/<int:pk>', views.StawkaDetail.as_view(), name=views.StawkaDetail.name),

    path('wypozyczenia', views.WypozyczenieList.as_view(), name=views.WypozyczenieList.name),
    path('wypozyczenia/<int:pk>', views.WypozyczenieDetail.as_view(), name=views.WypozyczenieDetail.name),
]

"""
    # Widoki - @csrf_exempt i @api_view:

    # Adres : Widok - lista rekordów 'daneOsobwe'
    path('dane-osobowe/', views.dane_osobwe_list),

     # Adres : Widok - kontretny rekord z 'daneOsobowe'    
    path('dane-osobowe/<int:pk>', views.dane_osobwe_detale),    
"""

"""
    # Widoki - APIViews:

    # Adres : Widok - lista rekordów 'daneOsobwe'
    path('dane-osobowe/', views.DaneOsoboweListAPIView.as_view()),

    # Adres : Widok - kontretny rekord z 'daneOsobowe'
    path('dane-osobowe/<int:pk>', views.DaneOsoboweDetailAPIView.as_view()),
"""
