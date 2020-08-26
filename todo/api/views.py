from api.models import Todo
from rest_framework import generics, status
from rest_framework import mixins
from rest_framework.response import Response

from .serializers import TodoSerializer, TodoCreateSerializer
from .utils import validate_user_id


class TodoListAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.filter(user_id=self.kwargs.get("user_id")).all()
        return queryset

    def get(self, request, *args, **kwargs):
        if not validate_user_id(kwargs.get("user_id")):
            return Response(data={"detail": "User ID does not exists"}, status=status.HTTP_404_NOT_FOUND)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not validate_user_id(kwargs.get("user_id")):
            return Response(data={"detail": "User ID does not exists"}, status=status.HTTP_404_NOT_FOUND)

        request.data._mutable = True
        request.data['user_id'] = kwargs.get("user_id")

        serializer = TodoCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TodoDetailAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, ):
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.filter(user_id=self.kwargs.get("user_id")).all()
        return queryset

    def get(self, request, *args, **kwargs):
        if not validate_user_id(kwargs.get("user_id")):
            return Response(data={"detail": "User ID does not exists"}, status=status.HTTP_404_NOT_FOUND)

        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if not validate_user_id(kwargs.get("user_id")):
            return Response(data={"detail": "User ID does not exists"}, status=status.HTTP_404_NOT_FOUND)

        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not validate_user_id(kwargs.get("user_id")):
            return Response(data={"detail": "User ID does not exists"}, status=status.HTTP_404_NOT_FOUND)

        instance = self.get_object()
        instance.active_status = False

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
