from django.db import models
from common.models.abstract import *


class SupplierPower(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                    StatusRecordableModel, MakeableModel, CheckableModel):
    SupplierPowerId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.SupplierPowerId)

    class Meta:
        verbose_name = 'SupplierPower'
        verbose_name_plural = 'SupplierPower'
        db_table = 'SupplierPower'
