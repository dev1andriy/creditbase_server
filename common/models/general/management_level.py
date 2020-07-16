from django.db import models
from common.models.abstract import *


class ManagementLevel(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                      StatusRecordableModel, MakeableModel, CheckableModel):
    ManagementLevelId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.ManagementLevelId, self.Description)

    class Meta:
        verbose_name = 'ManagementLevel'
        verbose_name_plural = 'ManagementLevel'
        db_table = 'ManagementLevel'


