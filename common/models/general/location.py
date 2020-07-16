from django.db import models
from common.models.abstract import *


class Location(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
               StatusRecordableModel, MakeableModel, CheckableModel):
    LocationId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.LocationId, self.Description)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Location'
        db_table = 'Location'
