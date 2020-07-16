from django.db import models

from common.models.abstract import *
from common.models.general import *


class CreditApplicationTemplateState(UpdateableModel, InsertableModel, TimeStampedModel):
    CreditApplicationId = models.ForeignKey(
        'common.CreditApplication',
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    ApplicationTemplate = models.ForeignKey(
        ApplicationTemplate,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ApplicationTemplateSection = models.ForeignKey(
        ApplicationTemplateSection,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ApplicationTemplateSectionState = models.IntegerField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.CreditApplicationId)

    class Meta:
        verbose_name = 'CreditApplicationTemplateState'
        verbose_name_plural = 'CreditApplicationTemplateState'
        db_table = 'CreditApplicationTemplateState'
