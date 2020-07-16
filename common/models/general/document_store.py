from django.db import models
from common.models.general import *
from common.models.abstract import *


class DocumentStore(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                    StatusRecordableModel, MakeableModel, CheckableModel):
    DocumentStoreId = models.AutoField(primary_key=True, null=False)
    DocumentStoreType = models.ForeignKey(
        DocumentStoreType,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.DocumentStoreId)

    class Meta:
        verbose_name = 'DocumentStore'
        verbose_name_plural = 'DocumentStore'
        db_table = 'DocumentStore'
