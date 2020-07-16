from django.db import models

from common.models.abstract import *


class CreditApplicationBankingSummary(UpdateableModel, InsertableModel, TimeStampedModel):
    CreditApplicationId = models.ForeignKey(
        'common.CreditApplication',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ExistingCommitment = models.FloatField(default=None, blank=True, null=True)
    ExistingBalance = models.FloatField(default=None, blank=True, null=True)
    ExistingExposure = models.FloatField(default=None, blank=True, null=True)
    ProposedCommitment = models.FloatField(default=None, blank=True, null=True)
    ProposedBalance = models.FloatField(default=None, blank=True, null=True)
    ProposedExposure = models.FloatField(default=None, blank=True, null=True)
    ProposedIncrease = models.FloatField(default=None, blank=True, null=True)
    ApprovedCommitment = models.FloatField(default=None, blank=True, null=True)
    ApprovedBalance = models.FloatField(default=None, blank=True, null=True)
    ApprovedExposure = models.FloatField(default=None, blank=True, null=True)
    ApprovedIncrease = models.FloatField(default=None, blank=True, null=True)
    ExistingMarketValue = models.FloatField(default=None, blank=True, null=True)
    ExistingForcedSaleValue = models.FloatField(default=None, blank=True, null=True)
    ExistingDiscountedValue = models.FloatField(default=None, blank=True, null=True)
    ExistingLienValue = models.FloatField(default=None, blank=True, null=True)
    ExistingCoverageByMV = models.FloatField(default=None, blank=True, null=True)
    ExistingCoverageByFSV = models.FloatField(default=None, blank=True, null=True)
    ExistingCoverageByDV = models.FloatField(default=None, blank=True, null=True)
    ExistingCoverageByLV = models.FloatField(default=None, blank=True, null=True)
    ProposedMarketValue = models.FloatField(default=None, blank=True, null=True)
    ProposedForcedSaleValue = models.FloatField(default=None, blank=True, null=True)
    ProposedDiscountedValue = models.FloatField(default=None, blank=True, null=True)
    ProposedLienValue = models.FloatField(default=None, blank=True, null=True)
    ProposedCoverageByMV = models.FloatField(default=None, blank=True, null=True)
    ProposedCoverageByFSV = models.FloatField(default=None, blank=True, null=True)
    ProposedCoverageByDV = models.FloatField(default=None, blank=True, null=True)
    ProposedCoverageByLV = models.FloatField(default=None, blank=True, null=True)
    ApprovedMarketValue = models.FloatField(default=None, blank=True, null=True)
    ApprovedForcedSaleValue = models.FloatField(default=None, blank=True, null=True)
    ApprovedDiscountedValue = models.FloatField(default=None, blank=True, null=True)
    ApprovedLienValue = models.FloatField(default=None, blank=True, null=True)
    ApprovedCoverageByMV = models.FloatField(default=None, blank=True, null=True)
    ApprovedCoverageByFSV = models.FloatField(default=None, blank=True, null=True)
    ApprovedCoverageByDV = models.FloatField(default=None, blank=True, null=True)
    ApprovedCoverageByLV = models.FloatField(default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.CreditApplicationId)

    class Meta:
        verbose_name = 'CreditApplicationBankingSummary'
        verbose_name_plural = 'CreditApplicationBankingSummary'
        db_table = 'CreditApplicationBankingSummary'
