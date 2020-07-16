from django.db import models
from common.models.abstract import *


class DocumentStatus(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                     StatusRecordableModel, MakeableModel, CheckableModel):
    DocumentStatusId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.DocumentStatusId)

    class Meta:
        verbose_name = 'DocumentStatus'
        verbose_name_plural = 'DocumentStatus'
        db_table = 'DocumentStatus'
