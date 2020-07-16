from rest_framework import serializers
from common.utils.return_value_or_none import return_value_or_none

from common.models.document import Document, DocumentFile


class DocumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = '__all__'
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        document_file = DocumentFile.objects.filter(DocumentId=representation['DocumentId']).order_by('-DocumentFileId').first()

        to_represent = {
            'documentId': representation.get('DocumentId', None),
            'documentName': representation.get('FileName', None),
            'documentType': return_value_or_none(representation.get('DocumentType', {}), 'Description'),
            'documentStatus': return_value_or_none(representation.get('DocumentStatus', {}), 'Description'),
            'applicationNumber': return_value_or_none(representation.get('CreditApplicationId', {}), 'CreditApplicationId'),
            'fileType': representation.get('FileType', None),
            'fileURL': 'http://' + self.context.get('host') + '/ViewFile/' + str(document_file.DocumentFileId) if document_file is not None and document_file.DocumentFileId is not None and self.context.get('host') is not None else None,
            'uploadedBy': '{} {}'.format(return_value_or_none(representation.get('LastUpdatedBy', {}), 'first_name'), return_value_or_none(representation.get('LastUpdatedBy', {}), 'last_name')),
            'dateUploaded': representation.get('LastUpdatedDate', None)
        }

        return to_represent
