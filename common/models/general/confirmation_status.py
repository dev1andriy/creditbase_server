from django.db import models
from common.models.abstract import *


class ConfirmationStatus(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                         StatusRecordableModel, MakeableModel, CheckableModel):
    ConfirmationStatusId = models.IntegerField(primary_key=True)

    def __str__(self):
        return "{} - {}".format(self.ConfirmationStatusId, self.Description)

    class Meta:
        verbose_name = 'ConfirmationStatus'
        verbose_name_plural = 'ConfirmationStatus'
        db_table = 'ConfirmationStatus'


