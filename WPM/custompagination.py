from rest_framework.pagination import LimitOffsetPagination


# 'limit=' - maksymalna liczba wyświetlanych elementów.
# 'offset=' - od którego miejsca wyświetlamy elementy.


class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
    max_limit = 5
