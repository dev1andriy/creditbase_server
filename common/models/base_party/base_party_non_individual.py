from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty


class BasePartyNonIndividual(InsertableModel, UpdateableModel):
    BasePartyId = models.OneToOneField(
        BaseParty,
        related_name='OtherInformation',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    HeadBasePartyId = models.ForeignKey(
        BaseParty,
        related_name='HeadBasePartyId',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ParentBasePartyId = models.ForeignKey(
        BaseParty,
        related_name='ParentBasePartyId',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    TradingAs = models.CharField(max_length=50, default=None, blank=True, null=True)
    PrimarySector = models.ForeignKey(
        Sector,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PrimaryIndustry = models.ForeignKey(
        Industry,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PrimaryActivity = models.ForeignKey(
        ActivityType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    OperationalStatus = models.ForeignKey(
        OperationalStatus,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CountryRegistration = models.ForeignKey(
        Country,
        related_name='CountryRegistration',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CountryOperation = models.ForeignKey(
        Country,
        related_name='CountryOperation',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PeriodAtAddress = models.FloatField(default=None, blank=True, null=True)
    RegistrationDate = models.DateTimeField(default=None, blank=True, null=True)
    OperationsStartDate = models.DateTimeField(default=None, blank=True, null=True)
    ShareCaptitalAuthorized = models.FloatField(default=None, blank=True, null=True)
    ShareCapitalPaidUp = models.FloatField(default=None, blank=True, null=True)
    ExperienceOfPromoters = models.FloatField(default=None, blank=True, null=True)
    ExperienceOfManagement = models.FloatField(default=None, blank=True, null=True)
    Governance = models.ForeignKey(
        GovernanceType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    DecisionMakingType = models.ForeignKey(
        DecisionMakingType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    IsFamilyBusiness = models.IntegerField(default=None, blank=True, null=True)
    IsGroupOwned = models.IntegerField(default=None, blank=True, null=True)
    IsWomanOwned = models.IntegerField(default=None, blank=True, null=True)
    IsYouthOwned = models.IntegerField(default=None, blank=True, null=True)
    TenureOfPremises = models.IntegerField(default=None, blank=True, null=True)
    EmployeeCountTotal = models.IntegerField(default=None, blank=True, null=True)
    EmployeeCountPermanent = models.IntegerField(default=None, blank=True, null=True)
    EmployeeCountTemporary = models.IntegerField(default=None, blank=True, null=True)
    EmployeeCountManagement = models.IntegerField(default=None, blank=True, null=True)
    KeyProductIncome = models.IntegerField(default=None, blank=True, null=True)
    MarketShare = models.FloatField(default=None, blank=True, null=True)
    Text1 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Text2 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Text3 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Text4 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Text5 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Text6 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Text7 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Text8 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Text9 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Text10 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Number1 = models.FloatField(default=None, blank=True, null=True)
    Number2 = models.FloatField(default=None, blank=True, null=True)
    Number3 = models.FloatField(default=None, blank=True, null=True)
    Number4 = models.FloatField(default=None, blank=True, null=True)
    Number5 = models.FloatField(default=None, blank=True, null=True)
    Number6 = models.FloatField(default=None, blank=True, null=True)
    Number7 = models.FloatField(default=None, blank=True, null=True)
    Number8 = models.FloatField(default=None, blank=True, null=True)
    Number9 = models.FloatField(default=None, blank=True, null=True)
    Number10 = models.FloatField(default=None, blank=True, null=True)
    Code1 = models.IntegerField(default=None, blank=True, null=True)
    Code2 = models.IntegerField(default=None, blank=True, null=True)
    Code3 = models.IntegerField(default=None, blank=True, null=True)
    Code4 = models.IntegerField(default=None, blank=True, null=True)
    Code5 = models.IntegerField(default=None, blank=True, null=True)
    Code6 = models.IntegerField(default=None, blank=True, null=True)
    Code7 = models.IntegerField(default=None, blank=True, null=True)
    Code8 = models.IntegerField(default=None, blank=True, null=True)
    Code9 = models.IntegerField(default=None, blank=True, null=True)
    Code10 = models.IntegerField(default=None, blank=True, null=True)
    Date1 = models.DateTimeField(default=None, blank=True, null=True)
    Date2 = models.DateTimeField(default=None, blank=True, null=True)
    Date3 = models.DateTimeField(default=None, blank=True, null=True)
    Date4 = models.DateTimeField(default=None, blank=True, null=True)
    Date5 = models.DateTimeField(default=None, blank=True, null=True)
    Date6 = models.DateTimeField(default=None, blank=True, null=True)
    Date7 = models.DateTimeField(default=None, blank=True, null=True)
    Date8 = models.DateTimeField(default=None, blank=True, null=True)
    Date9 = models.DateTimeField(default=None, blank=True, null=True)
    Date10 = models.DateTimeField(default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.BasePartyId)

    class Meta:
        verbose_name = 'BasePartyNonIndividual'
        verbose_name_plural = 'BasePartyNonIndividual'
        db_table = 'BasePartyNonIndividual'
