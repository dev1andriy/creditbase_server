from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty


class IndustryAnalysis(RankableModel, StatusRecordableModel, TimeStampedModel, InsertableModel, UpdateableModel):
    IndustryAnalysisId = models.AutoField(primary_key=True, null=False)
    BasePartyId = models.ForeignKey(
        BaseParty,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Industry = models.ForeignKey(
        Industry,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ProductServiceSold = models.CharField(max_length=100, default=None, blank=True, null=True)
    RevenueContribution = models.FloatField(default=None, blank=True, null=True)
    PercentTotalRevenue = models.FloatField(default=None, blank=True, null=True)
    PercentMarketShare = models.FloatField(default=None, blank=True, null=True)
    GrowthRate = models.FloatField(default=None, blank=True, null=True)
    BuyerPower = models.ForeignKey(
        BuyerPower,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    SupplierPower = models.ForeignKey(
        SupplierPower,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    NewEntrantThreat = models.ForeignKey(
        NewEntrantThreat,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    SubstitutionThreat = models.ForeignKey(
        SubstitutionThreat,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CompetitiveRivalry = models.ForeignKey(
        CompetitiveRivalry,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    IsPrimaryRevenueStream = models.BooleanField(default=False)
    Comment = models.TextField(default=None, blank=True, null=True)
    StartDate = models.DateTimeField(default=None, blank=True, null=True)
    EndDate = models.DateTimeField(default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.IndustryAnalysisId)

    class Meta:
        verbose_name = 'IndustryAnalysis'
        verbose_name_plural = 'IndustryAnalysis'
        db_table = 'IndustryAnalysis'
