from django.db import models

from common.models.abstract import *
from common.models.credit_memo import CreditMemo


class CreditMemoSection(InsertableModel, UpdateableModel, TimeStampedModel, ViewableModel):
    CreditMemoSectionId = models.AutoField(primary_key=True, null=False)
    CreditMemoId = models.ForeignKey(
        CreditMemo,
        on_delete=models.CASCADE,
        null=False,  blank=False
    )
    SectionOrder = models.IntegerField(default=1, null=False, blank=False)
    Name1 = models.CharField(max_length=100)
    Name2 = models.CharField(max_length=100)
    Description = models.CharField(max_length=300)
    # it will be improved
    TemplateId = models.IntegerField(default=None, null=True, blank=True)
    QueryId = models.IntegerField(default=None, null=True, blank=True)
    SectionContent = models.TextField(default=None, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.CreditMemoId, self.CreditMemoSectionId)

    class Meta:
        verbose_name = 'CreditMemoSection'
        verbose_name_plural = 'CreditMemoSection'
        db_table = 'CreditMemoSection'
