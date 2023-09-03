from rest_framework import serializers
from .models import ShoppingListItem, TodoListItem


class ShoppingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListItem
        fields = ['name', 'bought', 'id']


class TodoListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoListItem
        fields = ['name', 'completed', 'id']
