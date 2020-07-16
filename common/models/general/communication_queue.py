from django.db import models
from common.models.abstract import *


class CommunicationQueue(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                         StatusRecordableModel, MakeableModel, CheckableModel):
    CommunicationQueueId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.CommunicationQueueId)

    class Meta:
        verbose_name = 'CommunicationQueue'
        verbose_name_plural = 'CommunicationQueue'
        db_table = 'CommunicationQueue'
