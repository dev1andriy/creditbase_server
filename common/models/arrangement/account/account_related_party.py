from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty
from common.models.arrangement.account import Account


class AccountRelatedParty(TimeStampedModel, InsertableModel, UpdateableModel, PrintableModel, RankableModel):
    AccountRelatedPartyId = models.AutoField(primary_key=True, null=False, blank=False)
    AccountId = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    RelatedPartyId = models.ForeignKey(
        BaseParty,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    RelatedPartyName = models.CharField(max_length=100, null=True, blank=True)
    RelationCategory = models.ForeignKey(
        RelationCategory,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    RelationType = models.ForeignKey(
        RelationType,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    IsPrimaryAccountOwner = models.ForeignKey(
        Flag,
        related_name='AccountRelatedPartyIsPrimaryAccountOwner',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    Comment = models.TextField(null=True, blank=True)
    StartDate = models.DateTimeField(null=True, blank=True)
    EndDate = models.DateTimeField(null=True, blank=True)
    EditHostValuesFlag = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):
        return '{} - {} - {}'.format(self.AccountRelatedPartyId, self.AccountId, self.RelatedPartyId)

    class Meta:
        verbose_name = 'AccountRelatedParty'
        verbose_name_plural = 'AccountRelatedParty'
        db_table = 'AccountRelatedParty'
