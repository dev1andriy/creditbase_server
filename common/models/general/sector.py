from django.db import models
from common.models.abstract import *


class Sector(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
             StatusRecordableModel, MakeableModel, CheckableModel):
    SectorId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.SectorId, self.Description)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sector'
        db_table = 'Sector'
