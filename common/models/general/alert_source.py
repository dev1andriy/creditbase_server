from django.db import models
from common.models.abstract import *


class AlertSource(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                  StatusRecordableModel, MakeableModel, CheckableModel):
    AlertSourceId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AlertSourceId, self.Description)

    class Meta:
        verbose_name = 'AlertSource'
        verbose_name_plural = 'AlertSource'
        db_table = 'AlertSource'
