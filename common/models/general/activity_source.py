from django.db import models
from common.models.abstract import *


class ActivitySource(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                     StatusRecordableModel, MakeableModel, CheckableModel):
    ActivitySourceId = models.IntegerField(primary_key=True)

    def __str__(self):
        return "{} - {}".format(self.ActivitySourceId, self.Description)

    class Meta:
        verbose_name = 'ActivitySource'
        verbose_name_plural = 'ActivitySource'
        db_table = 'ActivitySource'


