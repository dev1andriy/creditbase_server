from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.document import Document


class DocumentFile(TimeStampedModel, InsertableModel, UpdateableModel):
    DocumentFileId = models.AutoField(primary_key=True, null=False)
    DocumentId = models.ForeignKey(
        Document,
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
    FileObject = models.TextField(null=True, blank=True, default=None)
    UploadDate = models.DateTimeField(null=True, blank=True, default=None)
    VerifiedDate = models.DateTimeField(null=True, blank=True, default=None)
    DocumentDateNext = models.DateTimeField(null=True, blank=True, default=None)

    objects = models.Manager()

    def __str__(self):
        return '{} - {}'.format(self.DocumentFileId, self.DocumentId)

    class Meta:
        verbose_name = 'DocumentFile'
        verbose_name_plural = 'DocumentFile'
        db_table = 'DocumentFile'
