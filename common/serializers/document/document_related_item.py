from rest_framework import serializers

from common.models import DocumentRelatedItem
from common.utils.return_value_or_none import return_value_or_none


class DocumentRelatedItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentRelatedItem
        fields = '__all__'
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'id': representation.get('DocumentRelatedItemId', None),
            'relatedItemType': return_value_or_none(representation.get('RelatedItemType', {}), 'RelatedItemTypeId'),
            'relatedItemTypeStringed': return_value_or_none(representation.get('RelatedItemType', {}), 'Description'),
            'relatedItemId': representation.get('RelatedItemId', None),
            'description': representation.get('Description', None)
        }

        return to_represent
