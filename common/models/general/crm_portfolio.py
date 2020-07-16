from django.db import models

from common.models.abstract import *


class CRMPortfolio(TimeStampedModel, InsertableModel, DescribeableModel, HostableModel, CheckableModel, MakeableModel,
                   StatusRecordableModel):
    CRMPortfolioId = models.IntegerField(primary_key=True)

    def __str__(self):
        return "{} - {}".format(self.CRMPortfolioId, self.Description)

    class Meta:
        verbose_name = 'CRMPortfolio'
        verbose_name_plural = 'CRMPortfolio'
        db_table = 'CRMPortfolio'
