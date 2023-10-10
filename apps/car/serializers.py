from rest_framework.serializers import ModelSerializer
from .models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'typeCar', 'year', 'countPlace',
                  'eugenie', 'create_at', 'update_at')
