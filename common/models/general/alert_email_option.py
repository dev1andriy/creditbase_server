from django.db import models
from common.models.abstract import *


class AlertEmailOption(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                       StatusRecordableModel, MakeableModel, CheckableModel):
    AlertEmailOptionId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AlertEmailOptionId, self.Description)

    class Meta:
        verbose_name = 'AlertEmailOption'
        verbose_name_plural = 'AlertEmailOption'
        db_table = 'AlertEmailOption'
