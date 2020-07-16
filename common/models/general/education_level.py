from django.db import models
from common.models.abstract import *


class EducationLevel(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                     StatusRecordableModel, MakeableModel, CheckableModel):
    EducationLevelId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.EducationLevelId)

    class Meta:
        verbose_name = 'EducationLevel'
        verbose_name_plural = 'EducationLevel'
        db_table = 'EducationLevel'
