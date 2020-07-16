from django.conf import settings
from django.db import models


class ViewableModel(models.Model):
    LastViewedDate = models.DateTimeField(null=True, blank=True)
    LastViewedBy = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     blank=True,
                                     on_delete=models.CASCADE,
                                     null=True,
                                     related_name="%(class)s_viewed_by",
                                     db_column='ViewedBy')

    class Meta:
        abstract = True
