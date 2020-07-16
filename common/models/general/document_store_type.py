from django.db import models
from common.models.abstract import *


class DocumentStoreType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                        StatusRecordableModel, MakeableModel, CheckableModel):
    DocumentStoreTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.DocumentStoreTypeId)

    class Meta:
        verbose_name = 'DocumentStoreType'
        verbose_name_plural = 'DocumentStoreType'
        db_table = 'DocumentStoreType'
