from django.db import models

from common.models.abstract import *
from common.models.general import *


class BasePartyTelephone(InsertableModel, UpdateableModel, RankableModel, HostValueFlagEditableModel, PrintableModel, TimeStampedModel):
    BasePartyTelephoneId = models.AutoField(primary_key=True)
    BasePartyId = models.ForeignKey(
        'common.BaseParty',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    TelephoneType = models.ForeignKey(
        TelephoneType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PreferenceType = models.ForeignKey(
        PreferenceType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    TelephonePart1 = models.CharField(max_length=20, default=None, blank=True, null=True)
    TelephonePart2 = models.CharField(max_length=20, default=None, blank=True, null=True)
    TelephonePart3 = models.CharField(max_length=20, default=None, blank=True, null=True)
    TelephonePart4 = models.CharField(max_length=20, default=None, blank=True, null=True)
    TelFormattedManual = models.CharField(max_length=50, default=None, blank=True, null=True)
    TelFormattedHost = models.CharField(max_length=50, default=None, blank=True, null=True)
    TelFormattedFinal = models.CharField(max_length=50, default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.BasePartyTelephoneId, self.TelFormattedFinal)

    class Meta:
        verbose_name = 'BasePartyTelephone'
        verbose_name_plural = 'BasePartyTelephone'
        db_table = 'BasePartyTelephone'
