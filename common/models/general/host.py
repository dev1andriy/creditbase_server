from common.models.general.host_type import HostType
from common.models.general import HostLoginMode
from django.db import models
from common.models.abstract import *


class Host(TimeStampedModel, InsertableModel, UpdateableModel, DescribeableModel,
           StatusRecordableModel, MakeableModel, CheckableModel):
    HostId = models.IntegerField(primary_key=True)
    HostType = models.ForeignKey(
        HostType,
        related_name='HostType',
        on_delete=models.CASCADE,
        db_column='HostType',
        default=None, blank=True, null=True
    )
    PullDataClasses = models.TextField()
    PushDataClasses = models.TextField()
    HostLoginMode = models.ForeignKey(
        HostLoginMode,
        related_name='HostLoginMode',
        on_delete=models.CASCADE,
        db_column='HostLoginMode',
        default=None, blank=True, null=True
    )
    HostUser = models.CharField(max_length=50, default=None, blank=True, null=True)
    HostPassword = models.CharField(max_length=300, default=None, blank=True, null=True)
    PasswordChangeFlag = models.IntegerField()
    PasswordExpiryFlag = models.IntegerField()
    PasswordExpiryWarnDays = models.IntegerField()
    LockoutFlag = models.IntegerField()
    LockoutMaxAttempts = models.IntegerField()
    LockoutSeconds = models.IntegerField()
    PssswordStrength = models.IntegerField()
    PssswordMinLength = models.IntegerField()
    AutoDisableFlag = models.IntegerField()
    AutoDisableDays = models.IntegerField()
    PasswordLookbackFlag = models.IntegerField()
    PasswordLookbackCount = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.HostId, self.HostType)

    class Meta:
        verbose_name = 'Host'
        verbose_name_plural = 'Host'
        db_table = 'Host'

