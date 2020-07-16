from django.db import models
from django.contrib.postgres.fields import JSONField

from common.models.abstract import *
from common.models.general import *
from common.models.general import Currency as CurrencyModel
from common.models.base_party import BaseParty


class Account(TimeStampedModel, InsertableModel, UpdateableModel, PrintableModel, RankableModel):
    AccountId = models.AutoField(primary_key=True, null=False, blank=False)
    HostId = models.ForeignKey(
        Host,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    AccountIdHost = models.CharField(max_length=50, null=True, blank=True)
    BasePartyId = models.ForeignKey(
        BaseParty,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    AccountIdOther1 = models.CharField(max_length=50, null=True, blank=True)
    AccountIdOther2 = models.CharField(max_length=50, null=True, blank=True)
    AccountTitle = models.CharField(max_length=100, null=True, blank=True)
    AccountCategory = models.ForeignKey(
        AccountCategory,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    AccountClass = models.ForeignKey(
        AccountClass,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    AccountType = models.ForeignKey(
        AccountType,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    FinancialInstitution = models.ForeignKey(
        FinancialInstitution,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    BusinessUnit = models.ForeignKey(
        BusinessUnit,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    Currency = models.ForeignKey(
        CurrencyModel,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    AccountStatus = models.ForeignKey(
        AccountStatus,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    OriginationDate = models.DateTimeField(null=True, blank=True)
    AccountOfficer = models.ForeignKey(
        AccountOfficer,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    OverdraftAllowedFlag = models.ForeignKey(
        Flag,
        related_name="OverdraftAllowedFlag",
        on_delete=models.CASCADE,
        default=None, null=True, blank=True)
    LimitId = models.CharField(max_length=50, null=True, blank=True)
    LimitCurrency = models.ForeignKey(
        CurrencyModel,
        related_name='LimitCurrency',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    LimitAmount = models.FloatField(null=True, blank=True)
    BalanceBook = models.FloatField(null=True, blank=True)
    BalanceAvailable = models.FloatField(null=True, blank=True)
    BalanceDate = models.DateTimeField(null=True, blank=True)
    LastTransactionDate = models.DateTimeField(null=True, blank=True)
    JointAccountFlag = models.ForeignKey(
        Flag,
        related_name="JointAccountFlag",
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    LiquidationAccountFlag = models.ForeignKey(
        Flag,
        related_name="LiquidationAccountFlag",
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    LienMarkedFlag = models.ForeignKey(
        Flag,
        related_name="LienMarkedFlag",
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    CollateralizableFlag = models.ForeignKey(
        Flag,
        related_name="CollateralizableFlag",
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    PostingRestrictionType = JSONField(null=True, blank=True)
    EditHostValuesFlag = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AccountId, self.AccountTitle)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Account'
        db_table = 'Account'
