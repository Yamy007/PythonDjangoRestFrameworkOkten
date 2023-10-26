from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CarSerializers
from .models import CarModel
from core.pagination import CustomPagination
from .filters import CarFilter
from rest_framework.permissions import IsAuthenticated
class ListCar(ListAPIView):
    serializer_class = CarSerializers
    queryset = CarModel.objects.all()
    pagination_class = CustomPagination
    filterset_class = CarFilter
    permission_classes = (IsAuthenticated, )

class RetrieveUpdateDestroyCar(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializers
    queryset = CarModel.objects.all()