from rest_framework import serializers
from common.models.arrangement import Collateral


class CollateralConfigSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='CollateralId')
    label = serializers.StringRelatedField(source='Description1')

    class Meta:
        model = Collateral
        fields = ('value', 'label')
