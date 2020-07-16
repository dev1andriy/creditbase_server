from django.db import models

from common.models.abstract import *


class RecentItem(TimeStampedModel, InsertableModel, UpdateableModel):
    RecentItemId = models.AutoField(primary_key=True, null=False)
    ItemType = models.IntegerField(null=False)
    ItemKey = models.IntegerField(null=False)

    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.RecentItemId)

    class Meta:
        verbose_name = 'RecentItem'
        verbose_name_plural = 'RecentItem'
        db_table = 'RecentItem'

