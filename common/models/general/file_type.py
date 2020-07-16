from django.db import models
from common.models.abstract import *


class FileType(DescribeableModel, HostableModel, TimeStampedModel, InsertableModel, UpdateableModel,
               StatusRecordableModel, MakeableModel, CheckableModel):
    FileTypeId = models.AutoField(primary_key=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.FileTypeId, self.Description)

    class Meta:
        verbose_name = 'FileType'
        verbose_name_plural = 'FileType'
        db_table = 'FileType'
