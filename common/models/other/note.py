from django.db import models

from common.models.abstract import *
from common.models.base_party import BaseParty


class Note(TimeStampedModel, InsertableModel, UpdateableModel):
    NoteId = models.AutoField(primary_key=True, null=False)
    BasePartyId = models.ForeignKey(
        BaseParty,
        on_delete=models.CASCADE,
        default=None, blank=True, null=True
    )
    NoteLevel = models.IntegerField(null=True, blank=True, default=None)
    Note = models.TextField(null=True, blank=True, default=None)
    ModuleId = models.IntegerField(null=True, blank=True, default=None)
    NoteKey1 = models.IntegerField(null=True, blank=True, default=None)
    NoteKey2 = models.IntegerField(null=True, blank=True, default=None)
    NoteKey3 = models.IntegerField(null=True, blank=True, default=None)
    Tab = models.CharField(max_length=100, null=True, blank=True, default=None)

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.Note)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Note'
        db_table = 'Note'
