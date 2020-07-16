from django.db import models


class MakeableModel(models.Model):
    MakerId = models.IntegerField(default=None, blank=True, null=True)
    MakeDate = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        abstract = True
