from django.db import models

from common.models.abstract import *


class FinancialInstitution(TimeStampedModel, InsertableModel, DescribeableModel, HostableModel, CheckableModel,
                           MakeableModel, StatusRecordableModel):
    FinancialInstitutionId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.FinancialInstitutionId, self.Description)

    class Meta:
        verbose_name = 'FinancialInstitution'
        verbose_name_plural = 'FinancialInstitution'
        db_table = 'FinancialInstitution'
