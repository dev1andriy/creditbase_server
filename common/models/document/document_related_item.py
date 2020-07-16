from django.db import models

from common.models.abstract import *
from common.models.general import *
from common.models.document import Document


class DocumentRelatedItem(TimeStampedModel, InsertableModel, UpdateableModel):
    DocumentRelatedItemId = models.AutoField(primary_key=True, null=False)
    DocumentId = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    RelatedItemType = models.ForeignKey(
        RelatedItemType,
        on_delete=models.CASCADE,
        default=None, null=True, blank=True
    )
    RelatedItemId = models.CharField(max_length=50, null=True, blank=True, default=None)
    Description = models.CharField(max_length=200, null=True, blank=True, default=None)

    objects = models.Manager()

    def __str__(self):
        return '{} - {}'.format(self.DocumentRelatedItemId, self.DocumentId)

    class Meta:
        verbose_name = 'DocumentRelatedItem'
        verbose_name_plural = 'DocumentRelatedItem'
        db_table = 'DocumentRelatedItem'
