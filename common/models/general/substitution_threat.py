from django.db import models
from common.models.abstract import *


class SubstitutionThreat(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                         StatusRecordableModel, MakeableModel, CheckableModel):
    SubstitutionThreatId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.SubstitutionThreatId)

    class Meta:
        verbose_name = 'SubstitutionThreat'
        verbose_name_plural = 'SubstitutionThreat'
        db_table = 'SubstitutionThreat'
