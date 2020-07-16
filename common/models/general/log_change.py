from django.db import models
from common.models.abstract import *
from common.models.general import *


class LogChange(TimeStampedModel, InsertableModel, UpdateableModel):
    LogChangeId = models.AutoField(primary_key=True, null=False)
    # ModuleId = models.ForeignKey(
    #     Module,
    #     on_delete=models.CASCADE,
    #     related_name='Module',
    #     null=True
    # )
    # TableId = models.ForeignKey(
    #     Table,
    #     on_delete=models.CASCADE,
    #     related_name='Table',
    #     null=True
    # )
    ItemType = models.IntegerField()
    ItemKey = models.IntegerField()
    ChangeTypeId = models.ForeignKey(
        ChangeType,
        on_delete=models.CASCADE,
        db_column='BasePartyId',
        related_name='Addresses',
        null=True
    )
    ChangeText = models.TextField(null=True, blank=True, default=None)

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.LogChangeId)

    class Meta:
        verbose_name = 'LogChange'
        verbose_name_plural = 'LogChange'
        db_table = 'LogChange'
