from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .serializers import UserSerializer

# Create your views here.

User = get_user_model()

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name']
