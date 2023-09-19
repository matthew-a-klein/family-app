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
        
    @classmethod
    def clear_daily_tasks(cls):
        CleaningListItem.objects.filter(frequency="D").delete()
    @classmethod
    def clear_weekly_tasks(cls):
        print("deleting weekly items")
        CleaningListItem.objects.filter(frequency="W").delete()
    @classmethod
    def clear_monthly_tasks(cls):
        CleaningListItem.objects.filter(frequency="M").delete()
    @classmethod   
    def add_daily_tasks(cls):
        with open('planning/cleaning_tasks/daily_cleaning_tasks.json',mode="r") as json_file:
            tasks = json.load(json_file)
            for task in tasks:
                CleaningListItem.objects.create(**task)
    @classmethod           
    def add_weekly_tasks(cls):
        with open('planning/cleaning_tasks/weekly_cleaning_tasks.json',mode="r") as json_file:
            tasks = json.load(json_file)
            for task in tasks:
                CleaningListItem.objects.create(**task)
    @classmethod
    def add_monthly_tasks(cls):
        with open('planning/cleaning_tasks/monthly_cleaning_tasks.json',mode="r") as json_file:
            tasks = json.load(json_file)
            for task in tasks:
                CleaningListItem.objects.create(**task)
    @classmethod            
    def refresh_daily_tasks(cls):
        cls.clear_daily_tasks()
        cls.add_daily_tasks()
        
    @classmethod            
    def refresh_weekly_tasks(cls):
        cls.clear_weekly_tasks()
        cls.add_weekly_tasks()
    @classmethod            
    def refresh_monthly_tasks(cls):
        cls.clear_monthly_tasks()
        cls.add_monthly_tasks()
   
        
        
