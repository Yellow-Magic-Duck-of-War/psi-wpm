
# Komendy wpisywane w terminal:
"""
    pip install django - instalacja django

    pip install mysqlclient - instalacja mysqlclient (gdyby to było takie proste na Windowsie...)
"""

"""
    python manage.py makemigrations (nazwa aplikacji) - tworzy plik do zmigrowania modółów
                                                        jako tabel bazy danych (przynajmniej ja tak to rozumiem)
    
    python manage.py migrate - migracja wcześniej stworzonego pliku z modelami
"""

"""
    python manage.py createsuperuser - stworzenie superużytkownika
"""

"""
    python manage.py runserver - start serwera
    
    CTRL + PAUSE - wyłączenie serwera
"""

"""
    Groups:
    * Administraotrzy
    * Klienci
    
    Users: 
    * Login: superuser, Hasło: Rok2020Ssie
    * Login: administrator, Hasło: Kontrabanda69
    * Login: tester001, Hasło: Prochibicja20
"""

# Widoki:
"""
    Uprawnienia:
    * AllowAny - Wszyscy mają dostęp.
    * IsAuthenticated - Tylko zarejstrowani mają dostęp.
    * IsAdminUser - Tylko administratorzy mają dostel.
    * IsAuthenticatedOrReadOnly - Wszyscy czytają, zarejestrowani edytują.
    
"""