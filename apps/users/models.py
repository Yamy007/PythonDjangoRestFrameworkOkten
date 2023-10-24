from django.db import models
from core.models import CoreModel
from core.enum.validate import Validate
from django.core import validators as V


class UserModel(CoreModel):
    class Meta:
        db_table = 'users'
    name = models.CharField(max_length=30, validators=[V.RegexValidator(*Validate.NameUser.value)])
    age = models.IntegerField(validators=[V.MinValueValidator(18), V.MaxValueValidator(65)])
    