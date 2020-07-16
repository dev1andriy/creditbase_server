from rest_framework import serializers
from common.models.credit_application.checklist.checklist_result import ChecklistResult


class ChecklistResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistResult
        fields = '__all__'
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'id': representation['ChecklistResultId'],
            'role': representation['Role'],
            'status': {
                'value': representation['Status']['Description'] if representation['Status'] is not None else None,
                'color': representation['Status']['Description1'] if representation['Status'] is not None else None,
            },
            'finalized': representation['FinalizedFlag'],
            'user': '{} {}'.format(representation['LastUpdatedBy']['first_name'] if representation['LastUpdatedBy'] is not None else '',
                                   representation['LastUpdatedBy']['last_name'] if representation['LastUpdatedBy'] is not None else ''),
            'date': representation['LastUpdatedDate'],
            'comment': representation['Comment']
            # 'id': representation['ResponseId'],
            # 'label': representation['Description']
        }

        return to_represent
