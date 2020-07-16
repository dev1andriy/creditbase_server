from django.db import models


class StatusRecordableModel(models.Model):
    RecordStatus = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        abstract = True
