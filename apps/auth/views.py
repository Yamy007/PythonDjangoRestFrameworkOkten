from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.users.serializers import UserSerializer
from django.contrib.auth import get_user_model

class GetMe(GenericAPIView):
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data , 200)
    
class GetAll(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    

    def get_queryset(self):
        return get_user_model().objects.all().exclude(id = self.request.user.id)
