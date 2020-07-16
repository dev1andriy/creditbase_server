from django.db import models

from common.models.base_party import BaseParty


class BasePartyApplicationSummary(models.Model):
    BasePartyId = models.OneToOneField(
        BaseParty,
        related_name='ApplicationSummary',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    CurrentCreditApplicationId = models.IntegerField(default=None, blank=True, null=True)
    CreditApplicationsTotal = models.IntegerField(default=None, blank=True, null=True)
    CreditApplicationsApproved = models.IntegerField(default=None, blank=True, null=True)
    CreditApplicationsDeclined = models.IntegerField(default=None, blank=True, null=True)
    CreditApplicationsCancelled = models.IntegerField(default=None, blank=True, null=True)
    CreditApplicationsInProcess = models.IntegerField(default=None, blank=True, null=True)
    CumulativeExposureApproved = models.IntegerField(default=None, blank=True, null=True)
    CumulativeExposureDeclined = models.IntegerField(default=None, blank=True, null=True)
    CumulativeExposureInProcess = models.IntegerField(default=None, blank=True, null=True)
    CurrentRatingApplicationId = models.IntegerField(default=None, blank=True, null=True)
    RatingApplicationsTotal = models.IntegerField(default=None, blank=True, null=True)
    RatingApplicationsApproved = models.IntegerField(default=None, blank=True, null=True)
    RatingApplicationsDeclined = models.IntegerField(default=None, blank=True, null=True)
    RatingApplicationsCancelled = models.IntegerField(default=None, blank=True, null=True)
    RatingApplicationsInProcess = models.IntegerField(default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.CurrentCreditApplicationId, self.CreditApplicationsTotal)

    class Meta:
        verbose_name = 'BasePartyApplicationSummary'
        verbose_name_plural = 'BasePartyApplicationSummary'
        db_table = 'BasePartyApplicationSummary'
