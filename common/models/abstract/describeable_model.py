from django.db import models


class DescribeableModel(models.Model):
    Description = models.CharField(max_length=50, default=None, blank=True, null=True)
    Description1 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Description2 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Description3 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Description4 = models.CharField(max_length=50, default=None, blank=True, null=True)
    Description5 = models.CharField(max_length=50, default=None, blank=True, null=True)

    class Meta:
        abstract = True
