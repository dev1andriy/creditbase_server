from django.db import models
from common.models.abstract import *


class DecisionMakingType(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                         StatusRecordableModel, MakeableModel, CheckableModel):
    DecisionMakingTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.DecisionMakingTypeId, self.Description)

    class Meta:
        verbose_name = 'DecisionMakingType'
        verbose_name_plural = 'DecisionMakingType'
        db_table = 'DecisionMakingType'
