from django.db import models
from django.contrib.postgres.fields import JSONField

from common.models.abstract import *
from common.models.general import *
from common.models.credit_application.checklist.checklist_tab import ChecklistTab


class ChecklistTemplate(UpdateableModel, InsertableModel, TimeStampedModel):
    TemplateId = models.AutoField(primary_key=True, null=False)
    TemplateType = models.ForeignKey(
        TemplateType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ChecklistTabId = models.ForeignKey(
        ChecklistTab,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )

    # it will be improved
    ModuleId = models.IntegerField(null=True, blank=True)

    Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=300, null=True, blank=True)
    Status = models.ForeignKey(
        ChecklistStatus,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )

    # it will be improved
    TemplateVersion = models.IntegerField(null=True, blank=True)

    ProfileTypes = JSONField(blank=True, null=True)
    ApplicationTypes = JSONField(blank=True, null=True)
    ApplicationPurposes = JSONField(blank=True, null=True)
    ProductTypesApplicable = JSONField(blank=True, null=True)
    CollateralTypesApplicable = JSONField(blank=True, null=True)

    # it will be improved
    Response1Flag = models.BooleanField(default=True, null=True, blank=True)
    Response2Flag = models.BooleanField(default=True, null=True, blank=True)
    Response3Flag = models.BooleanField(default=True, null=True, blank=True)
    Response4Flag = models.BooleanField(default=True, null=True, blank=True)
    Response1Role = models.CharField(max_length=100, null=True, blank=True)
    Response2Role = models.CharField(max_length=100, null=True, blank=True)
    Response3Role = models.CharField(max_length=100, null=True, blank=True)
    Response4Role = models.CharField(max_length=100, null=True, blank=True)

    AutoLabel = models.CharField(max_length=10, null=True, blank=True)
    Response1Label = models.CharField(max_length=10, null=True, blank=True)
    Response2Label = models.CharField(max_length=10, null=True, blank=True)
    Response3Label = models.CharField(max_length=10, null=True, blank=True)
    Response4Label = models.CharField(max_length=10, null=True, blank=True)
    ScorePass = models.FloatField(null=True, blank=True)
    ScoreFail = models.FloatField(null=True, blank=True)
    ScorePending = models.FloatField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.TemplateId)

    class Meta:
        verbose_name = 'ChecklistTemplate'
        verbose_name_plural = 'ChecklistTemplate'
        db_table = 'ChecklistTemplate'
