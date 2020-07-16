from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.sessions.base_session import AbstractBaseSession
from common.models.general.session_status import SessionStatus
from django.db import models

from common.models.abstract import InsertableModel, UpdateableModel, TimeStampedModel, Server, Application


class CustomSession(AbstractBaseSession, TimeStampedModel, InsertableModel, UpdateableModel):
    # SessionId = models.IntegerField(primary_key=True)
    SessionIdWeb = models.CharField(max_length=200, default=None, blank=True, null=True)
    ServerId = models.ForeignKey(
        Server,
        related_name='Server',
        on_delete=models.CASCADE,
        db_column='Server',
        default=None, blank=True, null=True
    )
    ApplicationId = models.ForeignKey(
        Application,
        related_name='Application',
        on_delete=models.CASCADE,
        db_column='ApplicationId',
        default=None, blank=True, null=True
    )
    StaffId = models.IntegerField(default=None, blank=True, null=True)
    IPAddress = models.CharField(max_length=50, default=None, blank=True, null=True)
    MACAddress = models.CharField(max_length=100, default=None, blank=True, null=True)
    SessionStatus = models.ForeignKey(
        SessionStatus,
        related_name='SessionStatus',
        on_delete=models.CASCADE,
        db_column='SessionStatus',
        default=None, blank=True, null=True
    )
    StartDate = models.DateTimeField(default=None, blank=True, null=True)
    EndDate = models.DateTimeField(default=None, blank=True, null=True)
    LastRequestDate = models.DateTimeField(default=None, blank=True, null=True)

    @classmethod
    def get_session_store_class(cls):
        return SessionStore


class SessionStore(DBStore):
    @classmethod
    def get_model_class(cls):
        return CustomSession

    def create_model_instance(self, data):
        obj = super(SessionStore, self).create_model_instance(data)
        try:
            account_id = int(data.get('_auth_user_id'))
        except (ValueError, TypeError):
            account_id = None
        obj.account_id = account_id
        return obj
