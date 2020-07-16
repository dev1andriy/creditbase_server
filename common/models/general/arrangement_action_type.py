from django.db import models
from common.models.abstract import *


class ArrangementActionType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                            StatusRecordableModel, MakeableModel, CheckableModel):
    ArrangementActionTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.ArrangementActionTypeId, self.Description)

    class Meta:
        verbose_name = 'ArrangementActionType'
        verbose_name_plural = 'ArrangementActionType'
        db_table = 'ArrangementActionType'
