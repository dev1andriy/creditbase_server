from django.db import models
from common.models.general import AlertType
from common.models.abstract import *


class AlertSubType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                   StatusRecordableModel, MakeableModel, CheckableModel):
    AlertSubTypeId = models.AutoField(primary_key=True, null=False)
    AlertType = models.ForeignKey(
        AlertType,
        on_delete=models.CASCADE,
        null=False, blank=False
    )

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AlertSubTypeId, self.Description)

    class Meta:
        verbose_name = 'AlertSubType'
        verbose_name_plural = 'AlertSubType'
        db_table = 'AlertSubType'
