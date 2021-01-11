
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
    * Login: superuser, Hasło: Rok2020Ssie
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