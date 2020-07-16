from django.db import models
from common.models.abstract import *


class ChecklistStatus(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                      StatusRecordableModel, MakeableModel, CheckableModel):
    ChecklistStatusId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.ChecklistStatusId)

    class Meta:
        verbose_name = 'ChecklistStatus'
        verbose_name_plural = 'ChecklistStatus'
        db_table = 'ChecklistStatus'

