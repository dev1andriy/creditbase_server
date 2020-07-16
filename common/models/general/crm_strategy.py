from django.db import models

from common.models.abstract import *


class CRMStrategy(TimeStampedModel, InsertableModel, DescribeableModel, HostableModel, CheckableModel, MakeableModel,
                  StatusRecordableModel):
    CRMStrategyId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.CRMStrategyId, self.Description)

    class Meta:
        verbose_name = 'CRMStrategy'
        verbose_name_plural = 'CRMStrategy'
        db_table = 'CRMStrategy'
