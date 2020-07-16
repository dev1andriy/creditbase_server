from rest_framework import serializers
from common.models.credit_application.checklist import ChecklistTemplate


class ChecklistTemplatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistTemplate
        fields = ('Description',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return representation['Description']
