from django.db import models
from common.models.abstract import *


class Country(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
              StatusRecordableModel, MakeableModel, CheckableModel):
    CountryId = models.IntegerField(primary_key=True)
    TelPrefix = models.CharField(max_length=10, default=None, blank=True, null=True)\

    objects = models.Manager()

    def __str__(self):
        return "{} - {} - {}".format(self.CountryId, self.TelPrefix, self.Description)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Country'
        db_table = 'Country'
