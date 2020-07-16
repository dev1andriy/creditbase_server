from django.db import models
from common.models.abstract import *


class Flag(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
           StatusRecordableModel, MakeableModel, CheckableModel):
    FlagId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.FlagId, self.Description)

    class Meta:
        verbose_name = 'Flag'
        verbose_name_plural = 'Flag'
        db_table = 'Flag'
