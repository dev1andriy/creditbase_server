from django.db import models

from common.models.abstract import *
from common.models.credit_memo import CreditMemo


class CreditMemoParam(InsertableModel, UpdateableModel, TimeStampedModel, ViewableModel):
    ParamId = models.AutoField(primary_key=True, null=False)
    CreditMemoId = models.ForeignKey(
        CreditMemo,
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
        return "{} - {}".format(self.CreditMemoId, self.ParamId)

    class Meta:
        verbose_name = 'CreditMemoParam'
        verbose_name_plural = 'CreditMemoParam'
        db_table = 'CreditMemoParam'
