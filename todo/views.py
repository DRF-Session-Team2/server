from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class TodoViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = TodoSerializer