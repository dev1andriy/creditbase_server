from django.db import models
from common.models.abstract import *


class ActivityStatus(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                     StatusRecordableModel, MakeableModel, CheckableModel):
    ActivityStatusId = models.IntegerField(primary_key=True)

    def __str__(self):
        return "{} - {}".format(self.ActivityStatusId, self.Description)

    class Meta:
        verbose_name = 'ActivityStatus'
        verbose_name_plural = 'ActivityStatus'
        db_table = 'ActivityStatus'


