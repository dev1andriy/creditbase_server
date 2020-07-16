from django.db import models
from common.models.abstract import *


class CommunicationStatus(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                          StatusRecordableModel, MakeableModel, CheckableModel):
    CommunicationStatusId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.CommunicationStatusId)

    class Meta:
        verbose_name = 'CommunicationStatus'
        verbose_name_plural = 'CommunicationStatus'
        db_table = 'CommunicationStatus'
