from django.db import models
from common.models.abstract import *


class AccountCategory(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                      HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    AccountCategoryId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AccountCategoryId, self.Description)

    class Meta:
        verbose_name = 'AccountCategory'
        verbose_name_plural = 'AccountCategory'
        db_table = 'AccountCategory'
