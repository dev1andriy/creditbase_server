from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty


class RelatedStaff(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel, HostableModel, RankableModel,
                   PrintableModel):
    RelatedStaffId = models.IntegerField(primary_key=True)
    BasePartyId = models.OneToOneField(
        BaseParty,
        on_delete=models.CASCADE,
    )
    StaffId = models.IntegerField(default=None, blank=True, null=True)
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
    Comment = models.TextField(default=None, blank=True, null=True)
    StartDate = models.DateTimeField(default=None, blank=True, null=True)
    EndDate = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.RelatedStaffId, self.Description)

    class Meta:
        verbose_name = 'RelatedStaff'
        verbose_name_plural = 'RelatedStaff'
        db_table = 'RelatedStaff'
