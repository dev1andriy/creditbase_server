from rest_framework import serializers
from common.models.general import Frequency


class FrequencySerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='FrequencyId')

    class Meta:
        model = Frequency
        fields = ('label', 'value')
