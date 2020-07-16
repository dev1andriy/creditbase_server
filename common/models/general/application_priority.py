from django.db import models
from common.models.abstract import *


class ApplicationPriority(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                          StatusRecordableModel, MakeableModel, CheckableModel):
    ApplicationPriorityId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.ApplicationPriorityId)

    class Meta:
        verbose_name = 'ApplicationPriority'
        verbose_name_plural = 'ApplicationPriority'
        db_table = 'ApplicationPriority'
