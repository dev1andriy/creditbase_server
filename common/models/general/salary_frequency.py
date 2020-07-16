from django.db import models
from common.models.abstract import *


class SalaryFrequency(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                      HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    SalaryFrequencyId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.SalaryFrequencyId, self.Description)

    class Meta:
        verbose_name = 'SalaryFrequency'
        verbose_name_plural = 'SalaryFrequency'
        db_table = 'SalaryFrequency'
