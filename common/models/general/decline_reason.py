from django.db import models
from common.models.abstract import *


class DeclineReason(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                    StatusRecordableModel, MakeableModel, CheckableModel):
    DeclineReasonId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.DeclineReasonId)

    class Meta:
        verbose_name = 'DeclineReason'
        verbose_name_plural = 'DeclineReason'
        db_table = 'DeclineReason'
