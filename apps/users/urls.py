from django.urls import path
from .views import CreateUserProfile
urlpatterns = [
    path('user/create', CreateUserProfile.as_view()),

]
