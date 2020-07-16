from django.db import models
from common.models.abstract import *


class DocumentIdType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                     StatusRecordableModel, MakeableModel, CheckableModel):
    DocumentIdTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.DocumentIdTypeId)

    class Meta:
        verbose_name = 'DocumentIdType'
        verbose_name_plural = 'DocumentIdType'
        db_table = 'DocumentIdType'
