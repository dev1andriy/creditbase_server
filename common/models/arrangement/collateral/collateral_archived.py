from django.db import models
from django.contrib.postgres.fields import JSONField

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty
from common.models.credit_application import CreditApplication
from common.models.arrangement.collateral import Collateral


class CollateralArchived(TimeStampedModel, InsertableModel, UpdateableModel, PrintableModel, RankableModel):
    CollateralId = models.AutoField(primary_key=True, null=False, blank=False)
    CreditApplicationId = models.ForeignKey(
        CreditApplication,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    ArchiveVersion = models.IntegerField(null=True, blank=True)
    ArchiveStatus = models.ForeignKey(
        ApplicationStatus,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    ActiveVersion = models.ForeignKey(
        Collateral,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
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
    CollateralIdHost = models.CharField(max_length=50, null=True, blank=True)
    CollateralIdOther1 = models.CharField(max_length=50, null=True, blank=True)
    CollateralIdOther2 = models.CharField(max_length=50, null=True, blank=True)
    CollateralIdParent = models.ForeignKey(
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
    ActionableFlag = models.BooleanField(default=False)
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
    ApprovalDate = JSONField(null=True, blank=True)
    OriginationDate = JSONField(null=True, blank=True)
    CoverageDate = JSONField(null=True, blank=True)
    NegotiatedFXRateDate = JSONField(null=True, blank=True)
    ExpiryDate = JSONField(null=True, blank=True)
    NextReviewDate = JSONField(null=True, blank=True)
    ForcedSaleValue = JSONField(null=True, blank=True)
    MarketValue = JSONField(null=True, blank=True)
    DiscountedValue = JSONField(null=True, blank=True)
    RecoveryValue = JSONField(null=True, blank=True)
    ApprovedCharge = JSONField(null=True, blank=True)
    OriginalCharge = JSONField(null=True, blank=True)
    ExistingCharge = JSONField(null=True, blank=True)
    ProposedCharge = JSONField(null=True, blank=True)
    ProposedValue = models.FloatField(null=True, blank=True)
    PriorLiens = JSONField(null=True, blank=True)
    ExistingExposure = JSONField(null=True, blank=True)
    DiscountFactor = JSONField(null=True, blank=True)
    LossRate = JSONField(null=True, blank=True)
    InsuranceType1 = JSONField(null=True, blank=True)
    InsuranceProvider1 = JSONField(null=True, blank=True)
    InsuranceExpiryDate1 = JSONField(null=True, blank=True)
    InsuranceAmount1 = JSONField(null=True, blank=True)
    InsurancePolicyRef1 = JSONField(null=True, blank=True)
    InsuranceProvider2 = JSONField(null=True, blank=True)
    InsuranceExpiryDate2 = JSONField(null=True, blank=True)
    InsuranceAmount2 = JSONField(null=True, blank=True)
    InsurancePolicyRef2 = JSONField(null=True, blank=True)
    InsuranceProvider3 = JSONField(null=True, blank=True)
    InsuranceExpiryDate3 = JSONField(null=True, blank=True)
    InsuranceAmount3 = JSONField(null=True, blank=True)
    InsurancePolicyRef3 = JSONField(null=True, blank=True)
    ValuationDone = JSONField(null=True, blank=True)
    ValuationBasis = JSONField(null=True, blank=True)
    ValuationProvider = JSONField(null=True, blank=True)
    ValuerName = JSONField(null=True, blank=True)
    ValuationDate = JSONField(null=True, blank=True)
    ValuationExpiryDate = JSONField(null=True, blank=True)
    TrackingInstalled = JSONField(null=True, blank=True)
    TrackerId = JSONField(null=True, blank=True)
    TrackerName = JSONField(null=True, blank=True)
    TrackingInstallDate = JSONField(null=True, blank=True)
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
    Code11 = JSONField(null=True, blank=True)
    Code12 = JSONField(null=True, blank=True)
    Code13 = JSONField(null=True, blank=True)
    Code14 = JSONField(null=True, blank=True)
    Code15 = JSONField(null=True, blank=True)
    Code16 = JSONField(null=True, blank=True)
    Code17 = JSONField(null=True, blank=True)
    Code18 = JSONField(null=True, blank=True)
    Code19 = JSONField(null=True, blank=True)
    Code20 = JSONField(null=True, blank=True)
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
    Value11 = JSONField(null=True, blank=True)
    Value12 = JSONField(null=True, blank=True)
    Value13 = JSONField(null=True, blank=True)
    Value14 = JSONField(null=True, blank=True)
    Value15 = JSONField(null=True, blank=True)
    Value16 = JSONField(null=True, blank=True)
    Value17 = JSONField(null=True, blank=True)
    Value18 = JSONField(null=True, blank=True)
    Value19 = JSONField(null=True, blank=True)
    Value20 = JSONField(null=True, blank=True)
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
    Text11 = JSONField(null=True, blank=True)
    Text12 = JSONField(null=True, blank=True)
    Text13 = JSONField(null=True, blank=True)
    Text14 = JSONField(null=True, blank=True)
    Text15 = JSONField(null=True, blank=True)
    Text16 = JSONField(null=True, blank=True)
    Text17 = JSONField(null=True, blank=True)
    Text18 = JSONField(null=True, blank=True)
    Text19 = JSONField(null=True, blank=True)
    Text20 = JSONField(null=True, blank=True)
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
    Date11 = JSONField(null=True, blank=True)
    Date12 = JSONField(null=True, blank=True)
    Date13 = JSONField(null=True, blank=True)
    Date14 = JSONField(null=True, blank=True)
    Date15 = JSONField(null=True, blank=True)
    Date16 = JSONField(null=True, blank=True)
    Date17 = JSONField(null=True, blank=True)
    Date18 = JSONField(null=True, blank=True)
    Date19 = JSONField(null=True, blank=True)
    Date20 = JSONField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.CollateralId)

    class Meta:
        verbose_name = 'CollateralArchived'
        verbose_name_plural = 'CollateralArchived'
        db_table = 'CollateralArchived'
