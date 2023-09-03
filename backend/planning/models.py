from django.db import models
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
