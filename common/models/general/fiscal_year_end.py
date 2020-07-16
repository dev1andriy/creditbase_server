from django.db import models
from common.models.abstract import *


class FiscalYearEnd(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                    StatusRecordableModel, MakeableModel, CheckableModel):
    FiscalYearEndId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.FiscalYearEndId, self.Description)

    class Meta:
        verbose_name = 'FiscalYearEnd'
        verbose_name_plural = 'FiscalYearEnd'
        db_table = 'FiscalYearEnd'
