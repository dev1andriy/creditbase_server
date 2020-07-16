from rest_framework import serializers
from common.models.general import RelationType


class RelationTypeSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='RelationTypeId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = RelationType
        fields = ('value', 'label')
