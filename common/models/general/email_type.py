from django.db import models
from common.models.abstract import *


class EmailType(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
                HostableModel, StatusRecordableModel, MakeableModel, CheckableModel):
    EmailTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.EmailTypeId, self.Description)

    class Meta:
        verbose_name = 'EmailType'
        verbose_name_plural = 'EmailType'
        db_table = 'EmailType'
