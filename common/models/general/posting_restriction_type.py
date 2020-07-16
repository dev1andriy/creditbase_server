from django.db import models
from common.models.abstract import *


class PostingRestrictionType(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                             HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    PostingRestrictionTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.PostingRestrictionTypeId, self.Description)

    class Meta:
        verbose_name = 'PostingRestrictionType'
        verbose_name_plural = 'PostingRestrictionType'
        db_table = 'PostingRestrictionType'
