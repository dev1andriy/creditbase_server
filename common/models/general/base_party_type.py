from django.db import models

from common.models.abstract import *


class BasePartyType(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel, HostableModel,
                    CheckableModel, MakeableModel,
                    StatusRecordableModel):
    BasePartyTypeId = models.AutoField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.BasePartyTypeId, self.Description)

    class Meta:
        verbose_name = 'BasePartyType'
        verbose_name_plural = 'BasePartyType'
        db_table = 'BasePartyType'
