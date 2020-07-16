from django.db import models
from common.models.abstract import *


class ChecklistTemplateType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                            StatusRecordableModel, MakeableModel, CheckableModel):
    ChecklistTemplateTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.ChecklistTemplateTypeId)

    class Meta:
        verbose_name = 'ChecklistTemplateType'
        verbose_name_plural = 'ChecklistTemplateType'
        db_table = 'ChecklistTemplateType'

