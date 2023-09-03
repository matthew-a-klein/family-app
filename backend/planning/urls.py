from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'shoppinglist', views.ShoppingListViewset, 'shoppinglist')
router.register(r'todolist', views.TodoListViewset, 'todolist')

urlpatterns = [
    path('', include(router.urls))
]
