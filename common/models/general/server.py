from common.models.general import Application
from django.db import models
from common.models.abstract import *


class Server(TimeStampedModel, InsertableModel, UpdateableModel,
             StatusRecordableModel, MakeableModel, CheckableModel):
    ServerId = models.IntegerField(primary_key=True)
    DNSName = models.CharField(max_length=100, default=None, blank=True, null=True)
    IPAddress = models.CharField(max_length=30, default=None, blank=True, null=True)
    MACAddress = models.CharField(max_length=100, default=None, blank=True, null=True)
    Description = models.CharField(max_length=100, default=None, blank=True, null=True)
    ApplicationId1 = models.ForeignKey(
        Application,
        related_name='ApplicationId1',
        on_delete=models.CASCADE,
        db_column='ApplicationId1',
        default=None, blank=True, null=True
    )
    ApplicationId2 = models.ForeignKey(
        Application,
        related_name='ApplicationId2',
        on_delete=models.CASCADE,
        db_column='ApplicationId2',
        default=None, blank=True, null=True
    )
    ApplicationId3 = models.ForeignKey(
        Application,
        related_name='ApplicationId3',
        on_delete=models.CASCADE,
        db_column='ApplicationId3',
        default=None, blank=True, null=True
    )
    ApplicationId4 = models.ForeignKey(
        Application,
        related_name='ApplicationId4',
        on_delete=models.CASCADE,
        db_column='ApplicationId4',
        default=None, blank=True, null=True
    )
    ApplicationId5 = models.ForeignKey(
        Application,
        related_name='ApplicationId5',
        on_delete=models.CASCADE,
        db_column='ApplicationId5',
        default=None, blank=True, null=True
    )

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.ServerId)

    class Meta:
        verbose_name = 'Server'
        verbose_name_plural = 'Server'
        db_table = 'Server'
