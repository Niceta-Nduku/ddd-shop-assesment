from django_filters import FilterSet, NumberFilter
from .models import Sales

class adminSalesFitler(FilterSet):
    """
    Filter sales by date
    """
    day = django_filters.NumberFilter(name='date', lookup_expr='day')
    month = django_filters.NumberFilter(name='date', lookup_expr='month')
    year = django_filters.NumberFilter(name='date', lookup_expr='year')
    class Meta:
        model = Sales
        field = ['date']