from django.db import models

from common.models.abstract import *


class CreditMemo(InsertableModel, UpdateableModel, TimeStampedModel, StatusRecordableModel, MakeableModel,
                 CheckableModel):
    CreditMemoId = models.AutoField(primary_key=True, null=False)

    # it will be improved
    ModuleId = models.IntegerField(default=None, null=True, blank=True)

    EntityTypesApplicable = models.IntegerField(default=None, null=True, blank=True)
    RequestTypesApplicable = models.IntegerField(default=None, null=True, blank=True)
    ProductTypesApplicable = models.IntegerField(default=None, null=True, blank=True)
    CollateralTypesApplicable = models.IntegerField(default=None, null=True, blank=True)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=300)
    CreditMemoId1 = models.IntegerField(default=None, null=True, blank=True)

    # it will be improved
    EnabledFlag = models.IntegerField(default=None, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.CreditMemoId)

    class Meta:
        verbose_name = 'CreditMemo'
        verbose_name_plural = 'CreditMemo'
        db_table = 'CreditMemo'
