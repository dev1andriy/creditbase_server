from django.db import models
from common.models.abstract import *


class DocumentType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                   StatusRecordableModel, MakeableModel, CheckableModel):
    DocumentTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.DocumentTypeId)

    class Meta:
        verbose_name = 'DocumentType'
        verbose_name_plural = 'DocumentType'
        db_table = 'DocumentType'
