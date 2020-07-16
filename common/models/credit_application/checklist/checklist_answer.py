from django.db import models
from django.contrib.auth import get_user_model

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty
from common.models.credit_application import CreditApplication
from common.models.credit_application.checklist import ChecklistTemplate, ChecklistQuestion, ChecklistResponse


class ChecklistAnswer(UpdateableModel, InsertableModel, TimeStampedModel):
    AnswerId = models.AutoField(primary_key=True, null=False)
    BasePartyId = models.ForeignKey(
        BaseParty,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CreditApplicationId = models.ForeignKey(
        CreditApplication,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )

    # ModuleId
    TemplateId = models.ForeignKey(
        ChecklistTemplate,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    QuestionId = models.ForeignKey(
        ChecklistQuestion,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ResponseAutoId = models.IntegerField(default=None, null=True, blank=True)
    ResponseAutoScore = models.FloatField(default=None, null=True, blank=True)
    ResponseAutoDate = models.DateTimeField(default=None, blank=True, null=True)
    ResponseAutoBy = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Response1Id = models.ForeignKey(
        ChecklistResponse,
        related_name='Response1Id',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Response1Score = models.FloatField(default=None, null=True, blank=True)
    Response1Date = models.DateTimeField(default=None, blank=True, null=True)
    Response1By = models.ForeignKey(
        get_user_model(),
        related_name='Response1By',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Response2Id = models.ForeignKey(
        ChecklistResponse,
        related_name='Response2Id',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Response2Score = models.FloatField(default=None, null=True, blank=True)
    Response2Date = models.DateTimeField(default=None, blank=True, null=True)
    Response2By = models.ForeignKey(
        get_user_model(),
        related_name='Response2By',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Response3Id = models.ForeignKey(
        ChecklistResponse,
        related_name='Response3Id',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Response3Score = models.FloatField(default=None, null=True, blank=True)
    Response3Date = models.DateTimeField(default=None, blank=True, null=True)
    Response3By = models.ForeignKey(
        get_user_model(),
        related_name='Response3By',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Response4Id = models.ForeignKey(
        ChecklistResponse,
        related_name='Response4Id',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Response4Score = models.FloatField(default=None, null=True, blank=True)
    Response4Date = models.DateTimeField(default=None, blank=True, null=True)
    Response4By = models.ForeignKey(
        get_user_model(),
        related_name='Response4By',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    # AlertId = models.ForeignKey(
    #     ,
    #     on_delete=models.CASCADE,
    #     default=None, blank=True, null=True
    # )

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.AnswerId)

    class Meta:
        verbose_name = 'ChecklistAnswer'
        verbose_name_plural = 'ChecklistAnswer'
        db_table = 'ChecklistAnswer'
