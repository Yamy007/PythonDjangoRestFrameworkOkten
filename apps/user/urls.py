from django.urls import path
from .views import *
urlpatterns = [
    path('api', UserListCreateView.as_view()),
    path('api/<int:pk>', UserRetrieveUpdateDestroyView.as_view())
]
