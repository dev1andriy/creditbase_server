from django.db import models
from common.models.abstract import *
from common.models.general import ArrangementCategory


class ArrangementParamCategory(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                               StatusRecordableModel, MakeableModel, CheckableModel):
    ArrangementParamCategoryId = models.AutoField(primary_key=True, null=False)
    ArrangementCategory = models.ForeignKey(ArrangementCategory, null=True, blank=True, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.ArrangementParamCategoryId, self.Description)

    class Meta:
        verbose_name = 'ArrangementParamCategory'
        verbose_name_plural = 'ArrangementParamCategory'
        db_table = 'ArrangementParamCategory'
