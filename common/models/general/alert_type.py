from django.db import models
from common.models.abstract import *


class AlertType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                StatusRecordableModel, MakeableModel, CheckableModel):
    AlertTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AlertTypeId, self.Description)

    class Meta:
        verbose_name = 'AlertType'
        verbose_name_plural = 'AlertType'
        db_table = 'AlertType'
