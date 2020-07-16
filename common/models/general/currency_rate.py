from django.db import models
from common.models.abstract import *
from common.models.general import Currency


class CurrencyRate(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                   StatusRecordableModel, MakeableModel, CheckableModel):
    CurrencyRateId = models.AutoField(primary_key=True, null=False)
    CurrencyIn = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE, related_name='CurrencyIn')
    CurrencyOut = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE, related_name='CurrencyOut')
    ExchangeRate = models.FloatField(null=True, blank=True)
    RateDate = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}:{}".format(self.CurrencyRateId, self.CurrencyIn, self.CurrencyOut)

    class Meta:
        verbose_name = 'CurrencyRate'
        verbose_name_plural = 'CurrencyRate'
        db_table = 'CurrencyRate'

