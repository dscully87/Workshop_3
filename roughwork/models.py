from django.db import models
from django.db.models import QuerySet
from django.urls import reverse


class WorkshopQuerySet(QuerySet):
    def completed(self):
        return self.filter(complete=True)


class Workshop(models.Model):
    name = models.CharField(max_length=35)
    host = models.CharField(max_length=35)
    topic = models.TextField(help_text="Brief description of the topic described")
    complete = models.BooleanField(default=False)

    objects = WorkshopQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse("workshops:workshop-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
