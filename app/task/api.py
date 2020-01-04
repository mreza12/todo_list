from rest_framework import viewsets, permissions

from . import serializers
from . import models


class categoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the category class"""

    queryset = models.category.objects.all()
    serializer_class = serializers.categorySerializer
    permission_classes = [permissions.IsAuthenticated]


class taskViewSet(viewsets.ModelViewSet):
    """ViewSet for the task class"""

    queryset = models.task.objects.all()
    serializer_class = serializers.taskSerializer
    permission_classes = [permissions.IsAuthenticated]
