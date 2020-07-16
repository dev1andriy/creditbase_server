from django.db import models


class HostValueFlagEditableModel(models.Model):
    EditHostValuesFlag = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        abstract = True
