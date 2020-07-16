from django.db import models
from django.contrib.postgres.fields import JSONField

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty
from common.models.credit_application import CreditApplication
from common.models.arrangement.facility import Facility


class FacilityArchived(TimeStampedModel, InsertableModel, UpdateableModel, PrintableModel, RankableModel):
    FacilityId = models.AutoField(primary_key=True, null=False, blank=False)
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
        Facility,
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
    FacilityIdHost = models.CharField(max_length=50, null=True, blank=True)
    FacilityIdOther1 = models.CharField(max_length=50, null=True, blank=True)
    FacilityIdOther2 = models.CharField(max_length=50, null=True, blank=True)
    FacilityIdParent = models.ForeignKey(
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
    # ArrangementActionType = models.ForeignKey(ArrangementActionType, null=True, blank=True, on_delete=models.CASCADE)
    Description1 = JSONField(null=True, blank=True)
    Description2 = JSONField(null=True, blank=True)
    Purpose = JSONField(null=True, blank=True)
    Currency = JSONField(null=True, blank=True)
    NominalFXRate = JSONField(null=True, blank=True)
    CurrentFXRate = JSONField(null=True, blank=True)
    NegotiatedFXRate = JSONField(null=True, blank=True)
    NegotiatedFXDealRef = JSONField(null=True, blank=True)
    Sector = JSONField(null=True, blank=True)
    Industry = JSONField(null=True, blank=True)
    FrequencyTenor = JSONField(null=True, blank=True)
    FrequencyRepayment = JSONField(null=True, blank=True)
    TenorOriginal = JSONField(null=True, blank=True)
    TenorRemaining = JSONField(null=True, blank=True)
    DisbursementsCount = JSONField(null=True, blank=True)
    RelationshipOfficer1 = JSONField(null=True, blank=True)
    RelationshipOfficer2 = JSONField(null=True, blank=True)
    RelationshipOfficer3 = JSONField(null=True, blank=True)
    Account1 = JSONField(null=True, blank=True)
    Account2 = JSONField(null=True, blank=True)
    Account3 = JSONField(null=True, blank=True)
    Account4 = JSONField(null=True, blank=True)
    ParameterSummary1 = JSONField(null=True, blank=True)
    ParameterSummary2 = JSONField(null=True, blank=True)
    ParameterSummary3 = JSONField(null=True, blank=True)
    ApprovalDate = JSONField(null=True, blank=True)
    OriginationDate = JSONField(null=True, blank=True)
    LastDisbursementDate = JSONField(null=True, blank=True)
    BalanceDate = JSONField(null=True, blank=True)
    NegotiatedFXRateDate = JSONField(null=True, blank=True)
    MaturityDate = JSONField(null=True, blank=True)
    ExpiryDate = JSONField(null=True, blank=True)
    FirstPaymentDate = JSONField(null=True, blank=True)
    LastPaymentDate = JSONField(null=True, blank=True)
    NextPaymentDate = JSONField(null=True, blank=True)
    PrincipalDueDate = JSONField(null=True, blank=True)
    InterestDueDate = JSONField(null=True, blank=True)
    DefaultDate = JSONField(null=True, blank=True)
    ApprovalValue = JSONField(null=True, blank=True)
    OriginalValue = JSONField(null=True, blank=True)
    CommitmentValue = JSONField(null=True, blank=True)
    BalanceValue = JSONField(null=True, blank=True)
    ProposedValue = models.FloatField(null=True, blank=True)
    DisbursedValue = JSONField(null=True, blank=True)
    UndisbursedValue = JSONField(null=True, blank=True)
    UtilisedValue = JSONField(null=True, blank=True)
    UnutilizedValue = JSONField(null=True, blank=True)
    ExposureTotal = JSONField(null=True, blank=True)
    ExposureUnused = JSONField(null=True, blank=True)
    RepaymentAmount = JSONField(null=True, blank=True)
    TotalPrincipalPaid = JSONField(null=True, blank=True)
    TotalInterestPaid = JSONField(null=True, blank=True)
    TotalFeesPaid = JSONField(null=True, blank=True)
    ApprovedBaseRate = JSONField(null=True, blank=True)
    ApprovedSpreadFloor = JSONField(null=True, blank=True)
    ApprovedSpreadCeiling = JSONField(null=True, blank=True)
    ApprovedSpreadRate = JSONField(null=True, blank=True)
    EffectiveBaseRate = JSONField(null=True, blank=True)
    EffectiveSpreadFloor = JSONField(null=True, blank=True)
    EffectiveSpreadCeiling = JSONField(null=True, blank=True)
    EffectiveSpreadRate = JSONField(null=True, blank=True)
    CostOfFunds = JSONField(null=True, blank=True)
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
    Fee11 = JSONField(null=True, blank=True)
    Fee12 = JSONField(null=True, blank=True)
    Fee13 = JSONField(null=True, blank=True)
    Fee14 = JSONField(null=True, blank=True)
    Fee15 = JSONField(null=True, blank=True)
    Fee16 = JSONField(null=True, blank=True)
    Fee17 = JSONField(null=True, blank=True)
    Fee18 = JSONField(null=True, blank=True)
    Fee19 = JSONField(null=True, blank=True)
    Fee20 = JSONField(null=True, blank=True)
    IsSecured = JSONField(null=True, blank=True)
    IsGuaranteed = JSONField(null=True, blank=True)
    OpenMarketValue = JSONField(null=True, blank=True)
    DiscountedValue = JSONField(null=True, blank=True)
    ForcedSaleValue = JSONField(null=True, blank=True)
    CoverageByMV = JSONField(null=True, blank=True)
    CoverageByDV = JSONField(null=True, blank=True)
    CoverageByFSV = JSONField(null=True, blank=True)
    PastDueBucket = JSONField(null=True, blank=True)
    PastDueExposure = JSONField(null=True, blank=True)
    PastDuePrincipal = JSONField(null=True, blank=True)
    PastDueInterest = JSONField(null=True, blank=True)
    PenaltyInterestDue = JSONField(null=True, blank=True)
    PastDueBucket1 = JSONField(null=True, blank=True)
    PastDueBucket2 = JSONField(null=True, blank=True)
    PastDueBucket3 = JSONField(null=True, blank=True)
    PastDueBucket4 = JSONField(null=True, blank=True)
    PastDueBucket5 = JSONField(null=True, blank=True)
    PastDueBucket6 = JSONField(null=True, blank=True)
    SpecificProvisions = JSONField(null=True, blank=True)
    InterestProvisions = JSONField(null=True, blank=True)
    TotalProvisions = JSONField(null=True, blank=True)
    ExcessProvisions = JSONField(null=True, blank=True)
    MinimumProvisions = JSONField(null=True, blank=True)
    WriteDown = JSONField(null=True, blank=True)
    WriteBack = JSONField(null=True, blank=True)
    NetDebt = JSONField(null=True, blank=True)
    RecoveredAmount = JSONField(null=True, blank=True)
    ProfessionalFeesPaid = JSONField(null=True, blank=True)
    NetBalance = JSONField(null=True, blank=True)
    BISAssetClass = JSONField(null=True, blank=True)
    RatingInternalPD = JSONField(null=True, blank=True)
    RatingInternalLGD = JSONField(null=True, blank=True)
    ProbabilityOfDefault = JSONField(null=True, blank=True)
    LossGivenDefault = JSONField(null=True, blank=True)
    ExposureAtDefault = JSONField(null=True, blank=True)
    ExpectedLoss = JSONField(null=True, blank=True)
    UnexpectedLoss = JSONField(null=True, blank=True)
    OriginationCost = JSONField(null=True, blank=True)
    ServicingCost = JSONField(null=True, blank=True)
    AverageFees = JSONField(null=True, blank=True)
    OperationCost = JSONField(null=True, blank=True)
    OperationCapital = JSONField(null=True, blank=True)
    RegulatoryCapital = JSONField(null=True, blank=True)
    EconomicCapital = JSONField(null=True, blank=True)
    RAROC = JSONField(null=True, blank=True)
    RWADrawn = JSONField(null=True, blank=True)
    RWAUndrawn = JSONField(null=True, blank=True)
    RWATotal = JSONField(null=True, blank=True)
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
    Code21 = JSONField(null=True, blank=True)
    Code22 = JSONField(null=True, blank=True)
    Code23 = JSONField(null=True, blank=True)
    Code24 = JSONField(null=True, blank=True)
    Code25 = JSONField(null=True, blank=True)
    Code26 = JSONField(null=True, blank=True)
    Code27 = JSONField(null=True, blank=True)
    Code28 = JSONField(null=True, blank=True)
    Code29 = JSONField(null=True, blank=True)
    Code30 = JSONField(null=True, blank=True)
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
    Value21 = JSONField(null=True, blank=True)
    Value22 = JSONField(null=True, blank=True)
    Value23 = JSONField(null=True, blank=True)
    Value24 = JSONField(null=True, blank=True)
    Value25 = JSONField(null=True, blank=True)
    Value26 = JSONField(null=True, blank=True)
    Value27 = JSONField(null=True, blank=True)
    Value28 = JSONField(null=True, blank=True)
    Value29 = JSONField(null=True, blank=True)
    Value30 = JSONField(null=True, blank=True)
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
    Text21 = JSONField(null=True, blank=True)
    Text22 = JSONField(null=True, blank=True)
    Text23 = JSONField(null=True, blank=True)
    Text24 = JSONField(null=True, blank=True)
    Text25 = JSONField(null=True, blank=True)
    Text26 = JSONField(null=True, blank=True)
    Text27 = JSONField(null=True, blank=True)
    Text28 = JSONField(null=True, blank=True)
    Text29 = JSONField(null=True, blank=True)
    Text30 = JSONField(null=True, blank=True)
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
    Date21 = JSONField(null=True, blank=True)
    Date22 = JSONField(null=True, blank=True)
    Date23 = JSONField(null=True, blank=True)
    Date24 = JSONField(null=True, blank=True)
    Date25 = JSONField(null=True, blank=True)
    Date26 = JSONField(null=True, blank=True)
    Date27 = JSONField(null=True, blank=True)
    Date28 = JSONField(null=True, blank=True)
    Date29 = JSONField(null=True, blank=True)
    Date30 = JSONField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.FacilityId, self.ArrangementType)

    class Meta:
        verbose_name = 'FacilityArchived'
        verbose_name_plural = 'FacilityArchived'
        db_table = 'FacilityArchived'
