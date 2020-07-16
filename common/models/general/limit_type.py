from django.db import models
from common.models.abstract import *


class LimitType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                StatusRecordableModel, MakeableModel, CheckableModel):
    LimitTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.LimitTypeId, self.Description)

    class Meta:
        verbose_name = 'LimitType'
        verbose_name_plural = 'LimitType'
        db_table = 'LimitType'

