from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer

class CreateUserProfile(CreateAPIView):
    serializer_class = UserSerializer