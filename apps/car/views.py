from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CarSerializer
from .models import CarModel
# Create your views here.


class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()


class CarGetUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
