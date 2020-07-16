from django.db import models
from common.models.abstract import *
from common.models.general import ArrangementCategory, ArrangementClass


class ArrangementType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                      StatusRecordableModel, MakeableModel, CheckableModel):
    ArrangementTypeId = models.AutoField(primary_key=True, null=False)

    ArrangementCategory = models.ForeignKey(ArrangementCategory, null=True, blank=True, on_delete=models.CASCADE)
    ArrangementClass = models.ForeignKey(ArrangementClass, null=True, blank=True, on_delete=models.CASCADE)
    ArrangementTypeParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    ParentFlag = models.BooleanField(default=False)
    ExposureDriver = models.IntegerField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.ArrangementTypeId, self.Description)

    class Meta:
        verbose_name = 'ArrangementType'
        verbose_name_plural = 'ArrangementType'
        db_table = 'ArrangementType'
