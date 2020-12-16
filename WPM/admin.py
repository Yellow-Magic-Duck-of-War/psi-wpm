from django.contrib import admin
from .models import (DaneOsobowe, Wypozyczenia, PojazdMiejski, PojazdyWDokach, Dok,
                     Lokalizacja, Rozliczenie, Stawka)

# Register your models here.

# admin.site.register() - rejestracja modelów do panuelu admina (będa wydoczne w panelu admina)

admin.site.register(DaneOsobowe)
admin.site.register(Wypozyczenia)
admin.site.register(PojazdMiejski)
admin.site.register(PojazdyWDokach)
admin.site.register(Dok)
admin.site.register(Lokalizacja)
admin.site.register(Rozliczenie)
admin.site.register(Stawka)




