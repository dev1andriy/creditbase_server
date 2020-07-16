from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty


class BasePartyBankingSummary(InsertableModel, UpdateableModel):
    BasePartyId = models.OneToOneField(
        BaseParty,
        related_name='BankingSummary',
        on_delete=models.CASCADE,
        primary_key=True
    )
    CommitmentTotal = models.FloatField(default=None, blank=True, null=True)
    ExposureTotal = models.FloatField(default=None, blank=True, null=True)
    ExposureProposed = models.FloatField(default=None, blank=True, null=True)
    ExposureIncrease = models.FloatField(default=None, blank=True, null=True)
    ExposureAtRisk = models.FloatField(default=None, blank=True, null=True)
    CollateralValuebyMV = models.FloatField(default=None, blank=True, null=True)
    CollateralValuebyFSV = models.FloatField(default=None, blank=True, null=True)
    CollateralValuebyDV = models.FloatField(default=None, blank=True, null=True)
    CoverageRatiobyMV = models.FloatField(default=None, blank=True, null=True)
    CoverageRatiobyFSV = models.FloatField(default=None, blank=True, null=True)
    CoverageRatiobyDV = models.FloatField(default=None, blank=True, null=True)
    AssetClassification = models.ForeignKey(
        AssetClassification,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PastDueDays = models.IntegerField(default=None, blank=True, null=True)
    PastDueTotal = models.FloatField(default=None, blank=True, null=True)
    PastDueBucket1 = models.FloatField(default=None, blank=True, null=True)
    PastDueBucket2 = models.FloatField(default=None, blank=True, null=True)
    PastDueBucket3 = models.FloatField(default=None, blank=True, null=True)
    PastDueBucket4 = models.FloatField(default=None, blank=True, null=True)
    PastDueBucket5 = models.FloatField(default=None, blank=True, null=True)
    PastDueBucket6 = models.FloatField(default=None, blank=True, null=True)
    DepositsBalanceTotal = models.FloatField(default=None, blank=True, null=True)
    DepositsOriginalTotal = models.FloatField(default=None, blank=True, null=True)
    FacilitiesCount = models.IntegerField(default=None, blank=True, null=True)
    FacilitiesPastDueCount = models.FloatField(default=None, blank=True, null=True)
    CollateralsCount = models.IntegerField(default=None, blank=True, null=True)
    DepositsCount = models.IntegerField(default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.BasePartyId)

    class Meta:
        verbose_name = 'BasePartyBankingSummary'
        verbose_name_plural = 'BasePartyBankingSummary'
        db_table = 'BasePartyBankingSummary'
