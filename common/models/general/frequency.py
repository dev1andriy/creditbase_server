from django.db import models
from common.models.abstract import *


class Frequency(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                StatusRecordableModel, MakeableModel, CheckableModel):
    FrequencyId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.FrequencyId, self.Description)

    class Meta:
        verbose_name = 'Frequency'
        verbose_name_plural = 'Frequency'
        db_table = 'Frequency'
