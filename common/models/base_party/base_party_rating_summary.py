from django.db import models

from common.models.base_party import BaseParty


class BasePartyRatingSummary(models.Model):
    BasePartyId = models.OneToOneField(
        BaseParty,
        related_name='RatingSummary',
        on_delete=models.CASCADE,
        primary_key=True
    )
    RatingInternal1 = models.IntegerField(default=None, blank=True, null=True)
    RatingInternalModel1 = models.IntegerField(default=None, blank=True, null=True)
    RatingInternalDate1 = models.DateTimeField(default=None, blank=True, null=True)
    RatingInternal2 = models.IntegerField(default=None, blank=True, null=True)
    RatingInternalModel2 = models.IntegerField(default=None, blank=True, null=True)
    RatingInternalDate2 = models.DateTimeField(default=None, blank=True, null=True)
    RatingExternal1 = models.IntegerField(default=None, blank=True, null=True)
    RatingExternalModel1 = models.IntegerField(default=None, blank=True, null=True)
    RatingExternalDate1 = models.DateTimeField(default=None, blank=True, null=True)
    RatingExternal2 = models.IntegerField(default=None, blank=True, null=True)
    RatingExternalModel2 = models.IntegerField(default=None, blank=True, null=True)
    RatingExternalDate2 = models.DateTimeField(default=None, blank=True, null=True)
    RatingExternal3 = models.IntegerField(default=None, blank=True, null=True)
    RatingExternalModel3 = models.IntegerField(default=None, blank=True, null=True)
    RatingExternalDate3 = models.DateTimeField(default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {} - {}".format(self.RatingInternal1, self.RatingInternalModel1, self.RatingInternalDate1)

    class Meta:
        verbose_name = 'BasePartyRatingSummary'
        verbose_name_plural = 'BasePartyRatingSummary'
        db_table = 'BasePartyRatingSummary'
