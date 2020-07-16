from django.db import models
from common.models.abstract import *


class BuyerPower(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                 StatusRecordableModel, MakeableModel, CheckableModel):
    BuyerPowerId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return '{} - {}'.format(self.BuyerPowerId, self.Description)

    class Meta:
        verbose_name = 'BuyerPower'
        verbose_name_plural = 'BuyerPower'
        db_table = 'BuyerPower'

