from django.db import models
from common.models.abstract import *
from django.contrib.postgres.fields import JSONField


class ApplicationTemplate(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                          StatusRecordableModel, MakeableModel, CheckableModel):
    ApplicationTemplateId = models.AutoField(primary_key=True, null=False)
    ProfileTypes = JSONField(blank=True, null=True)
    ApplicationTypes = JSONField(blank=True, null=True)
    ApplicationPurposes = JSONField(blank=True, null=True)
    ProductTypesApplicable = JSONField(blank=True, null=True)
    CollateralTypesApplicable = JSONField(blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.ApplicationTemplateId)

    class Meta:
        verbose_name = 'ApplicationTemplate'
        verbose_name_plural = 'ApplicationTemplate'
        db_table = 'ApplicationTemplate'
