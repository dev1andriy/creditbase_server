from common.models.abstract import *
from django.db import models


class ChecklistTab(UpdateableModel, InsertableModel, TimeStampedModel):
    ChecklistTabId = models.AutoField(primary_key=True, null=False)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Title = models.CharField(max_length=100, null=True, blank=True)

    TabId = models.IntegerField(null=True, blank=True)
    TabLevel = models.IntegerField(default=1, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.ChecklistTabId)

    class Meta:
        verbose_name = 'ChecklistTab'
        verbose_name_plural = 'ChecklistTab'
        db_table = 'ChecklistTab'
