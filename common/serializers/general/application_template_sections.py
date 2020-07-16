from rest_framework import serializers
from common.models.general import ApplicationTemplateSection


class ApplicationTemplateSectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationTemplateSection
        fields = ('ApplicationTemplateSectionId', 'Description2', 'Description3', 'Description4')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return {
            'id': representation['ApplicationTemplateSectionId'],
            'name': representation['Description2'],
            'label': representation['Description3'],
            'type': representation['Description4'],
        }
