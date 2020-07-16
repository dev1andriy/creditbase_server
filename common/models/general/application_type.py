from django.db import models
from common.models.abstract import *


class ApplicationType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                      StatusRecordableModel, MakeableModel, CheckableModel):
    ApplicationTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.ApplicationTypeId)

    class Meta:
        verbose_name = 'ApplicationType'
        verbose_name_plural = 'ApplicationType'
        db_table = 'ApplicationType'
