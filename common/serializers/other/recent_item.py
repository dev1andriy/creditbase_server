from rest_framework import serializers
from common.models.base_party import *


class LastBasePartySerializer(serializers.ModelSerializer):
    Id = serializers.StringRelatedField(source='BasePartyId', many=False, read_only=True, )
    Label = serializers.StringRelatedField(source='BasePartyName', many=False, read_only=True, )

    class Meta:
        model = BaseParty
        fields = ('Id', 'Label')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ItemType'] = 1
        representation['Id'] = int(representation['Id'])
        return representation
