from django.db import models
from common.models.abstract import *


class AlertStatus(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                  StatusRecordableModel, MakeableModel, CheckableModel):
    AlertStatusId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AlertStatusId, self.Description)

    class Meta:
        verbose_name = 'AlertStatus'
        verbose_name_plural = 'AlertStatus'
        db_table = 'AlertStatus'
