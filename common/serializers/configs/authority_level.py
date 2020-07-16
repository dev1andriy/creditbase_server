from rest_framework import serializers
from common.models.general import AuthorityLevel


class AuthorityLevelSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='AuthorityLevelId')

    class Meta:
        model = AuthorityLevel
        fields = ('label', 'value')
