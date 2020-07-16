from rest_framework import serializers
from common.models.general import RelatedItemType


class RelatedItemTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='RelatedItemTypeId')

    class Meta:
        model = RelatedItemType
        fields = ('label', 'value')
