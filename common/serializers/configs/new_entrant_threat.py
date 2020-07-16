from rest_framework import serializers
from common.models.general import NewEntrantThreat


class NewEntrantThreatSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='NewEntrantThreatId')

    class Meta:
        model = NewEntrantThreat
        fields = ('label', 'value')
