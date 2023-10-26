from django.db import models
from core.models import CoreModel
from core.enum.validate import Validate
from django.core import validators as V

class AutoParkModel(CoreModel):
    class Meta:
        db_table = 'auto_parks'
    name = models.CharField(max_length=30, validators=[V.RegexValidator(Validate.NameAutoPark.pattern, Validate.NameAutoPark.message)])
    
