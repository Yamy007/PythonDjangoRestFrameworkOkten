from rest_framework.serializers import ModelSerializer
from .models import UserModel
from apps.auto_parks.serializers import AutoParkSerializerPreview

class UserSerializer (ModelSerializer):
   auto_parks = AutoParkSerializerPreview(read_only=True, many=True)
   class Meta:
       model = UserModel
       fields = ('id', 'name', 'age', 'auto_parks')