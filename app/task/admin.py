from django.contrib import admin
from django import forms

from . import models


class categoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.category
        fields = "__all__"


class categoryAdmin(admin.ModelAdmin):
    form = categoryAdminForm
    list_display = [
        "name",
    ]
    readonly_fields = [
        "name",
    ]


class taskAdminForm(forms.ModelForm):

    class Meta:
        model = models.task
        fields = "__all__"


class taskAdmin(admin.ModelAdmin):
    form = taskAdminForm
    list_display = [
        "last_updated",
        "note",
        "done",
        "created",
        "priority",
        "name",
    ]
    readonly_fields = [
        "last_updated",
        "note",
        "done",
        "created",
        "priority",
        "name",
    ]


admin.site.register(models.category, categoryAdmin)
admin.site.register(models.task, taskAdmin)
