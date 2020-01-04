from rest_framework import serializers

from . import models


class categorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.category
        fields = [
            "name",
        ]

class taskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.task
        fields = [
            "last_updated",
            "note",
            "done",
            "created",
            "priority",
            "name",
        ]
