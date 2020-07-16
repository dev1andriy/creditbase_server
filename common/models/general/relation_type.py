from django.db import models
from common.models.abstract import *
from common.models.general import RelationCategory


class RelationType(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                   StatusRecordableModel, MakeableModel, CheckableModel):
    RelationTypeId = models.IntegerField(primary_key=True)
    RelationCategory = models.ForeignKey(RelationCategory, null=False, blank=False, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.RelationTypeId, self.Description)

    class Meta:
        verbose_name = 'RelationType'
        verbose_name_plural = 'RelationType'
        db_table = 'RelationType'
