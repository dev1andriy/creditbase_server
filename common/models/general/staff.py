from django.db import models
from common.models.abstract import *


class Staff(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
            StatusRecordableModel, MakeableModel, CheckableModel):
    StaffId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.StaffId, self.Description)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'
        db_table = 'Staff'
