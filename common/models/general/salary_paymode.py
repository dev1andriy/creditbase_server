from django.db import models
from common.models.abstract import *


class SalaryPayMode(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                    HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    SalaryPayModeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.SalaryPayModeId, self.Description)

    class Meta:
        verbose_name = 'SalaryPayMode'
        verbose_name_plural = 'SalaryPayMode'
        db_table = 'SalaryPayMode'
