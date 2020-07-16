from django.db import models
from common.models.abstract import *


class ChangeType(HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                 StatusRecordableModel, MakeableModel, CheckableModel):
    ChangeTypeId = models.AutoField(primary_key=True, null=False)
    Description = models.CharField(max_length=100, null=True, blank=True, default=None)

    objects = models.Manager()

    def __str__(self):
        return '{} - {}'.format(self.ChangeTypeId, self.Description)

    class Meta:
        verbose_name = 'ChangeType'
        verbose_name_plural = 'ChangeType'
        db_table = 'ChangeType'
