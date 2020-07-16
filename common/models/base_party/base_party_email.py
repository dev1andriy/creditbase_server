from django.db import models

from common.models.abstract import *
from common.models.general import *


class BasePartyEmail(InsertableModel, UpdateableModel, RankableModel, HostValueFlagEditableModel, PrintableModel,
                     TimeStampedModel):
    BasePartyEmailId = models.AutoField(primary_key=True)
    AddressType = models.ForeignKey(
        AddressType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    BasePartyId = models.ForeignKey(
        'common.BaseParty',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    EmailType = models.ForeignKey(
        EmailType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PreferenceType = models.ForeignKey(
        PreferenceType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    EmailManual = models.CharField(max_length=50, default=None, blank=True, null=True)
    EmailHost = models.CharField(max_length=50, default=None, blank=True, null=True)
    EmailFinal = models.CharField(max_length=50, default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.BasePartyEmailId, self.EmailManual)

    class Meta:
        verbose_name = 'BasePartyEmail'
        verbose_name_plural = 'BasePartyEmail'
        db_table = 'BasePartyEmail'
