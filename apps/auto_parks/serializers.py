from rest_framework.serializers import ModelSerializer
from .models import AutoParkModel
from apps.cars.serializers import CarSerializersPreview

class AutoParkSerializer(ModelSerializer):
   cars = CarSerializersPreview(read_only=True, many=True)
   class Meta:
       model = AutoParkModel
       fields = ('id', 'name',  'cars','create_at', 'update_at')


class AutoParkSerializerPreview(ModelSerializer):
    class Meta:
       model = AutoParkModel
       fields = ('id', 'name')