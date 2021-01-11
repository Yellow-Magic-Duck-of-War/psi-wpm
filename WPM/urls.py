from django.urls import path, include
from . import views                      # Import wszystkich widoków z 'views.py'.
"""
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'UserWidok', views.UserWidok)
router.register(r'GroupWidok', views.GroupWidok)

router.register(r'DaneOsoboweWidok', views.DaneOsoboweWidok)
router.register(r'DokWidok', views.DokWidok)
router.register(r'LokalizacjaWidok', views.LokalizacjaWidok)
router.register(r'PojazdMiejskiWidok', views.PojazdMiejskiWidok)
router.register(r'PojazdyWDokachWidok', views.PojazdyWDokachWidok)
router.register(r'RozliczenieWidok', views.RozliczenieWidok)
router.register(r'StawkaWidok', views.StawkaWidok)
router.register(r'WypozyczeniaWidok', views.WypozyczeniaWidok)
"""
urlpatterns = [
    # path('', include(router.urls)),
    path('',                            views.APIRoot.as_view(),                name=views.APIRoot.name),

    path('dane-osobowe',                views.DaneOsoboweList.as_view(),        name=views.APIRoot.name),
    path('dane-osobowe/<int:pk>',       views.DaneOsoboweDetail.as_view(),      name=views.APIRoot.name),

    path('dok',                         views.DokList.as_view(),                name=views.APIRoot.name),
    path('dok/<int:pk>',                views.DokDetail.as_view(),              name=views.APIRoot.name),

    path('lokalizacja',                 views.LokalizacjaList.as_view(),        name=views.APIRoot.name),
    path('lokalizacja/<int:pk>',        views.LokalizacjaDetail.as_view(),      name=views.APIRoot.name),

    path('pojazd-miejski',              views.PojazdMiejskiList.as_view(),      name=views.APIRoot.name),
    path('pojazd-miejski/<int:pk>',     views.PojazdMiejskiDetail.as_view(),    name=views.APIRoot.name),

    path('pojazdy-w-dokach',            views.PojazdyWDokachList.as_view(),     name=views.APIRoot.name),
    path('pojazdy-w-dokach/<int:pk>',   views.PojazdyWDokachDetail.as_view(),   name=views.APIRoot.name),

    path('rozliczenie',                 views.RozliczenieList.as_view(),        name=views.APIRoot.name),
    path('rozliczenie/<int:pk>',        views.RozliczenieDetail.as_view(),      name=views.APIRoot.name),

    path('stawka',                      views.StawkaList.as_view(),             name=views.APIRoot.name),
    path('stawka/<int:pk>',             views.StawkaDetail.as_view(),           name=views.APIRoot.name),

    path('wypozyczenia',                views.WypozyczeniaList.as_view(),       name=views.APIRoot.name),
    path('wypozyczenia/<int:pk>',       views.WypozyczeniaDetail.as_view(),     name=views.APIRoot.name),
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