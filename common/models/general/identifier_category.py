from django.db import models
from common.models.abstract import *


class IdentifierCategory(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                         HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    IdentifierCategoryId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.IdentifierCategoryId, self.Description)

    class Meta:
        verbose_name = 'IdentifierCategory'
        verbose_name_plural = 'IdentifierCategory'
        db_table = 'IdentifierCategory'
