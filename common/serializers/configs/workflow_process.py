from rest_framework import serializers
from common.models.general import WorkflowProcess


class WorkflowProcessSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='WorkflowProcessId')

    class Meta:
        model = WorkflowProcess
        fields = ('label', 'value')
