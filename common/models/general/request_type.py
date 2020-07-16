from django.db import models
from common.models.abstract import *


class RequestType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
                  StatusRecordableModel, MakeableModel, CheckableModel):
    RequestTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.RequestTypeId)

    class Meta:
        verbose_name = 'RequestType'
        verbose_name_plural = 'RequestType'
        db_table = 'RequestType'

