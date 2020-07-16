from rest_framework import serializers
from common.models.general import Purpose


class PurposeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='PurposeId')

    class Meta:
        model = Purpose
        fields = ('label', 'value')




