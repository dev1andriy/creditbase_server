from django.db import models
from common.models.abstract import *


class Suffix(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
             StatusRecordableModel, MakeableModel, CheckableModel):
    SuffixId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.SuffixId)

    class Meta:
        verbose_name = 'Suffix'
        verbose_name_plural = 'Suffix'
        db_table = 'Suffix'
