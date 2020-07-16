from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.communication import Communication


class CommunicationDistribution(TimeStampedModel, InsertableModel, UpdateableModel):
    DistributionId = models.AutoField(primary_key=True, null=False)
    CommunicationId = models.ForeignKey(
        Communication,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    RecipientType = models.ForeignKey(
        RecipientType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    AddressTo = models.CharField(max_length=100, null=True, blank=True, default=None)
    # Temp field type / In the future will be foreign key
    RecipientName = models.IntegerField(null=True, blank=True, default=None)
    DistributionStatus = models.ForeignKey(
        DistributionStatus,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.DistributionId)

    class Meta:
        verbose_name = 'CommunicationDistribution'
        verbose_name_plural = 'CommunicationDistribution'
        db_table = 'CommunicationDistribution'

