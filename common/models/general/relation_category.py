from django.db import models
from common.models.abstract import *


class RelationCategory(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                       HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    RelationCategoryId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.RelationCategoryId, self.Description)

    class Meta:
        verbose_name = 'RelationCategory'
        verbose_name_plural = 'RelationCategory'
        db_table = 'RelationCategory'
