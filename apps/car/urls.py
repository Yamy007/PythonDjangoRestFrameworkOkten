from django.urls import path
from .views import *
urlpatterns = [
    path('api', CarListCreateView.as_view()),
    path('api/<int:pk>', CarGetUpdateRetrieveDestroyView.as_view()),
]
