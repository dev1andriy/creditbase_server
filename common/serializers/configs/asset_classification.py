from rest_framework import serializers
from common.models.general import AssetClassification


class AssetClassificationSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='AssetClassificationId')

    class Meta:
        model = AssetClassification
        fields = ('label', 'value')
