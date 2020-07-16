from django.db import models
from common.models.abstract import *


class GovernanceType(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                     StatusRecordableModel, MakeableModel, CheckableModel):
    GovernanceTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.GovernanceTypeId, self.Description)

    class Meta:
        verbose_name = 'GovernanceType'
        verbose_name_plural = 'GovernanceType'
        db_table = 'GovernanceType'
