from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.arrangement.facility import Facility
from common.models.arrangement.collateral import Collateral
from common.models.credit_application import CreditApplication


class Coverage(TimeStampedModel, InsertableModel, UpdateableModel):
    CoverageId = models.AutoField(primary_key=True, null=False, blank=False)
    HostId = models.ForeignKey(
        Host,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    CoverageIdHost = models.CharField(max_length=50, null=True, blank=True)
    FacilityIdHost = models.CharField(max_length=50, null=True, blank=True)
    CollateralIdHost = models.CharField(max_length=50, null=True, blank=True)
    FacilityId = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    CollateralId = models.ForeignKey(
        Collateral,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    CreditApplicationId = models.ForeignKey(
        CreditApplication,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    Assignment = models.FloatField(null=True, blank=True)
    LienOrder = models.IntegerField(null=True, blank=True)
    BindWith = models.CharField(max_length=10, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {} / {}".format(self.CoverageId, self.FacilityId, self.CollateralId)

    class Meta:
        verbose_name = 'Coverage'
        verbose_name_plural = 'Coverage'
        db_table = 'Coverage'
