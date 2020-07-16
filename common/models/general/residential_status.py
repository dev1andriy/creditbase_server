from django.db import models
from common.models.abstract import *


class ResidentialStatus(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                        StatusRecordableModel, MakeableModel, CheckableModel):
    ResidentialStatusId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.ResidentialStatusId)

    class Meta:
        verbose_name = 'ResidentialStatus'
        verbose_name_plural = 'ResidentialStatus'
        db_table = 'ResidentialStatus'
