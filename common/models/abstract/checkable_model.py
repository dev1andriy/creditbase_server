from django.db import models


class CheckableModel(models.Model):
    CheckerId = models.IntegerField(default=None, blank=True, null=True)
    CheckDate = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        abstract = True
