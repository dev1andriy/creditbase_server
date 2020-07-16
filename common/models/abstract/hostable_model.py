from django.db import models


class HostableModel(models.Model):
    IdHost = models.CharField(max_length=20, default=None, blank=True, null=True)

    class Meta:
        abstract = True
