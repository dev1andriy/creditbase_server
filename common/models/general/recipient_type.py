from django.db import models
from common.models.abstract import *


class RecipientType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                    StatusRecordableModel, MakeableModel, CheckableModel):
    RecipientTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.RecipientTypeId)

    class Meta:
        verbose_name = 'RecipientType'
        verbose_name_plural = 'RecipientType'
        db_table = 'RecipientType'
