from django.db import models
from common.models.abstract import *


class PreferenceType(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                     HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    PreferenceTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.PreferenceTypeId, self.Description)

    class Meta:
        verbose_name = 'PreferenceType'
        verbose_name_plural = 'PreferenceType'
        db_table = 'PreferenceType'
