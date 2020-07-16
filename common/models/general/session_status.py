from django.db import models
from common.models.abstract import *


class SessionStatus(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                    StatusRecordableModel, MakeableModel, CheckableModel):
    SessionStatusId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.SessionStatusId)

    class Meta:
        verbose_name = 'SessionStatus'
        verbose_name_plural = 'SessionStatus'
        db_table = 'SessionStatus'
