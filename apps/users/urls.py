from django.urls import path,include
from .views import ListCreateUser, RetrieveUpdateDestroyUser

urlpatterns = [
    path('user', ListCreateUser.as_view()),
    path('user/<int:pk>', RetrieveUpdateDestroyUser.as_view()),

]
