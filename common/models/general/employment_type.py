from django.db import models
from common.models.abstract import *


class EmploymentType(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                     StatusRecordableModel, MakeableModel, CheckableModel):
    EmploymentTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.EmploymentTypeId, self.Description)

    class Meta:
        verbose_name = 'EmploymentType'
        verbose_name_plural = 'EmploymentType'
        db_table = 'EmploymentType'


