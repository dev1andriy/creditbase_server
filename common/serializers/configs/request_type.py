from rest_framework import serializers
from common.models.general import RequestType


class RequestTypeSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='RequestTypeId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = RequestType
        fields = ('value', 'label')
