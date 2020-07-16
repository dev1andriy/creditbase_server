from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty


class BasePartyIndividual(InsertableModel, UpdateableModel):
    BasePartyId = models.OneToOneField(
        BaseParty,
        related_name='Individual',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    FirstName = models.CharField(max_length=50, default=None, blank=True, null=True)
    MiddleName = models.CharField(max_length=50, default=None, blank=True, null=True)
    LastName = models.CharField(max_length=50, default=None, blank=True, null=True)
    OtherNames = models.CharField(max_length=50, default=None, blank=True, null=True)
    Prefix = models.ForeignKey(
        Prefix,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Suffix = models.ForeignKey(
        Suffix,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    BirthDate = models.DateTimeField(default=None, blank=True, null=True)
    CountryNationality = models.IntegerField(default=None, blank=True, null=True)
    CountryResidence = models.IntegerField(default=None, blank=True, null=True)
    MaritalStatus = models.ForeignKey(
        MaritalStatus,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    EducationLevel = models.ForeignKey(
        EducationLevel,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ResidentialStatus = models.ForeignKey(
        ResidentialStatus,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CurrentAddressId = models.IntegerField(default=None, blank=True, null=True)
    DurationAtAddress = models.FloatField(default=None, blank=True, null=True)
    PreviousAddressId = models.IntegerField(default=None, blank=True, null=True)
    DependantsCount = models.IntegerField(default=None, blank=True, null=True)
    EmploymentType = models.ForeignKey(
        EmploymentType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    EmployerType = models.ForeignKey(
        EmployerType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    EmployerCurrent = models.CharField(max_length=100, default=None, blank=True, null=True)
    EmployerPrevious = models.CharField(max_length=100, default=None, blank=True, null=True)
    EmploymentDate = models.DateTimeField(default=None, blank=True, null=True)
    ConfirmationStatus = models.ForeignKey(
        ConfirmationStatus,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    RetirementAge = models.IntegerField(default=None, blank=True, null=True)
    ContractTenure = models.IntegerField(default=None, blank=True, null=True)
    ContractExpiryDate = models.DateTimeField(default=None, blank=True, null=True)
    EmployeeId = models.CharField(max_length=20, default=None, blank=True, null=True)
    EmployerSector = models.ForeignKey(
        EmployerSector,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ExperienceSector = models.FloatField(default=None, blank=True, null=True)
    Occupation = models.CharField(max_length=100, default=None, blank=True, null=True)
    ExperienceOccupation = models.FloatField(default=None, blank=True, null=True)
    ManagementLevel = models.ForeignKey(
        ManagementLevel,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    JobGrade = models.ForeignKey(
        JobGrade,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    EmployerTelephoneId = models.IntegerField(default=None, blank=True, null=True)
    EmployerAddressId = models.IntegerField(default=None, blank=True, null=True)
    SalaryFrequency = models.ForeignKey(
        SalaryFrequency,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    SalaryPayMode = models.ForeignKey(
        SalaryPayMode,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    IncomeGross = models.FloatField(default=None, blank=True, null=True)
    IncomeOther = models.FloatField(default=None, blank=True, null=True)
    IncomeTotal = models.FloatField(default=None, blank=True, null=True)
    IncomeNet = models.FloatField(default=None, blank=True, null=True)
    IncomeDisposable = models.FloatField(default=None, blank=True, null=True)
    DeductionsStatutory = models.FloatField(default=None, blank=True, null=True)
    DeductionsOther = models.FloatField(default=None, blank=True, null=True)
    DeductionsTotal = models.FloatField(default=None, blank=True, null=True)
    ExpensesLiving = models.FloatField(default=None, blank=True, null=True)
    ExpensesOther = models.FloatField(default=None, blank=True, null=True)
    ExpensesTotal = models.FloatField(default=None, blank=True, null=True)
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
        return "{} - {} - {} - {}".format(self.EmployeeId, self.FirstName, self.LastName, self.LastName)

    class Meta:
        verbose_name = 'BasePartyIndividual'
        verbose_name_plural = 'BasePartyIndividual'
        db_table = 'BasePartyIndividual'
