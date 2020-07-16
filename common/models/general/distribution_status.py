from django.db import models
from common.models.abstract import *


class DistributionStatus(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                         StatusRecordableModel, MakeableModel, CheckableModel):
    DistributionStatusId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.DistributionStatusId)

    class Meta:
        verbose_name = 'DistributionStatus'
        verbose_name_plural = 'DistributionStatus'
        db_table = 'DistributionStatus'
