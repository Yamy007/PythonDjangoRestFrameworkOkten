from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializers
from .models import AutoParkModel


class ListAutoPark(ListAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()

class RetrieveUpdateDestroyAutoPark(RetrieveUpdateDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        return Response(serializer.data, 201)
        