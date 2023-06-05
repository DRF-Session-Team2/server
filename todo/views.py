from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer