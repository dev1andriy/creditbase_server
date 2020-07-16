from rest_framework import serializers
from common.models.general import IdentifierCategory


class IdentifierCategorySerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='IdentifierCategoryId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = IdentifierCategory
        fields = ('value', 'label')
