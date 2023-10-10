from django.db import models
from core.models import BaseModel
from apps.user.models import UserModel


class CarPark(BaseModel):
    class Meta:
        db_table = 'park'
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name='park')
