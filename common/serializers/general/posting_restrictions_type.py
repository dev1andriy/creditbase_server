from rest_framework import serializers
from common.models.general import PostingRestrictionType


class PostingRestrictionsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostingRestrictionType
        fields = ('Description',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return " " + representation['Description']
