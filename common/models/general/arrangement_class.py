from django.db import models
from common.models.abstract import *


class ArrangementClass(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                       StatusRecordableModel, MakeableModel, CheckableModel):
    ArrangementClassId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.ArrangementClassId, self.Description)

    class Meta:
        verbose_name = 'ArrangementClass'
        verbose_name_plural = 'ArrangementClass'
        db_table = 'ArrangementClass'
