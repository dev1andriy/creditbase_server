from django.db import models
from common.models.abstract import *


class Industry(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
               StatusRecordableModel, MakeableModel, CheckableModel):
    IndustryId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.IndustryId, self.Description)

    class Meta:
        verbose_name = 'Industry'
        verbose_name_plural = 'Industry'
        db_table = 'Industry'
