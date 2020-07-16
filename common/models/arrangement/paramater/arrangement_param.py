from django.db import models
from django.contrib.postgres.fields import JSONField

from common.models.abstract import *
from common.models.general import *


class ArrangementParam(TimeStampedModel, InsertableModel, UpdateableModel, PrintableModel, RankableModel):
    ArrangementParamId = models.AutoField(primary_key=True, null=False, blank=False)
    ArrangementCategory = models.ForeignKey(
        ArrangementCategory,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    ArrangementParamCategory = models.ForeignKey(
        ArrangementParamCategory,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    FieldType = models.IntegerField(null=True, blank=True)
    Name1 = models.CharField(max_length=50, null=True, blank=True)
    Name2 = models.CharField(max_length=50, null=True, blank=True)
    Name3 = models.CharField(max_length=50, null=True, blank=True)
    Name4 = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    Description1 = models.CharField(max_length=50, null=True, blank=True)
    Description2 = models.CharField(max_length=50, null=True, blank=True)
    Description3 = models.CharField(max_length=50, null=True, blank=True)
    Description4 = models.CharField(max_length=50, null=True, blank=True)
    Description5 = models.CharField(max_length=50, null=True, blank=True)
    Mandatory = models.BooleanField(default=False)

    ActiveFlag = models.BooleanField(default=True)
    AllowNullFlag = models.BooleanField(default=True)
    # MaskType
    # ScaleType
    # AlignmentType
    # RoundingType
    # MonetaryFlag

    # to be updated
    DataSourceType1 = models.CharField(max_length=100, null=True, blank=True)
    DataSourceType2 = models.CharField(max_length=100, null=True, blank=True)
    DataSourceType3 = models.CharField(max_length=100, null=True, blank=True)

    URL1 = models.CharField(max_length=200, null=True, blank=True)
    URL2 = models.CharField(max_length=200, null=True, blank=True)
    URL3 = JSONField(null=True, blank=True)

    # to be updated
    Query1 = models.CharField(max_length=100, null=True, blank=True)
    Query2 = models.CharField(max_length=100, null=True, blank=True)
    Query3 = models.CharField(max_length=100, null=True, blank=True)
    TotalType = models.CharField(max_length=100, null=True, blank=True)

    IdHost = models.CharField(max_length=20, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.ArrangementParamId, self.Name2)

    class Meta:
        verbose_name = 'ArrangementParam'
        verbose_name_plural = 'ArrangementParam'
        db_table = 'ArrangementParam'
