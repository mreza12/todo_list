from django import forms
from . import models


class categoryForm(forms.ModelForm):
    class Meta:
        model = models.category
        fields = [
            "name",
        ]


class taskForm(forms.ModelForm):
    class Meta:
        model = models.task
        fields = [
            "name",
            "priority",
            "category",
            "note",
            "done",
        ]

