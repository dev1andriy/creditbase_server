from rest_framework import serializers
from common.models.general import PostingRestrictionType


class PostingRestrictionTypeSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='PostingRestrictionTypeId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = PostingRestrictionType
        fields = ('value', 'label')
