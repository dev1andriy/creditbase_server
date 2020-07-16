from rest_framework import serializers
from common.models.general import Country


class CountrySerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='CountryId')

    class Meta:
        model = Country
        fields = ('label', 'value')
