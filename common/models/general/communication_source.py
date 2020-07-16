from django.db import models
from common.models.abstract import *


class CommunicationSource(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                          StatusRecordableModel, MakeableModel, CheckableModel):
    CommunicationSourceId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.CommunicationSourceId)

    class Meta:
        verbose_name = 'CommunicationSource'
        verbose_name_plural = 'CommunicationSource'
        db_table = 'CommunicationSource'
