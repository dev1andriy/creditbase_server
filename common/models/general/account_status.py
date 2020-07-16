from django.db import models
from common.models.abstract import *


class AccountStatus(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                    HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    AccountStatusId = models.IntegerField(primary_key=True)

    def __str__(self):
        return "{} - {}".format(self.AccountStatusId, self.Description)

    objects = models.Manager()

    class Meta:
        verbose_name = 'AccountStatus'
        verbose_name_plural = 'AccountStatus'
        db_table = 'AccountStatus'
