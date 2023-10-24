from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CarSerializers
from .models import CarModel
from core.pagination import CustomPagination
from .filters import CarFilter

class ListCar(ListAPIView):
    serializer_class = CarSerializers
    queryset = CarModel.objects.all()
    pagination_class = CustomPagination
    filterset_class = CarFilter

class RetrieveUpdateDestroyCar(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializers
    queryset = CarModel.objects.all()