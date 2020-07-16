from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty


class Communication(TimeStampedModel, InsertableModel, UpdateableModel):
    CommunicationId = models.AutoField(primary_key=True, null=False)
    BasePartyId = models.ForeignKey(
        BaseParty,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CommunicationType = models.ForeignKey(
        CommunicationType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CommunicationStatus = models.ForeignKey(
        CommunicationStatus,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CommunicationQueue = models.ForeignKey(
        CommunicationQueue,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CommunicationSource = models.ForeignKey(
        CommunicationSource,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CommunicationSourceId = models.IntegerField(null=True, blank=True, default=None)
    ReadStatus = models.ForeignKey(
        ReadStatus,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    # Temp field type / In the future will be foreign key
    StaffSenderId = models.IntegerField(null=True, blank=True, default=None)
    AddressFrom = models.CharField(max_length=100, null=True, blank=True, default=None)
    AddressTo = models.TextField(null=True, blank=True, default=None)
    AddressCC = models.TextField(null=True, blank=True, default=None)
    AddressBCC = models.TextField(null=True, blank=True, default=None)
    TelFormatted = models.CharField(max_length=50, null=True, blank=True, default=None)
    Subject = models.CharField(max_length=100, null=True, blank=True, default=None)
    Body = models.TextField(null=True, blank=True, default=None)
    Priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    DueDate = models.DateTimeField(null=True, blank=True, default=None)
    DraftDate = models.DateTimeField(null=True, blank=True, default=None)
    QueuedDate = models.DateTimeField(null=True, blank=True, default=None)
    SentDate = models.DateTimeField(null=True, blank=True, default=None)

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.CommunicationId)

    class Meta:
        verbose_name = 'Communication'
        verbose_name_plural = 'Communication'
        db_table = 'Communication'
