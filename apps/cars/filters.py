from django_filters import rest_framework as filters
from .models import CarModel

class CarFilter(filters.FilterSet):
    # countPlaceGt = filters.NumberFilter()
    order = filters.OrderingFilter(
        fields = (
            'id',
            'brand',
            'year'
        )
    )
    class Meta:
        model = CarModel
        fields = {
            'year': ('lt', 'lte', 'gte', 'gt'),
            'countPlace': ('lt', 'lte', 'gte', 'gt'),
            'eugenie': ('lt', 'lte', 'gte', 'gt'),
            'brand': ('startswith', 'endswith', 'contains'),
            'typeCar': ('startswith', 'endswith', 'contains'),
            
        }

