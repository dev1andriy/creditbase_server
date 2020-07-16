from django.db import models
from common.models.abstract import *


class TemplateType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                   StatusRecordableModel, MakeableModel, CheckableModel):
    TemplateTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.TemplateTypeId)

    class Meta:
        verbose_name = 'TemplateType'
        verbose_name_plural = 'TemplateType'
        db_table = 'TemplateType'

