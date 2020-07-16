from rest_framework import serializers
from common.models.general import Flag


class FlagSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='FlagId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = Flag
        fields = ('value', 'label')
