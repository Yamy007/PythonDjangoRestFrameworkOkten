from django.db import models
from core.models import CoreModel
from apps.auto_parks.models import AutoParkModel
from core.enum.validate import Validate
from django.core import validators as V
from datetime import datetime



class CarChoiceType(models.TextChoices):
    Hatchback = 'Hatchback',
    Sedan = 'Sedan',
    Coupe = 'Coupe',
    Jeep = 'Jeep'

    
class CarModel(CoreModel):
    
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20, validators=[V.RegexValidator(*Validate.BrandCar.value)])
    year = models.IntegerField(validators=[V.MinValueValidator(1900), V.MaxValueValidator(datetime.now().year)])
    typeCar = models.CharField(max_length=12, choices=CarChoiceType.choices)
    countPlace = models.IntegerField(validators=[V.MinValueValidator(2), V.MaxValueValidator(200)])
    eugenie = models.FloatField(validators=[V.MinValueValidator(2), V.MaxValueValidator(20)])
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')


