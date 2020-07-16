from django.db import models


class PrintableModel(models.Model):
    PrintFlag = models.BooleanField(default=False)

    class Meta:
        abstract = True
