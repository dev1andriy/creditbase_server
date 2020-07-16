from django.db import models
from common.models.abstract import *


class Sequence(TimeStampedModel, InsertableModel, UpdateableModel):
    SequenceId = models.IntegerField(primary_key=True)
    Description = models.IntegerField()
    TabelId = models.IntegerField()
    TableName = models.CharField(max_length=50, default=None, blank=True, null=True)
    TableFilter = models.CharField(max_length=50, default=None, blank=True, null=True)
    CurrentValue = models.IntegerField()
    IncrementValue = models.IntegerField()
    MinimumValue = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.SequenceId, self.TableName)

    class Meta:
        verbose_name = 'Sequence'
        verbose_name_plural = 'Sequence'
        db_table = 'Sequence'
