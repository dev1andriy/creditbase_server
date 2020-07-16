from django.db import models
from common.models.abstract import *


class RelatedItemType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                      StatusRecordableModel, MakeableModel, CheckableModel):
    RelatedItemTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.RelatedItemTypeId)

    class Meta:
        verbose_name = 'RelatedItemType'
        verbose_name_plural = 'RelatedItemType'
        db_table = 'RelatedItemType'
