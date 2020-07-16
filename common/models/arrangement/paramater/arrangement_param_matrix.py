from django.db import models
from django.contrib.postgres.fields import JSONField

from common.models.abstract import *
from common.models.general import *
from common.models.arrangement.paramater import ArrangementParam


class ArrangementParamMatrix(TimeStampedModel, InsertableModel, UpdateableModel, PrintableModel, RankableModel):
    ArrangementParamMatrixId = models.AutoField(primary_key=True, null=False, blank=False)
    ArrangementParamId = models.ForeignKey(
        ArrangementParam,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    ArrangementType = models.ForeignKey(
        ArrangementType,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    RequestType = models.ForeignKey(
        RequestType,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    ValueLimits = JSONField(null=True, blank=True)
    DisplayFlag = JSONField(null=True, blank=True)
    ModifyFlag = JSONField(null=True, blank=True)
    PrintFlag = JSONField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {} - {}".format(self.ArrangementParamMatrixId, self.ArrangementType, self.ArrangementParamId)

    class Meta:
        verbose_name = 'ArrangementParamMatrix'
        verbose_name_plural = 'ArrangementParamMatrix'
        db_table = 'ArrangementParamMatrix'
