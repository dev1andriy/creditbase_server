from django.db import models
from django.contrib.postgres.fields import JSONField

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty
from common.models.credit_application import CreditApplication


class Deposit(TimeStampedModel, InsertableModel, UpdateableModel):
    DepositId = models.AutoField(primary_key=True, null=False, blank=False)
    BasePartyId = models.ForeignKey(
        BaseParty,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    HostId = models.ForeignKey(
        Host,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    DataView = models.IntegerField(null=True, blank=True)
    RequestType = models.ForeignKey(
        RequestType,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    DepositIdHost = models.CharField(max_length=50, null=True, blank=True)
    DepositIdOther1 = models.CharField(max_length=50, null=True, blank=True)
    DepositIdOther2 = models.CharField(max_length=50, null=True, blank=True)
    DepositIdParent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    ArrangementClass = models.ForeignKey(
        ArrangementClass,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    ArrangementTypeHost = models.CharField(max_length=20, null=True, blank=True)
    ArrangementType = models.ForeignKey(
        ArrangementType,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    CreditApplicationId = models.ForeignKey(
        CreditApplication,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    Description1 = JSONField(null=True, blank=True)
    Description2 = JSONField(null=True, blank=True)
    Currency = JSONField(null=True, blank=True)
    NominalFXRate = JSONField(null=True, blank=True)
    CurrentFXRate = JSONField(null=True, blank=True)
    NegotiatedFXRate = JSONField(null=True, blank=True)
    NegotiatedFXDealRef = JSONField(null=True, blank=True)
    RelationshipOfficer1 = JSONField(null=True, blank=True)
    RelationshipOfficer2 = JSONField(null=True, blank=True)
    RelationshipOfficer3 = JSONField(null=True, blank=True)
    ParameterSummary1 = JSONField(null=True, blank=True)
    ParameterSummary2 = JSONField(null=True, blank=True)
    ParameterSummary3 = JSONField(null=True, blank=True)
    TenorOriginal = JSONField(null=True, blank=True)
    TenorRemaining = JSONField(null=True, blank=True)
    ApprovalDate = JSONField(null=True, blank=True)
    OriginationDate = JSONField(null=True, blank=True)
    BalanceDate = JSONField(null=True, blank=True)
    NegotiatedFXRateDate = JSONField(null=True, blank=True)
    MaturityDate = JSONField(null=True, blank=True)
    NextRolloverDate = JSONField(null=True, blank=True)
    OriginalDeposit = JSONField(null=True, blank=True)
    OriginalValue = JSONField(null=True, blank=True)
    BalanceValue = JSONField(null=True, blank=True)
    TotalPrincipal = JSONField(null=True, blank=True)
    TotalInterestPaid = JSONField(null=True, blank=True)
    BalanceHigh1M = JSONField(null=True, blank=True)
    BalanceHigh3M = JSONField(null=True, blank=True)
    BalanceHigh6M = JSONField(null=True, blank=True)
    BalanceHigh12M = JSONField(null=True, blank=True)
    BalanceHighYTD = JSONField(null=True, blank=True)
    BalanceLow1M = JSONField(null=True, blank=True)
    BalanceLow3M = JSONField(null=True, blank=True)
    BalanceLow6M = JSONField(null=True, blank=True)
    BalanceLow12M = JSONField(null=True, blank=True)
    BalanceLowYTD = JSONField(null=True, blank=True)
    BalanceAvg1M = JSONField(null=True, blank=True)
    BalanceAvg3M = JSONField(null=True, blank=True)
    BalanceAvg6M = JSONField(null=True, blank=True)
    BalanceAvg12M = JSONField(null=True, blank=True)
    BalanceAvgYTD = JSONField(null=True, blank=True)
    ApprovedBaseRate = JSONField(null=True, blank=True)
    ApprovedSpreadFloor = JSONField(null=True, blank=True)
    ApprovedSpreadCeiling = JSONField(null=True, blank=True)
    ApprovedSpreadRate = JSONField(null=True, blank=True)
    EffectiveBaseRate = JSONField(null=True, blank=True)
    EffectiveSpreadFloor = JSONField(null=True, blank=True)
    EffectiveSpreadCeiling = JSONField(null=True, blank=True)
    EffectiveSpreadRate = JSONField(null=True, blank=True)
    Fee1 = JSONField(null=True, blank=True)
    Fee2 = JSONField(null=True, blank=True)
    Fee3 = JSONField(null=True, blank=True)
    Fee4 = JSONField(null=True, blank=True)
    Fee5 = JSONField(null=True, blank=True)
    Fee6 = JSONField(null=True, blank=True)
    Fee7 = JSONField(null=True, blank=True)
    Fee8 = JSONField(null=True, blank=True)
    Fee9 = JSONField(null=True, blank=True)
    Fee10 = JSONField(null=True, blank=True)
    Code1 = JSONField(null=True, blank=True)
    Code2 = JSONField(null=True, blank=True)
    Code3 = JSONField(null=True, blank=True)
    Code4 = JSONField(null=True, blank=True)
    Code5 = JSONField(null=True, blank=True)
    Code6 = JSONField(null=True, blank=True)
    Code7 = JSONField(null=True, blank=True)
    Code8 = JSONField(null=True, blank=True)
    Code9 = JSONField(null=True, blank=True)
    Code10 = JSONField(null=True, blank=True)
    Value1 = JSONField(null=True, blank=True)
    Value2 = JSONField(null=True, blank=True)
    Value3 = JSONField(null=True, blank=True)
    Value4 = JSONField(null=True, blank=True)
    Value5 = JSONField(null=True, blank=True)
    Value6 = JSONField(null=True, blank=True)
    Value7 = JSONField(null=True, blank=True)
    Value8 = JSONField(null=True, blank=True)
    Value9 = JSONField(null=True, blank=True)
    Value10 = JSONField(null=True, blank=True)
    Text1 = JSONField(null=True, blank=True)
    Text2 = JSONField(null=True, blank=True)
    Text3 = JSONField(null=True, blank=True)
    Text4 = JSONField(null=True, blank=True)
    Text5 = JSONField(null=True, blank=True)
    Text6 = JSONField(null=True, blank=True)
    Text7 = JSONField(null=True, blank=True)
    Text8 = JSONField(null=True, blank=True)
    Text9 = JSONField(null=True, blank=True)
    Text10 = JSONField(null=True, blank=True)
    Date1 = JSONField(null=True, blank=True)
    Date2 = JSONField(null=True, blank=True)
    Date3 = JSONField(null=True, blank=True)
    Date4 = JSONField(null=True, blank=True)
    Date5 = JSONField(null=True, blank=True)
    Date6 = JSONField(null=True, blank=True)
    Date7 = JSONField(null=True, blank=True)
    Date8 = JSONField(null=True, blank=True)
    Date9 = JSONField(null=True, blank=True)
    Date10 = JSONField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.DepositId)

    class Meta:
        verbose_name = 'Deposit'
        verbose_name_plural = 'Deposit'
        db_table = 'Deposit'
