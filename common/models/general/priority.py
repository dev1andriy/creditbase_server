from django.db import models
from common.models.abstract import *


class Priority(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
               StatusRecordableModel, MakeableModel, CheckableModel):
    PriorityId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.PriorityId)

    class Meta:
        verbose_name = 'Priority'
        verbose_name_plural = 'Priority'
        db_table = 'Priority'
