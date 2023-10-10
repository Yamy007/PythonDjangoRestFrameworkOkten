from rest_framework.serializers import ModelSerializer
from .models import CarPark
from apps.car.serializers import CarSerializer


class CarParkSerializer(ModelSerializer):
    cars = CarSerializer(read_only=True, many=True)

    class Meta:
        model = CarPark
        fields = ('id', 'name', 'cars', 'create_at', 'update_at')


class CarParkByUserSerializer(ModelSerializer):

    class Meta:
        model = CarPark
        fields = ('id', 'name',  'create_at', 'update_at')
