from django.db import models
from common.models.abstract import *


class ChecklistTemplateStatus(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                              StatusRecordableModel, MakeableModel, CheckableModel):
    ChecklistTemplateStatusId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.ChecklistTemplateStatusId)

    class Meta:
        verbose_name = 'ChecklistTemplateStatus'
        verbose_name_plural = 'ChecklistTemplateStatus'
        db_table = 'ChecklistTemplateStatus'

