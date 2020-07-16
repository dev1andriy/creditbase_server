from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.base_party.base_party_address import BasePartyAddress
from common.models.base_party.base_party_telephone import BasePartyTelephone
from common.models.base_party.base_party_email import BasePartyEmail


class BaseParty(InsertableModel, UpdateableModel, TimeStampedModel):
    BasePartyId = models.AutoField(primary_key=True)
    HostId = models.ForeignKey(
        Host,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    BasePartyHostId = models.CharField(max_length=50, default=None, blank=True, null=True)
    BasePartyName = models.CharField(max_length=200, default=None, blank=True, null=True)
    LegalEntityType = models.IntegerField(default=None, blank=True, null=True)
    PrimaryLegalIdType = models.IntegerField(default=None, blank=True, null=True)
    PrimaryLegalId = models.CharField(max_length=50, default=None, blank=True, null=True)
    BasePartyType = models.ForeignKey(
        BasePartyType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ProfileType = models.ForeignKey(
        ProfileType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    RelationshipStartDate = models.DateTimeField(default=None, blank=True, null=True)
    FinancialInstitution = models.ForeignKey(
        FinancialInstitution,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    BusinessUnit = models.ForeignKey(
        BusinessUnit,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CRMPortfolio = models.ForeignKey(
        CRMPortfolio,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CRMStrategy = models.ForeignKey(
        CRMStrategy,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PrimaryEmailId = models.ForeignKey(
        BasePartyEmail,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PrimaryTelephoneId = models.ForeignKey(
        BasePartyTelephone,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PrimaryContactId = models.ForeignKey(
        BasePartyAddress,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PrimaryRM = models.IntegerField(default=None, blank=True, null=True)
    EditHostValuesFlag = models.IntegerField(default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.BasePartyId, self.BasePartyName)

    class Meta:
        verbose_name = 'BaseParty'
        verbose_name_plural = 'BaseParty'
        db_table = 'BaseParty'
