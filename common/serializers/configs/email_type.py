from rest_framework import serializers
from common.models.general import EmailType


class EmailTypeSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='EmailTypeId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = EmailType
        fields = ('value', 'label')
