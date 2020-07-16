from django.db import models
from common.models.abstract import *


class Currency(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
               StatusRecordableModel, MakeableModel, CheckableModel):
    CurrencyId = models.AutoField(primary_key=True, null=False)
    IsoCode1 = models.CharField(max_length=5, null=True, blank=True)
    IsoCode2 = models.IntegerField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.CurrencyId, self.Description)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currency'
        db_table = 'Currency'

