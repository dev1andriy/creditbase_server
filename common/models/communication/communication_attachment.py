from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.communication import Communication


class CommunicationAttachment(TimeStampedModel, InsertableModel, UpdateableModel):
    AttachmentId = models.AutoField(primary_key=True, null=False)
    CommunicationId = models.ForeignKey(
        Communication,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    Name = models.CharField(max_length=50, null=True, blank=True, default=None)
    Description = models.CharField(max_length=200, null=True, blank=True, default=None)
    FileType = models.ForeignKey(
        FileType,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    FileName = models.CharField(max_length=200, null=True, blank=True, default=None)
    FileURL = models.CharField(max_length=200, null=True, blank=True, default=None)
    FileSize = models.FloatField(null=True, blank=True, default=None)
    FileObject = models.TextField(null=True, blank=True, default=None)

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.AttachmentId)

    class Meta:
        verbose_name = 'CommunicationAttachment'
        verbose_name_plural = 'CommunicationAttachment'
        db_table = 'CommunicationAttachment'

