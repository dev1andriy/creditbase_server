from django.db import models
from common.models.abstract import *


class AlertDocumentStatus(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                          StatusRecordableModel, MakeableModel, CheckableModel):
    AlertDocumentStatusId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AlertDocumentStatusId, self.Description)

    class Meta:
        verbose_name = 'AlertDocumentStatus'
        verbose_name_plural = 'AlertDocumentStatus'
        db_table = 'AlertDocumentStatus'
