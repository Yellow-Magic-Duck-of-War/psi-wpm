
# Instalacja pakietów:

"""
    pip install django - instalacja django

    pip install mysqlclient - instalacja mysqlclient (gdyby to było takie proste na Windowsie...)
"""

# Migracja modeli do bazy danych:

"""
    python manage.py makemigrations (nazwa aplikacji) - tworzy plik do zmigrowania modółów
                                                        jako tabel bazy danych (przynajmniej ja tak to rozumiem)
    
    python manage.py migrate - migracja wcześniej stworzonego pliku z modelami
"""

# Superuser

"""
    python manage.py createsuperuser - stworzenie superużytkownika
"""

# Włączenie i wyłącznie serwera:

"""
    python manage.py runserver - start serwera
    
    CTRL + PAUSE - wyłączenie serwera
"""

# Użytkownicy:

"""
    Groups:
    * Administraotrzy
    * Klienci
    
    Users: 
    * Login: superusser, Hasło: Rok2020Ssie
    * Login: administrator, Hasło: Kontrabanda69
    * Login: tester001, Hasło: Prochibicja20
"""

# Widoki - Uprawnienia:
"""
    Uprawnienia:
    * AllowAny - Wszyscy mają dostęp.
    * IsAuthenticated - Tylko zarejstrowani mają dostęp.
    * IsAdminUser - Tylko administratorzy mają dostel.
    * IsAuthenticatedOrReadOnly - Wszyscy czytają, zarejestrowani edytują.
"""

"""
# Widoki modeli:

# Widok Użytkowników:
class UserWidok(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # authentication_classes = [authentication.TokenAuthentication]   # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAdminUser]                  # Poziom dostępu: Admin

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)


# ----------------------------------------------------------------------------------------------------------------------


# Widok Grup:
class GroupWidok(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAdminUser]                 # Poziom dostępu: Admin


# ----------------------------------------------------------------------------------------------------------------------


# Widok Danych Osobowych:
class DaneOsoboweWidok(viewsets.ModelViewSet):
    queryset = DaneOsobowe.objects.all()
    serializer_class = DaneOsoboweSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticated]             # Poziom dostępu: Każdy zarejestrowany

    # def list(self, request): pass                         # Lista obiaktów z bazy danych
    # def create(self, request): pass                       # Strorzenie obiektu w bazie danych
    # def retrieve(self, request, pk=None): pass            # Konkretny obiekt z bazy danych
    # def update(self, request, pk=None): pass              # Aktualizacja obiektu z bazy danych
    # def partial_update(self, request, pk=None): pass      #
    # def destroy(self, request, pk=None): pass             # Usunięcie obiktu z bazy danych

    # Jeżeli [akcja] == list lub create to ma do niej dostęp tylko administrator.
    # Do pozostałych ma dostęp każdy użytkownik.

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

# ----------------------------------------------------------------------------------------------------------------------


class DokWidok(viewsets.ModelViewSet):
    queryset = Dok.objects.all()
    serializer_class = DokSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Poziom dostępu: Każdy zarejestrowany


# ----------------------------------------------------------------------------------------------------------------------

class LokalizacjaWidok(viewsets.ModelViewSet):
    queryset = Lokalizacja.objects.all()
    serializer_class = LokalizacjaSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Poziom dostępu: Każdy zarejestrowany


# ----------------------------------------------------------------------------------------------------------------------

class PojazdMiejskiWidok(viewsets.ModelViewSet):
    queryset = PojazdMiejski.objects.all()
    serializer_class = PojazdMiejskiSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Poziom dostępu: Każdy zarejestrowany


# ----------------------------------------------------------------------------------------------------------------------

class PojazdyWDokachWidok(viewsets.ModelViewSet):
    queryset = PojazdyWDokach.objects.all()
    serializer_class = PojazdyWDokachSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Poziom dostępu: Każdy zarejestrowany


# ----------------------------------------------------------------------------------------------------------------------

class RozliczenieWidok(viewsets.ModelViewSet):
    queryset = Rozliczenie.objects.all()
    serializer_class = RozliczenieSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticated]  # Poziom dostępu: Każdy zarejestrowany


# ----------------------------------------------------------------------------------------------------------------------

class StawkaWidok(viewsets.ModelViewSet):
    queryset = Stawka.objects.all()
    serializer_class = StawkaSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAdminUser]  # Poziom dostępu: Każdy zarejestrowany


# ----------------------------------------------------------------------------------------------------------------------

class WypozyczeniaWidok(viewsets.ModelViewSet):
    queryset = Wypozyczenia.objects.all()
    serializer_class = WypozyczeniaSerializer

    # authentication_classes = [authentication.TokenAuthentication]  # Wymagany token rejestracji.
    # permission_classes = [permissions.IsAuthenticated]  # Poziom dostępu: Każdy zarejestrowany


# ----------------------------------------------------------------------------------------------------------------------"""

