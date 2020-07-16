from rest_framework import serializers
from common.models.general import SubstitutionThreat


class SubstitutionThreatSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='SubstitutionThreatId')

    class Meta:
        model = SubstitutionThreat
        fields = ('label', 'value')
