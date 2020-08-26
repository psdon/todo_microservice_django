from api.models import Todo
from rest_framework import generics, status
from rest_framework import mixins
from rest_framework.response import Response

from .serializers import TodoSerializer, TodoCreateSerializer


class TodoListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,
                      generics.GenericAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.filter(user_id=self.kwargs.get("user_id")).all()
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
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
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
