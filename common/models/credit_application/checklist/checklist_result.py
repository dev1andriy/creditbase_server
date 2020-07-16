from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty
from common.models.credit_application import CreditApplication
from common.models.credit_application.checklist import ChecklistTemplate


class ChecklistResult(UpdateableModel, InsertableModel, TimeStampedModel):
    ChecklistResultId = models.AutoField(primary_key=True, null=False)
    BasePartyId = models.ForeignKey(
        BaseParty,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CreditApplicationId = models.ForeignKey(
        CreditApplication,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )

    # ModuleId
    TemplateId = models.ForeignKey(
        ChecklistTemplate,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )

    # it will be improved
    Role = models.CharField(max_length=100, default="Temp role", null=True, blank=True)

    Score = models.FloatField(default=None, null=True, blank=True)
    Status = models.ForeignKey(
        ChecklistStatus,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    FinalizedFlag = models.BooleanField(default=False, null=False, blank=False)

    Comment = models.TextField(default=None, null=True, blank=True)

    TEMP_FIELD = models.IntegerField(null=False, blank=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.ChecklistResultId)

    class Meta:
        verbose_name = 'ChecklistResult'
        verbose_name_plural = 'ChecklistResult'
        db_table = 'ChecklistResult'
