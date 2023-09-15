from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ShoppingListItem, TodoListItem, CleaningListItem, User
from .serializers import ShoppingListItemSerializer, TodoListItemSerializer, UserSerializer, CleaningListItemSerializer


# Create your views here.


class ShoppingListViewset(viewsets.ModelViewSet):

    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemSerializer


class TodoListViewset(viewsets.ModelViewSet):

    queryset = TodoListItem.objects.all()
    serializer_class = TodoListItemSerializer


class CleaningListViewset(viewsets.ModelViewSet):

    queryset = CleaningListItem.objects.all()
    serializer_class = CleaningListItemSerializer

    @action(detail=False, methods=['POST'])
    def delete_daily(self, request):
        CleaningListItemSerializer.clear_daily_items()
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def delete_weekly(self, request):
        CleaningListItemSerializer.clear_weekly_items()
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def delete_monthly(self, request):
        CleaningListItemSerializer.clear_monthly_items()
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['POST'])
    def add_tasks(self, request):
        CleaningListItemSerializer.add_tasks()
        return Response(status=status.HTTP_200_OK)
        
