from django.db import models
from common.models.abstract import *


class CompetitiveRivalry(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                         StatusRecordableModel, MakeableModel, CheckableModel):
    CompetitiveRivalryId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.CompetitiveRivalryId)

    class Meta:
        verbose_name = 'CompetitiveRivalry'
        verbose_name_plural = 'CompetitiveRivalry'
        db_table = 'CompetitiveRivalry'
