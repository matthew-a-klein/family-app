from rest_framework import serializers, decorators
from .models import ShoppingListItem, TodoListItem, User, CleaningListItem
import json

class ShoppingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListItem
        fields = ['name', 'bought', 'id']


class TodoListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoListItem
        fields = ['name', 'completed', 'id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'longitude', 'latitude', 'id']
        extra_kwargs = {'password': {'write_only': True}}


class CleaningListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningListItem
        fields = ['name', 'completed', 'id', 'frequency']

    def clear_daily_items():
        CleaningListItem.objects.filter(frequency="D").delete()

    def clear_weekly_items():
        print("deleting weekly items")
        CleaningListItem.objects.filter(frequency="W").delete()

    def clear_monthly_items():
        CleaningListItem.objects.filter(frequency="M").delete()
        
    def add_tasks():
        with open('planning/cleaning_tasks.json',mode="r") as json_file:
            tasks = json.load(json_file)
            for task in tasks:
                CleaningListItem.objects.create(**task)
        
