from django.db import models
from common.models.abstract import *


class TelephoneType(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                    StatusRecordableModel, MakeableModel, CheckableModel):
    TelephoneTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.TelephoneTypeId, self.Description)

    class Meta:
        verbose_name = 'TelephoneType'
        verbose_name_plural = 'TelephoneType'
        db_table = 'TelephoneType'
