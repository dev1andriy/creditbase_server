from django.db import models
from common.models.abstract import *


class ActivityType(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                   StatusRecordableModel, MakeableModel, CheckableModel):
    ActivityTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.ActivityTypeId, self.Description)

    class Meta:
        verbose_name = 'ActivityType'
        verbose_name_plural = 'ActivityType'
        db_table = 'ActivityType'


