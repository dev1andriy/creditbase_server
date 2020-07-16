from django.db import models
from common.models.abstract import *


class AlertSeverity(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                    StatusRecordableModel, MakeableModel, CheckableModel):
    AlertSeverityId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AlertSeverityId, self.Description)

    class Meta:
        verbose_name = 'AlertSeverity'
        verbose_name_plural = 'AlertSeverity'
        db_table = 'AlertSeverity'
