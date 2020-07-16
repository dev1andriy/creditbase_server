from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField

from common.models.general import *
from common.models.base_party import BaseParty


class CreditApplication(models.Model):
    CreditApplicationId = models.AutoField(primary_key=True, null=False)
    BasePartyId = models.ForeignKey(
        BaseParty,
        related_name='BasePartyCreditApplication',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ApplicationSource = models.ForeignKey(
        ApplicationSource,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    FinancialInstitution = models.ForeignKey(
        FinancialInstitution,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ApplicationType = models.ForeignKey(
        ApplicationType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    BusinessUnit = models.ForeignKey(
        BusinessUnit,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    PurposesApplicable = JSONField(blank=True, null=True)
    ProductsApplicable = JSONField(blank=True, null=True)
    CollateralsApplicable = JSONField(blank=True, null=True)
    ApplicationTemplate = models.ForeignKey(
        ApplicationTemplate,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    # ApplicationPurposes = JSONField(blank=True, null=True)
    WorkflowProcess = models.ForeignKey(
        WorkflowProcess,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    RequiredAuthorityLevel = models.ForeignKey(
        AuthorityLevel,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ApplicationStatus = models.ForeignKey(
        ApplicationStatus,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    ApplicationPriority = models.ForeignKey(
        ApplicationPriority,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    DecisionAuthorityLevel = models.ForeignKey(
        AuthorityLevel,
        related_name='DecisionAuthorityLevel',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    DecisionType = models.ForeignKey(
        DecisionType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    DeclineReason = models.ForeignKey(
        DeclineReason,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    # DecisionBy = models.ForeignKey(get_user_model,
    #                                on_delete=models.CASCADE,
    #                                null=True,
    #                                blank=True,
    #                                )
    DecisionDate = models.DateTimeField(default=None, null=True, blank=True)
    DecisionExpiryDate = models.DateTimeField(default=None, null=True, blank=True)
    # DecisionReviewFrequency
    DecisionReviewTenor = models.IntegerField(default=None, null=True, blank=True)
    DecisionNextReviewDate = models.DateTimeField(default=None, null=True, blank=True)
    # related in the future
    PrintFlag = models.IntegerField(default=None, null=True, blank=True)
    # ChecklistTemplates = JSONField(blank=True, null=True)
    TATNet = models.IntegerField(default=None, null=True, blank=True)
    TATGross = models.IntegerField(default=None, null=True, blank=True)
    ReceivedDate = models.DateTimeField(default=None, null=True, blank=True)
    InsertDate = models.DateTimeField(default=None, null=True, blank=True)
    LastUpdatedDate = models.DateTimeField(default=None, null=True, blank=True)
    LastReviewDate = models.DateTimeField(default=None, null=True, blank=True)
    LastWFLStepDate = models.DateTimeField(default=None, null=True, blank=True)
    ReceivedBy = models.ForeignKey(
        get_user_model(),
        related_name='ReceivedBy',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    InsertedBy = models.ForeignKey(
        get_user_model(),
        related_name='InsertedBy',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    LastUpdatedBy = models.ForeignKey(
        get_user_model(),
        related_name='LastUpdatedBy',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    LastReviewedBy = models.ForeignKey(
        get_user_model(),
        related_name='LastReviewedBy',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    LastWFLStepBy = models.ForeignKey(
        get_user_model(),
        related_name='LastWFLStepBy',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    CurrentWFLStepWith = models.IntegerField(default=None, blank=True, null=True)
    IsArchived = models.BooleanField(default=False, blank=True, null=True)
    ArchivedDate = models.DateTimeField(default=None, blank=True, null=True)
    ArchivedBy = models.ForeignKey(
        get_user_model(),
        related_name='ArchivedBy',
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.CreditApplicationId, self.BasePartyId)

    class Meta:
        verbose_name = 'CreditApplication'
        verbose_name_plural = 'CreditApplication'
        db_table = 'CreditApplication'
