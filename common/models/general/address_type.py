from django.db import models
from common.models.abstract import *


class AddressType(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                  HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    AddressTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AddressTypeId, self.Description)

    class Meta:
        verbose_name = 'AddressType'
        verbose_name_plural = 'AddressType'
        db_table = 'AddressType'
