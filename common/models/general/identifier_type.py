from django.db import models
from common.models.abstract import *


class IdentifierType(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                     HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    IdentifierTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.IdentifierTypeId, self.Description)

    class Meta:
        verbose_name = 'IdentifierType'
        verbose_name_plural = 'IdentifierType'
        db_table = 'IdentifierType'
