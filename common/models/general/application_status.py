from django.db import models
from common.models.abstract import *


class ApplicationStatus(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                        StatusRecordableModel, MakeableModel, CheckableModel):
    ApplicationStatusId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.ApplicationStatusId)

    class Meta:
        verbose_name = 'ApplicationStatus'
        verbose_name_plural = 'ApplicationStatus'
        db_table = 'ApplicationStatus'
