from django.db import models
from common.models.abstract import *


class JobGrade(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
               StatusRecordableModel, MakeableModel, CheckableModel):
    JobGradeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.JobGradeId, self.Description)

    class Meta:
        verbose_name = 'JobGrade'
        verbose_name_plural = 'JobGrade'
        db_table = 'JobGrade'


