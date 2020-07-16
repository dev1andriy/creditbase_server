from django.db import models

from common.models.general import *
from common.models.base_party import BaseParty


class BasePartyFinancialsSummary(models.Model):
    BasePartyId = models.OneToOneField(
        BaseParty,
        related_name='FinancialsSummary',
        on_delete=models.CASCADE,
    )
    FinancialModel = models.ForeignKey(
        FinancialModel,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    FiscalYearEnd = models.ForeignKey(
        FiscalYearEnd,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    RecentStatementDate = models.DateTimeField(default=None, blank=True, null=True)
    StatementCount = models.IntegerField(default=None, blank=True, null=True)
    StatementHistory = models.IntegerField(default=None, blank=True, null=True)
    TotalRevenue = models.FloatField(default=None, blank=True, null=True)
    GrossProfit = models.FloatField(default=None, blank=True, null=True)
    TotalOperatingExpenses = models.FloatField(default=None, blank=True, null=True)
    EBITDA = models.FloatField(default=None, blank=True, null=True)
    RetainedEarnings = models.FloatField(default=None, blank=True, null=True)
    TotalAssets = models.FloatField(default=None, blank=True, null=True)
    TotalCurrentAssets = models.FloatField(default=None, blank=True, null=True)
    TotalNonCurrentAssets = models.FloatField(default=None, blank=True, null=True)
    TotalCurrentLiabilities = models.FloatField(default=None, blank=True, null=True)
    TotalNonCurrentLiabilities = models.FloatField(default=None, blank=True, null=True)
    TotalEquity = models.FloatField(default=None, blank=True, null=True)
    DSCR = models.FloatField(default=None, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'BasePartyFinancialsSummary'
        verbose_name_plural = 'BasePartyFinancialsSummary'
        db_table = 'BasePartyFinancialsSummary'
