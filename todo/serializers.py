from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo 
        fields = ('url', 'id', 'title', 'created', 'due_date')