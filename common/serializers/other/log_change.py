from rest_framework import serializers
from common.models.general import LogChange


class LogChangeSerializer(serializers.ModelSerializer):
    InsertedBy = serializers.StringRelatedField(source='InsertedBy.get_full_name', many=False, read_only=True, )

    class Meta:
        model = LogChange
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_response = {
            "date": representation['InsertDate'],
            "user": representation['InsertedBy'],
            "message": representation['ChangeText']
        }

        return to_response
