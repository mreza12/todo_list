from django.db import models
from django.urls import reverse


class category(models.Model):

    #  Fields
    name = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("task_category_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("task_category_update", args=(self.pk,))


class task(models.Model):

    #  Relationships
    category = models.ForeignKey("category", on_delete=models.CASCADE)

    #  Fields
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    note = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    priority = models.CharField(max_length=15,choices=[('Urgent','Urgent'),('Important','Important'),('Low','Low')])
    done = models.BooleanField(default=False,blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("task_task_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("task_task_update", args=(self.pk,))
