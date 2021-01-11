"""WPMProjekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from WPM import views

urlpatterns = [
    path('admin/', admin.site.urls),    # Strona administratora.
    path('', include('WPM.urls')),      # Import wszystkich url z API.

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
]
