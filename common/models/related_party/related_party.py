from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty


class RelatedParty(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                   StatusRecordableModel, MakeableModel, CheckableModel, HostValueFlagEditableModel, RankableModel,
                   PrintableModel):
    RelatedPartyId = models.AutoField(primary_key=True)
    BaseParty1Id = models.ForeignKey(
        BaseParty,
        related_name='BaseParty1',
        on_delete=models.CASCADE,
        null=True
    )
    BaseParty2Id = models.ForeignKey(
        BaseParty,
        related_name='BaseParty2',
        on_delete=models.CASCADE,
        null=True
    )
    RelationCategory = models.ForeignKey(
        RelationCategory,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    RelationType = models.ForeignKey(
        RelationType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PercentOwnership = models.FloatField(default=None, blank=True, null=True)
    PercentVoting = models.FloatField(default=None, blank=True, null=True)
    SharesCount = models.IntegerField(default=None, blank=True, null=True)
    SharesValue = models.FloatField(default=None, blank=True, null=True)
    GuaranteeType = models.ForeignKey(
        GuaranteeType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PercentGuaranteed = models.FloatField(default=None, blank=True, null=True)
    MaxGuaranteeAmount = models.FloatField(default=None, blank=True, null=True)
    IsControllingOwner = models.BooleanField(default=False)
    LinkFinancials = models.BooleanField(default=False)
    LinkBankingInfo = models.BooleanField(default=False)
    LinkApplications = models.BooleanField(default=False)
    Comment = models.TextField(default=None, blank=True, null=True)
    StartDate = models.DateTimeField(default=None, blank=True, null=True)
    EndDate = models.DateTimeField(default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.RelatedPartyId, self.Description)

    class Meta:
        verbose_name = 'RelatedParty'
        verbose_name_plural = 'RelatedParty'
        db_table = 'RelatedParty'
