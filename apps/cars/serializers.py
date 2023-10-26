from rest_framework.serializers import ModelSerializer
from .models import CarModel


class CarSerializers(ModelSerializer):
   class Meta:
       model = CarModel
       fields = ('id', 'brand', 'year', 'type_car', 'count_place', 'eugenie', 'create_at', 'update_at')


class CarSerializersPreview(ModelSerializer):
   class Meta:
       model = CarModel
       fields = ('id', 'brand', 'year', 'type_car')

