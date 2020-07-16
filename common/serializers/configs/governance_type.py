from rest_framework import serializers
from common.models.general import GovernanceType


class GovernanceTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='GovernanceTypeId')

    class Meta:
        model = GovernanceType
        fields = ('label', 'value')
