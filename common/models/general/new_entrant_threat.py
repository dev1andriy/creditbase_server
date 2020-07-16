from django.db import models
from common.models.abstract import *


class NewEntrantThreat(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                       StatusRecordableModel, MakeableModel, CheckableModel):
    NewEntrantThreatId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.NewEntrantThreatId)

    class Meta:
        verbose_name = 'NewEntrantThreat'
        verbose_name_plural = 'NewEntrantThreat'
        db_table = 'NewEntrantThreat'
