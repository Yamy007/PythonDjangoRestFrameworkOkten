from django.urls import path,include
from .views import ListAutoPark, RetrieveUpdateDestroyAutoPark

urlpatterns = [
    path('park', ListAutoPark.as_view()),
    path('park/<int:pk>', RetrieveUpdateDestroyAutoPark.as_view()),

]
