from django.db import models


class RankableModel(models.Model):
    OrderingRank = models.IntegerField(default=None, blank=True, null=True)

    class Meta:
        abstract = True
