from django.db import models
from common.models.abstract import *


class AuthorityLevel(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                     StatusRecordableModel, MakeableModel, CheckableModel):
    AuthorityLevelId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.AuthorityLevelId, self.Description)

    class Meta:
        verbose_name = 'AuthorityLevel'
        verbose_name_plural = 'AuthorityLevel'
        db_table = 'AuthorityLevel'
