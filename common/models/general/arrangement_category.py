from django.db import models
from common.models.abstract import *


class ArrangementCategory(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                          StatusRecordableModel, MakeableModel, CheckableModel):
    ArrangementCategoryId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.ArrangementCategoryId, self.Description)

    class Meta:
        verbose_name = 'ArrangementCategory'
        verbose_name_plural = 'ArrangementCategory'
        db_table = 'ArrangementCategory'
