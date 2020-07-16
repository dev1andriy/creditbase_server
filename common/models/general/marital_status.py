from django.db import models
from common.models.abstract import *


class MaritalStatus(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                    StatusRecordableModel, MakeableModel, CheckableModel):
    MaritalStatusId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.MaritalStatusId)

    class Meta:
        verbose_name = 'MaritalStatus'
        verbose_name_plural = 'MaritalStatus'
        db_table = 'MaritalStatus'
