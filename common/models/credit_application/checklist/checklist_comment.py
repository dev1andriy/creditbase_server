from django.db import models

from common.models.abstract import *
from common.models.base_party import BaseParty
from common.models.credit_application import CreditApplication
from common.models.credit_application.checklist import ChecklistTemplate, ChecklistQuestion


class ChecklistComment(UpdateableModel, InsertableModel, TimeStampedModel):
    CommentId = models.AutoField(primary_key=True, null=False)
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
    CommentIdRelated = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Comment = models.TextField(default=None, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.CommentId)

    class Meta:
        verbose_name = 'ChecklistComment'
        verbose_name_plural = 'ChecklistComment'
        db_table = 'ChecklistComment'
