from django.db import models


class TimeStampedModel(models.Model):
    InsertDate = models.DateTimeField(null=True, blank=True)
    LastUpdatedDate = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
