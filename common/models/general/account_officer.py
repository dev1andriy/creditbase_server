from django.db import models
from common.models.abstract import *


class AccountOfficer(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                     HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    AccountOfficerId = models.IntegerField(primary_key=True)

    def __str__(self):
        return "{} - {}".format(self.AccountOfficerId, self.Description)

    objects = models.Manager()

    class Meta:
        verbose_name = 'AccountOfficer'
        verbose_name_plural = 'AccountOfficer'
        db_table = 'AccountOfficer'
