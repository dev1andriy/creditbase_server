from django.db import models
from common.models.abstract import *


class Purpose(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
              StatusRecordableModel, MakeableModel, CheckableModel):
    PurposeId = models.AutoField(primary_key=True, null=False)
    PurposeLevel = models.IntegerField(default=1, blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.PurposeId)

    class Meta:
        verbose_name = 'Purpose'
        verbose_name_plural = 'Purpose'
        db_table = 'Purpose'
