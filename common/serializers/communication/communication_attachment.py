from rest_framework import serializers
from common.models.communication import CommunicationAttachment


class CommunicationAttachmentSerializer(serializers.ModelSerializer):
    FileType = serializers.StringRelatedField(source='FileType.Description', many=False, read_only=True, )

    class Meta:
        model = CommunicationAttachment
        fields = "__all__"
        exclude = ("FileObject",)
