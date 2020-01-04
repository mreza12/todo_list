from django.views import generic
from . import models
from . import forms


class categoryListView(generic.ListView):
    model = models.category
    form_class = forms.categoryForm


class categoryCreateView(generic.CreateView):
    model = models.category
    form_class = forms.categoryForm


class categoryDetailView(generic.DetailView):
    model = models.category
    form_class = forms.categoryForm


class categoryUpdateView(generic.UpdateView):
    model = models.category
    form_class = forms.categoryForm
    pk_url_kwarg = "pk"


class taskListView(generic.ListView):
    model = models.task
    form_class = forms.taskForm


class taskCreateView(generic.CreateView):
    model = models.task
    form_class = forms.taskForm


class taskDetailView(generic.DetailView):
    model = models.task
    form_class = forms.taskForm


class taskUpdateView(generic.UpdateView):
    model = models.task
    form_class = forms.taskForm
    pk_url_kwarg = "pk"
