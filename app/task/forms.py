from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit



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
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'

