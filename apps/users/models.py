from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import CoreModel 
from .manager import UserManager
from django.core import validators 
from core.enum.validate import Validate 
class UserProfileModel(CoreModel):
    class Meta:
        db_table = 'user_profile'
    name = models.CharField(max_length=25, validators=[validators.RegexValidator(*Validate.NameUser.value)]) 
    surname = models.CharField(max_length=25, validators=[validators.RegexValidator(*Validate.NameUser.value)])
    age = models.IntegerField(validators=[validators.MinValueValidator(18), validators.MaxValueValidator(100)])

class UserModel(AbstractBaseUser, PermissionsMixin, CoreModel):
    class Meta:
        db_table = 'auth_user'
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    profile = models.OneToOneField(UserProfileModel, on_delete=models.CASCADE, related_name='user', null=True )    

    USERNAME_FIELD = 'email'

    objects = UserManager() 