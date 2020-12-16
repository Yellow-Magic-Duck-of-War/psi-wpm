from django.urls import path
from . import views             # Import wszystkich widoków

urlpatterns = [
    path('', views.daneOsoboweView, name='daneOsoboweView'),
]