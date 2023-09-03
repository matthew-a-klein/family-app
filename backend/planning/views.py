from rest_framework import viewsets
from .models import ShoppingListItem, TodoListItem
from .serializers import ShoppingListItemSerializer, TodoListItemSerializer
from rest_framework import response, status

# Create your views here.


class ShoppingListViewset(viewsets.ModelViewSet):

    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemSerializer


class TodoListViewset(viewsets.ModelViewSet):

    queryset = TodoListItem.objects.all()
    serializer_class = TodoListItemSerializer
