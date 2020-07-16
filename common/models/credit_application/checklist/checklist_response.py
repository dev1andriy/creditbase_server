from django.db import models
from django.contrib.postgres.fields import JSONField

from common.models.abstract import *
from common.models.credit_application.checklist import ChecklistQuestion


class ChecklistResponse(UpdateableModel, InsertableModel, TimeStampedModel, RankableModel):
    ResponseId = models.AutoField(primary_key=True, null=False)
    ResponseIdHost = models.IntegerField(default=None, null=True, blank=True)
    QuestionId = models.ForeignKey(
        ChecklistQuestion,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Description = models.CharField(max_length=100, default=None, null=True, blank=True)
    Points = models.FloatField(default=None, null=True, blank=True)
    FollowupQuestionId = JSONField(blank=True, null=True)

    # AlertEnabledFlag
    # AlertClass
    # AlertSource
    # AlertType
    # AlertSeverity

    objects = models.Manager()

    def __str__(self):
        return "{} - {} - {}".format(self.QuestionId, self.ResponseId, self.Description)

    class Meta:
        verbose_name = 'ChecklistResponse'
        verbose_name_plural = 'ChecklistResponse'
        db_table = 'ChecklistResponse'
