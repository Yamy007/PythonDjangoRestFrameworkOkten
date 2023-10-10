from django.urls import path
from .views import *
urlpatterns = [
    path('api', CarParkListCView.as_view()),
    path('api/<int:pk>', CarParkRetrieveUpdateDestroyAddCarView.as_view()),
    path('api/<int:pk>/car', CarParkRetrieveListCar.as_view()),
]
