from rest_framework import serializers
from common.models.credit_application.checklist.checklist_tab import ChecklistTab


class ChecklistTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistTab
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            "name": representation['Name'],
            "title": representation['Title'],
            "id": representation['ChecklistTabId']
        }

        return to_represent
