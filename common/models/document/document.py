from django.db import models
from django.contrib.auth import get_user_model

from common.models.abstract import *
from common.models.general import *
from common.models.base_party import BaseParty
from common.models.credit_application import CreditApplication


class Document(TimeStampedModel, InsertableModel, UpdateableModel):
    DocumentId = models.AutoField(primary_key=True, null=False)
    BasePartyId = models.ForeignKey(
        BaseParty,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    # Temp field type / In the future will be foreign key
    CreditApplicationId = models.ForeignKey(
        CreditApplication,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    DocumentType = models.ForeignKey(
        DocumentType,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    DocumentStatus = models.ForeignKey(
        DocumentStatus,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    Name1 = models.CharField(max_length=50, null=True, blank=True, default=None)
    Name2 = models.CharField(max_length=50, null=True, blank=True, default=None)
    Description1 = models.CharField(max_length=50, null=True, blank=True, default=None)
    Description2 = models.CharField(max_length=50, null=True, blank=True, default=None)
    DocumentIdType = models.ForeignKey(
        DocumentIdType,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    CharDocumentId = models.CharField(max_length=50, null=True, blank=True, default=None)
    # FileType = models.ForeignKey(
    #     FileType,
    #     on_delete=models.CASCADE,
    #     default=None, null=True, blank=True
    # )
    FileType = models.CharField(max_length=100, null=True, blank=True)
    FileName = models.CharField(max_length=200, null=True, blank=True, default=None)
    FileURL = models.CharField(max_length=200, null=True, blank=True, default=None)
    # FileSize = models.FloatField(null=True, blank=True, default=None)
    FileSize = models.CharField(max_length=100, null=True, blank=True)
    DocumentStoreType = models.ForeignKey(
        DocumentStoreType,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    DocumentStore = models.ForeignKey(
        DocumentStore,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    Frequency = models.ForeignKey(
        Frequency,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    DocumentDateFirst = models.DateTimeField(null=True, blank=True, default=None)
    DocumentDateNext = models.DateTimeField(null=True, blank=True, default=None)
    DocumentDateLast = models.DateTimeField(null=True, blank=True, default=None)
    ExpectedDocuments = models.IntegerField(null=True, blank=True, default=None)
    SkipEvery = models.IntegerField(null=True, blank=True, default=None)
    StartSkip = models.IntegerField(null=True, blank=True, default=None)
    # Temp field type / In the future will be foreign key
    AlertEnabledFlag = models.IntegerField(null=True, blank=True, default=None)
    AlertDays = models.IntegerField(null=True, blank=True, default=None)
    AlertDocumentStatus = models.ForeignKey(
        AlertDocumentStatus,
        related_name='AlertDocumentStatus',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    AlertSource = models.ForeignKey(
        AlertSource,
        related_name='AlertSource',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    AlertType = models.ForeignKey(
        AlertType,
        related_name='AsdAlertType',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    AlertSubType = models.ForeignKey(
        AlertSubType,
        related_name='AlertSubType',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    AlertSeverity = models.ForeignKey(
        AlertSeverity,
        related_name='AlertSeverity',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    AlertStatus = models.ForeignKey(
        AlertStatus,
        related_name='AlertStatus',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    # Temp field type / In the future will be foreign key
    AlertTemplateId = models.IntegerField(null=True, blank=True, default=None)
    # Temp field type / In the future will be foreign key
    AlertEmailFlag = models.IntegerField(null=True, blank=True, default=None)
    AlertEmailOption = models.ForeignKey(
        AlertEmailOption,
        related_name='AlertEmailOption',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    # Temp field type / In the future will be foreign key
    AlertSenderId = models.IntegerField(null=True, blank=True, default=None)
    AlertRecipientId = models.TextField(null=True, blank=True, default=None)
    AlertBasePartyEmailId = models.TextField(null=True, blank=True, default=None)
    AlertConvertOption = models.ForeignKey(
        AlertConvertOption,
        related_name='AlertConvertOption',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    # Temp field type / In the future will be foreign key
    WarningEnabledFlag = models.IntegerField(null=True, blank=True, default=None)
    WarningDays = models.IntegerField(null=True, blank=True, default=None)
    WarningDocumentStatus = models.ForeignKey(
        'common.AlertDocumentStatus',
        related_name='WarningDocumentStatus',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    WarningSource = models.ForeignKey(
        'common.AlertSource',
        related_name='WarningSource',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    WarningType = models.ForeignKey(
        'common.AlertType',
        related_name='WarningType',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    WarningSubType = models.ForeignKey(
        'common.AlertSubType',
        related_name='WarningSubType',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    WarningSeverity = models.ForeignKey(
        'common.AlertSeverity',
        related_name='WarningSeverity',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    WarningStatus = models.ForeignKey(
        'common.AlertStatus',
        related_name='WarningStatus',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    # Temp field type / In the future will be foreign key
    WarningTemplateId = models.IntegerField(null=True, blank=True, default=None)
    # Temp field type / In the future will be foreign key
    WarningEmailFlag = models.IntegerField(null=True, blank=True, default=None)
    WarningEmailOption = models.ForeignKey(
        'common.AlertEmailOption',
        related_name='WarningEmailOption',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    # Temp field type / In the future will be foreign key
    WarningSenderId = models.IntegerField(null=True, blank=True, default=None)
    WarningRecipientId = models.TextField(null=True, blank=True, default=None)
    WarningBasePartyEmailId = models.TextField(null=True, blank=True, default=None)

    StorageLocation = models.IntegerField(null=True, blank=True)
    FirstUploadDate = models.DateTimeField(null=True, blank=True, default=None)
    LastVerifyDate = models.DateTimeField(null=True, blank=True, default=None)
    LastClearDate = models.DateTimeField(null=True, blank=True, default=None)
    FirstUploadBy = models.ForeignKey(
        get_user_model(),
        related_name='FirstUploadBy',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True,
    )
    LastVerifyBy = models.ForeignKey(
        get_user_model(),
        related_name='LastVerifyBy',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True,
    )
    LastClearanceBy = models.ForeignKey(
        get_user_model(),
        related_name='LastClearanceBy',
        on_delete=models.CASCADE,
        default=None, null=True, blank=True,
    )

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.DocumentId)

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Document'
        db_table = 'Document'
