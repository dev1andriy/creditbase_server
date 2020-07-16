from django.db import models

from common.models.abstract import *
from common.models.base_party import BaseParty
from common.models.credit_application import CreditApplication
from common.models.credit_application.checklist import ChecklistTemplate, ChecklistQuestion
from common.models.document import Document


class ChecklistDocument(UpdateableModel, InsertableModel, TimeStampedModel):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    DocumentId = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        null=False, blank=False
    )
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
    FileType = models.CharField(max_length=100, null=True, blank=True)
    FileSize = models.CharField(max_length=100, null=True, blank=True)

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

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.DocumentId)

    class Meta:
        verbose_name = 'ChecklistDocument'
        verbose_name_plural = 'ChecklistDocument'
        db_table = 'ChecklistDocument'
