from django.db import models
from common.models.abstract import *


class ActionType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                 StatusRecordableModel, MakeableModel, CheckableModel):
    ActionTypeId = models.AutoField(primary_key=True, null=False)
    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.ActionTypeId, self.Description)

    class Meta:
        verbose_name = 'ActionType'
        verbose_name_plural = 'ActionType'
        db_table = 'ActionType'

