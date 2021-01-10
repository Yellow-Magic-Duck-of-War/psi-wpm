from django.urls import path, include
from . import views                      # Import wszystkich widoków z 'views.py'.
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

urlpatterns = [
    path('', include(router.urls)),
    # path('daneOsobowe/', views.daneOsoboweView, name='daneOsoboweView'),
    # path('daneOsoboweLista/', views.DaneOsobweLista, name='DaneOsoboweLista'),
    # path('daneOsoboweLista/<int:pk>', views.DaneOsobweDetale, name='DaneOsoboweDetale'),
]