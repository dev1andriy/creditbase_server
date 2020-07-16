from django.db import models
from common.models.abstract import *


class EmployerType(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                   StatusRecordableModel, MakeableModel, CheckableModel):
    EmployerTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.EmployerTypeId, self.Description)

    class Meta:
        verbose_name = 'EmployerType'
        verbose_name_plural = 'EmployerType'
        db_table = 'EmployerType'


