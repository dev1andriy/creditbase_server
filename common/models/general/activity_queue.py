from django.db import models
from common.models.abstract import *


class ActivityQueue(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                    StatusRecordableModel, MakeableModel, CheckableModel):
    ActivityQueueId = models.IntegerField(primary_key=True)

    def __str__(self):
        return "{} - {}".format(self.ActivityQueueId, self.Description)

    class Meta:
        verbose_name = 'ActivityQueue'
        verbose_name_plural = 'ActivityQueue'
        db_table = 'ActivityQueue'


