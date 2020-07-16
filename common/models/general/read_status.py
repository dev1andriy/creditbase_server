from django.db import models
from common.models.abstract import *


class ReadStatus(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                 StatusRecordableModel, MakeableModel, CheckableModel):
    ReadStatusId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.ReadStatusId)

    class Meta:
        verbose_name = 'ReadStatus'
        verbose_name_plural = 'ReadStatus'
        db_table = 'ReadStatus'
