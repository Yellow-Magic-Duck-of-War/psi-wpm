from django.urls import path, include
from . import views                      # Import wszystkich widoków
from rest_framework import routers

router = routers.DefaultRouter()

router.register('UserWidok', views.UserWidok)
router.register('GroupWidok', views.GroupWidok)

router.register('DaneOsoboweWidok', views.DaneOsoboweWidok)
router.register('DokWidok', views.DokWidok)
router.register('LokalizacjaWidok', views.LokalizacjaWidok)
router.register('PojazdMiejskiWidok', views.PojazdMiejskiWidok)
router.register('PojazdyWDokachWidok', views.PojazdyWDokachWidok)
router.register('RozliczenieWidok', views.RozliczenieWidok)
router.register('StawkaWidok', views.StawkaWidok)
router.register('WypozyczeniaWidok', views.WypozyczeniaWidok)

urlpatterns = [
    path('', include(router.urls)),
    # path('daneOsobowe/', views.daneOsoboweView, name='daneOsoboweView'),
    # path('daneOsoboweLista/', views.DaneOsobweLista, name='DaneOsoboweLista'),
    # path('daneOsoboweLista/<int:pk>', views.DaneOsobweDetale, name='DaneOsoboweDetale'),
]