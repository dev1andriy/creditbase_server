from django.db import models
from common.models.abstract import *


class FinancialModel(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                     StatusRecordableModel, MakeableModel, CheckableModel):
    FinancialModelId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.FinancialModelId, self.Description)

    class Meta:
        verbose_name = 'FinancialModel'
        verbose_name_plural = 'FinancialModel'
        db_table = 'FinancialModel'
