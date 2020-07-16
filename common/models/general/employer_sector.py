from django.db import models
from common.models.abstract import *


class EmployerSector(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                     HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    EmployerSectorId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.EmployerSectorId, self.Description)

    class Meta:
        verbose_name = 'EmployerSector'
        verbose_name_plural = 'EmployerSector'
        db_table = 'EmployerSector'
