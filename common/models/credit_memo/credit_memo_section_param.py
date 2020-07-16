from django.db import models

from common.models.abstract import *
from common.models.credit_memo import CreditMemoParam


class CreditMemoSectionParam(InsertableModel, UpdateableModel, TimeStampedModel, ViewableModel):
    CreditMemoSectionParamId = models.AutoField(primary_key=True, null=False)
    ParamId = models.ForeignKey(
        CreditMemoParam,
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=300)
    Setting1 = models.IntegerField(null=True, blank=True)
    Setting2 = models.IntegerField(null=True, blank=True)
    Setting3 = models.IntegerField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.CreditMemoSectionParamId)

    class Meta:
        verbose_name = 'CreditMemoSectionParam'
        verbose_name_plural = 'CreditMemoSectionParam'
        db_table = 'CreditMemoSectionParam'
