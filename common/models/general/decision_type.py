from django.db import models
from common.models.abstract import *


class DecisionType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                   StatusRecordableModel, MakeableModel, CheckableModel):
    DecisionTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.DecisionTypeId)

    class Meta:
        verbose_name = 'DecisionType'
        verbose_name_plural = 'DecisionType'
        db_table = 'DecisionType'
