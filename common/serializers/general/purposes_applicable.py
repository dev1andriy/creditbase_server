from rest_framework import serializers
from common.models.general import Purpose


class PurposesApplicableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ('Description',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return " " + representation['Description']
