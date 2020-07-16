from django.db import models
from django.contrib.auth import get_user_model

from common.models.abstract import *
from common.models.credit_memo import CreditMemo


class CreditMemoRecent(InsertableModel, UpdateableModel, TimeStampedModel):
    StaffId = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    CreditMemoId = models.ForeignKey(
        CreditMemo,
        on_delete=models.CASCADE,
        null=False, blank=False
    )

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.CreditMemoId, self.StaffId)

    class Meta:
        verbose_name = 'CreditMemoRecent'
        verbose_name_plural = 'CreditMemoRecent'
        db_table = 'CreditMemoRecent'
