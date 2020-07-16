from django.db import models

from common.models.abstract import *
from common.models.general import *


class BasePartyAddress(InsertableModel, UpdateableModel, RankableModel, HostValueFlagEditableModel, PrintableModel):
    BasePartyAddressId = models.AutoField(primary_key=True)
    BasePartyId = models.ForeignKey(
        'common.BaseParty',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    AddressType = models.ForeignKey(
        AddressType,
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
    Level1Location = models.CharField(max_length=100, default=None, blank=True, null=True)
    Level2Location = models.CharField(max_length=100, default=None, blank=True, null=True)
    Level3Location = models.CharField(max_length=100, default=None, blank=True, null=True)
    # Level1Location = models.ForeignKey(
    #     Location,
    #     related_name='Location1',
    #     on_delete=models.CASCADE,
    #     db_column='Level1Location',
    #     default=None, blank=True, null=True
    # )
    # Level2Location = models.ForeignKey(
    #     Location,
    #     related_name='Location2',
    #     on_delete=models.CASCADE,
    #     db_column='Level2Location',
    #     default=None, blank=True, null=True
    # )
    # Level3Location = models.ForeignKey(
    #     Location,
    #     related_name='Location3',
    #     on_delete=models.CASCADE,
    #     db_column='Level3Location',
    #     default=None, blank=True, null=True
    # )
    # PostCode = models.IntegerField(default=None, blank=True, null=True)
    PostCode = models.CharField(max_length=50, default=None, blank=True, null=True)
    Street1 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Street2 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Street3 = models.CharField(max_length=50, default=None, blank=True, null=True)
    AddressManual = models.CharField(max_length=150, default=None, blank=True, null=True)
    AddressHost = models.CharField(max_length=150, default=None, blank=True, null=True)
    AddressFinal = models.CharField(max_length=150, default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {} - {}".format(self.BasePartyAddressId, self.AddressType, self.AddressFinal)

    class Meta:
        verbose_name = 'BasePartyAddress'
        verbose_name_plural = 'BasePartyAddress'
        db_table = 'BasePartyAddress'
