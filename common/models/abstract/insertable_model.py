from django.conf import settings
from django.db import models


class InsertableModel(models.Model):
    InsertedBy = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   blank=True,
                                   on_delete=models.CASCADE,
                                   null=True,
                                   related_name="%(class)s_inserted_by",
                                   db_column='InsertedBy')

    class Meta:
        abstract = True
