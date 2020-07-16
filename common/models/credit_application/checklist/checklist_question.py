from django.db import models
from django.contrib.postgres.fields import JSONField

from common.models.abstract import *
from common.models.credit_application.checklist import ChecklistTemplate


class ChecklistQuestion(UpdateableModel, InsertableModel, TimeStampedModel):
    QuestionId = models.AutoField(primary_key=True, null=False)
    QuestionIdHost = models.CharField(max_length=20, null=True, blank=True)

    # it will be improved
    ParentSectionFlag = models.BooleanField(default=False, null=False)
    ParentSectionId = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )

    Description = models.CharField(max_length=300, null=True, blank=True)
    FormulaName = models.IntegerField(null=True, blank=True)
    OrderingRank = models.IntegerField(null=True, blank=True)
    TemplateId = models.ForeignKey(
        ChecklistTemplate,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Weight = models.FloatField(null=True, blank=True)

    # it will be improved
    AutoAttributeFlag = models.IntegerField(null=True, blank=True)
    AutoAttributeId = models.IntegerField(null=True, blank=True)
    HelpTextFlag = models.IntegerField(null=True, blank=True)

    HelpText = models.TextField(null=True, blank=True)

    # it will be improved
    CommentsFlag = models.IntegerField(null=True, blank=True)
    DisplayScoreFlag = models.IntegerField(null=True, blank=True)
    DisplayWeightFlag = models.IntegerField(null=True, blank=True)
    WeightFormulaId = models.IntegerField(null=True, blank=True)
    ScoreFormulaId = models.IntegerField(null=True, blank=True)
    RandomizeFlag = models.IntegerField(null=True, blank=True)
    DocumentsFlag = models.BooleanField(default=False)

    # Response1Label = models.CharField(max_length=10, null=True, blank=True)
    # Response2Label = models.CharField(max_length=10, null=True, blank=True)
    # Response3Label = models.CharField(max_length=10, null=True, blank=True)
    # Response4Label = models.CharField(max_length=10, null=True, blank=True)

    DocumentType = JSONField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.Description, self.QuestionId)

    class Meta:
        verbose_name = 'ChecklistQuestion'
        verbose_name_plural = 'ChecklistQuestion'
        db_table = 'ChecklistQuestion'
