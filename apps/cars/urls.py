from django.urls import path
from .views import ListCar , RetrieveUpdateDestroyCar

urlpatterns = [
    path('cars', ListCar.as_view()),
    path('cars/<int:pk>', RetrieveUpdateDestroyCar.as_view())
]
