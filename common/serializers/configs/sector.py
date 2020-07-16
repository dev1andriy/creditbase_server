from rest_framework import serializers
from common.models.general import Sector


class SectorSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='SectorId')

    class Meta:
        model = Sector
        fields = ('label', 'value')
