from django.db import models
from django.contrib.auth import get_user_model

from common.models.abstract import *
from common.models.general import *


class CreditApplicationStaff(UpdateableModel, InsertableModel, TimeStampedModel, RankableModel, PrintableModel):
    CreditApplicationId = models.ForeignKey(
        'common.CreditApplication',
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    StaffId = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    RelationCategory = models.ForeignKey(
        RelationCategory,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    RelationType = models.ForeignKey(
        RelationType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    IsPrimaryRelatedStaff = models.BooleanField(default=False)
    Comment = models.TextField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.CreditApplicationId)

    class Meta:
        verbose_name = 'CreditApplicationStaff'
        verbose_name_plural = 'CreditApplicationStaff'
        db_table = 'CreditApplicationStaff'
