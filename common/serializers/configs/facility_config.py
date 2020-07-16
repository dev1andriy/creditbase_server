from rest_framework import serializers
from common.models.arrangement import Facility


class FacilityConfigSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='FacilityId')
    label = serializers.StringRelatedField(source='Description1')

    class Meta:
        model = Facility
        fields = ('value', 'label')
