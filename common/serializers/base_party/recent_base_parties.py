from rest_framework import serializers
from common.models.base_party import BaseParty


class RecentBasePartiesSerializer(serializers.ModelSerializer):
    BasePartyType = serializers.StringRelatedField(source='BasePartyType.Description', many=False,)

    class Meta:
        model = BaseParty
        fields = ('BasePartyId', 'BasePartyName', 'BasePartyType')
