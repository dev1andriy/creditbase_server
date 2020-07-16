from rest_framework import serializers
from common.models.general import RelationCategory


class RelationCategorySerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='RelationCategoryId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = RelationCategory
        fields = ('value', 'label')
