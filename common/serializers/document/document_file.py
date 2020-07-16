from rest_framework import serializers
from common.utils.return_value_or_none import return_value_or_none

from common.models.document import DocumentFile


class DocumentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentFile
        exclude = ("FileObject",)
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'documentFileId': representation.get('DocumentFileId', None),
            'documentType': return_value_or_none(representation.get('DocumentType', {}), 'Description'),
            'fileName': representation.get('FileName', None),
            'fileType': representation.get('FileType', None),
            'status': return_value_or_none(representation.get('DocumentStatus', {}), 'Description'),
            # 'uploadBy'
            # 'verifiedBy'
            'uploadDate': representation.get('UploadDate', None),
            'verifiedDate': representation.get('VerifiedDate', None),
            'documentDateNext': representation.get('DocumentDateNext', None)
        }

        return to_represent
