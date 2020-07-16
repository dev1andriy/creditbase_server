from django.db import models
from common.models.abstract import *


class ApplicationSource(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                        StatusRecordableModel, MakeableModel, CheckableModel):
    ApplicationSourceId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.ApplicationSourceId)

    class Meta:
        verbose_name = 'ApplicationSource'
        verbose_name_plural = 'ApplicationSource'
        db_table = 'ApplicationSource'
