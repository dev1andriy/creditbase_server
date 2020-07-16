from rest_framework import serializers
from common.models.credit_application.checklist.checklist_response import ChecklistResponse


class ChecklistResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistResponse
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'id': representation['ResponseId'],
            'label': representation['Description']
        }

        return to_represent
