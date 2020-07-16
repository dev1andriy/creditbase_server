from django.db import models
from common.models.abstract import *


class OperationalStatus(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                        StatusRecordableModel, MakeableModel, CheckableModel):
    OperationalStatusId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.OperationalStatusId, self.Description)

    class Meta:
        verbose_name = 'OperationalStatus'
        verbose_name_plural = 'OperationalStatus'
        db_table = 'OperationalStatus'
