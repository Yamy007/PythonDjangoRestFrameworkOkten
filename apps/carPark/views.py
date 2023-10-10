from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializers import CarParkSerializer
from apps.car.serializers import CarSerializer
from .models import CarPark
from apps.car.models import CarModel


class CarParkListCView(ListAPIView):
    serializer_class = CarParkSerializer
    queryset = CarPark.objects.all()


class CarParkRetrieveUpdateDestroyAddCarView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarParkSerializer
    queryset = CarPark.objects.all()

    def post(self, *args, **kwargs):
        park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(park=park)
        return Response(serializer.data)


class CarParkRetrieveListCar(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return CarModel.objects.filter(park_id=pk)
