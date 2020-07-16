from django.db import models
from common.models.abstract import *


class AccountClass(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                   HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    AccountClassId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AccountClassId, self.Description)

    class Meta:
        verbose_name = 'AccountClass'
        verbose_name_plural = 'AccountClass'
        db_table = 'AccountClass'
