from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializers import UserSerializers
from apps.carPark.serializers import CarParkSerializer
from .models import UserModel


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializers
    queryset = UserModel.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializers
    queryset = UserModel.objects.all()

    def post(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializers = CarParkSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save(user=user)
        return Response(serializers.data)
