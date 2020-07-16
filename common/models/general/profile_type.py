from django.db import models

from common.models.abstract import *


class ProfileType(TimeStampedModel, InsertableModel, DescribeableModel, HostableModel, CheckableModel, MakeableModel,
                  StatusRecordableModel):
    ProfileTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.ProfileTypeId, self.Description)

    class Meta:
        verbose_name = 'ProfileType'
        verbose_name_plural = 'ProfileType'
        db_table = 'ProfileType'
