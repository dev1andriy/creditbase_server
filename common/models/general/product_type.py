from django.db import models
from common.models.abstract import *


class ProductType(TimeStampedModel, HostableModel, InsertableModel, UpdateableModel, DescribeableModel,
                  StatusRecordableModel, MakeableModel, CheckableModel):
    ProductTypeId = models.IntegerField(primary_key=True)

    objects = models.Manager()

    def __str__(self):
        return "{} - {}".format(self.ProductTypeId, self.Description)

    class Meta:
        verbose_name = 'ProductType'
        verbose_name_plural = 'ProductType'
        db_table = 'ProductType'
