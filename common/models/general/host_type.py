from django.db import models
from common.models.abstract import *


class HostType(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
               StatusRecordableModel, MakeableModel, CheckableModel):
    HostTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.HostTypeId, self.Description)

    class Meta:
        verbose_name = 'HostType'
        verbose_name_plural = 'HostType'
