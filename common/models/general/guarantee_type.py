from django.db import models
from common.models.abstract import *


class GuaranteeType(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                    StatusRecordableModel, MakeableModel, CheckableModel):
    GuaranteeTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.GuaranteeTypeId, self.Description)

    class Meta:
        verbose_name = 'GuaranteeType'
        verbose_name_plural = 'GuaranteeType'
        db_table = 'GuaranteeType'
