from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty


class BasePartyIdentifier(InsertableModel, UpdateableModel, PrintableModel):
    BasePartyIdentifierId = models.AutoField(primary_key=True)
    BasePartyId = models.ForeignKey(
        BaseParty,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    IdentifierCategory = models.ForeignKey(
        IdentifierCategory,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    IdentifierType = models.ForeignKey(
        IdentifierType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Identifier = models.IntegerField(default=None, blank=True, null=True)
    StartDate = models.DateTimeField(default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {} - {}".format(self.BasePartyIdentifierId, self.Identifier, self.IdentifierType)

    class Meta:
        verbose_name = 'BasePartyIdentifier'
        verbose_name_plural = 'BasePartyIdentifier'
        db_table = 'BasePartyIdentifier'
