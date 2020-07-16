from django.db import models
from common.models.abstract import *


class Prefix(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
             StatusRecordableModel, MakeableModel, CheckableModel):
    PrefixId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.PrefixId)

    class Meta:
        verbose_name = 'Prefix'
        verbose_name_plural = 'Prefix'
        db_table = 'Prefix'
