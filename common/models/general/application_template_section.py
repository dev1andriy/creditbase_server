from django.db import models
from common.models.abstract import *


# will be improved
class ApplicationTemplateSection(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                                 StatusRecordableModel, MakeableModel, CheckableModel):
    ApplicationTemplateSectionId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.ApplicationTemplateSectionId)

    class Meta:
        verbose_name = 'ApplicationTemplateSection'
        verbose_name_plural = 'ApplicationTemplateSection'
        db_table = 'ApplicationTemplateSection'

