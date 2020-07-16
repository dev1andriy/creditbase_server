from django.db import models

from common.models.abstract import *
from common.models.general.financial_institution import FinancialInstitution


class BusinessUnit(TimeStampedModel, InsertableModel, DescribeableModel, HostableModel, CheckableModel, MakeableModel,
                   StatusRecordableModel):
    BusinessUnitId = models.IntegerField(primary_key=True)
    FinancialInstitution = models.ForeignKey(
        FinancialInstitution,
        on_delete=models.CASCADE,
        db_column='FinancialInstitution',
        default=None, blank=True, null=True
    )

    objects = models.Manager()

    def __str__(self):
        return "{} - {} - {}".format(self.BusinessUnitId, self.FinancialInstitution, self.Description)

    class Meta:
        verbose_name = 'BusinessUnit'
        verbose_name_plural = 'BusinessUnit'
        db_table = 'BusinessUnit'
