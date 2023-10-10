from django.db import models
from core.models import BaseModel
from apps.carPark.models import CarPark
# Create your models here.


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=25)
    typeCar = models.CharField(max_length=50)
    year = models.IntegerField()
    countPlace = models.IntegerField()
    eugenie = models.FloatField()
    park = models.ForeignKey(
        CarPark, on_delete=models.CASCADE, related_name='cars')
