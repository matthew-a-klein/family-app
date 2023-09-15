from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.


class ShoppingListItem(models.Model):
    name = models.TextField(max_length=40, blank=False)
    bought = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class TodoListItem(models.Model):
    name = models.TextField(max_length=40, blank=False)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class User(User):

    longitude = models.DecimalField(
        blank=True, decimal_places=8, max_digits=11)
    latitude = models.DecimalField(blank=True, decimal_places=8, max_digits=11)


class CleaningListItem(models.Model):
    class Frequency(models.TextChoices):
        DAILY = "D"
        WEEKLY = "W"
        MONTHLY = "M"
    name = models.TextField(max_length=40, blank=False)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    frequency = models.CharField(
        max_length=1, choices=Frequency.choices, blank=True)

    def __str__(self):
        return self.name
