from django.db import models
from common.models.abstract import *


class AlertConvertOption(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                         StatusRecordableModel, MakeableModel, CheckableModel):
    AlertConvertOptionId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AlertConvertOptionId, self.Description)

    class Meta:
        verbose_name = 'AlertConvertOption'
        verbose_name_plural = 'AlertConvertOption'
        db_table = 'AlertConvertOption'
