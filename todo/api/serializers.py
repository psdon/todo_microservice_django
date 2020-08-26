from api.models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'todo_status', 'active_status', 'date_added', 'date_updated']


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
