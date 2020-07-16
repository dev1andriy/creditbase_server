from rest_framework import serializers
from common.models.general import CompetitiveRivalry


class CompetitiveRivalrySerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='CompetitiveRivalryId')

    class Meta:
        model = CompetitiveRivalry
        fields = ('label', 'value')
