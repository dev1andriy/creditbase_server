from django.db import models
from common.models.abstract import *


class AssetClassification(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                          StatusRecordableModel, MakeableModel, CheckableModel):
    AssetClassificationId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AssetClassificationId, self.Description)

    class Meta:
        verbose_name = 'AssetClassification'
        verbose_name_plural = 'AssetClassification'
        db_table = 'AssetClassification'
