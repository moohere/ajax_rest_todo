from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', views.TodoView)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
]