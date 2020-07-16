from django.db import models
from common.models.abstract import *


class Application(TimeStampedModel, InsertableModel, UpdateableModel,
                  StatusRecordableModel, MakeableModel, CheckableModel):
    ApplicationId = models.IntegerField(primary_key=True)
    Description1 = models.CharField(max_length=20, default=None, blank=True, null=True)
    Description2 = models.CharField(max_length=20, default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.ApplicationId)

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Application'
        db_table = 'Application'
