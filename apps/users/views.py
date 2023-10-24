from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializers import UserSerializer
from apps.auto_parks.serializers import AutoParkSerializer
from .models import UserModel


class ListCreateUser(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

class RetrieveUpdateDestroyUser(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def post(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializer = AutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, 201)
        