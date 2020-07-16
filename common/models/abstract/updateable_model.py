from django.conf import settings
from django.db import models


class UpdateableModel(models.Model):
    LastUpdatedBy = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      blank=True,
                                      on_delete=models.CASCADE,
                                      null=True,
                                      related_name="%(class)s_updated_by",
                                      db_column='LastUpdatedBy')

    class Meta:
        abstract = True
