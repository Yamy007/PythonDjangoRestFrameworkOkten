from rest_framework.serializers import ModelSerializer
from .models import UserModel
from apps.carPark.serializers import CarParkByUserSerializer


class UserSerializers(ModelSerializer):

    park = CarParkByUserSerializer(read_only=True, many=True)

    class Meta:
        model = UserModel
        fields = ('id', 'name', 'age', 'park', 'create_at', 'update_at')
