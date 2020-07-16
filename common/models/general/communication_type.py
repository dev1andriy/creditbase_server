from django.db import models
from common.models.abstract import *


class CommunicationType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                        StatusRecordableModel, MakeableModel, CheckableModel):
    CommunicationTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.CommunicationTypeId)

    class Meta:
        verbose_name = 'CommunicationType'
        verbose_name_plural = 'CommunicationType'
        db_table = 'CommunicationType'
