from django.db import models
from common.models.abstract import *
from common.models.general import AccountCategory


class AccountType(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                  HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    AccountTypeId = models.IntegerField(primary_key=True)
    AccountCategory = models.ForeignKey(AccountCategory, null=False, blank=False, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AccountTypeId, self.Description)

    class Meta:
        verbose_name = 'AccountType'
        verbose_name_plural = 'AccountType'
        db_table = 'AccountType'
