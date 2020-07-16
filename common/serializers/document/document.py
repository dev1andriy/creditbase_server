from rest_framework import serializers

from common.models.document import Document, DocumentFile, DocumentRelatedItem
from common.serializers.document.document_file import DocumentFileSerializer
from common.serializers.document.document_related_item import DocumentRelatedItemsSerializer


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        document_file = DocumentFile.objects.filter(DocumentId=representation['DocumentId']).order_by('-DocumentFileId').first()

        to_represent = {
            'documentId': representation['DocumentId'],
            'document': {
                'documentDetails': {
                    'basePartyId': representation.get('BasePartyId', None),
                    'documentType': representation.get('DocumentType', None),
                    'description': representation.get('Description1', None),
                    'fileName': representation.get('FileName', None),
                    'fileType': representation.get('FileType', None),
                    'fileSize': representation.get('FileSize', None),
                    'fileView': 'http://' + self.context.get('host') + '/ViewFile/' + str(document_file.DocumentFileId) if document_file is not None and document_file.DocumentFileId is not None and self.context.get('host') is not None else None,
                    'documentIdType': representation.get('DocumentIdType', None),
                    'charDocumentId': representation.get('CharDocumentId', None),
                    'documentStatus': representation.get('DocumentStatus', None),
                    'receivedDate': representation.get('LastUpdatedDate', None),
                    # 'note': representation['Description1'],

                },
                'relatedItems': DocumentRelatedItemsSerializer(DocumentRelatedItem.objects.filter(DocumentId_id=representation.get('DocumentId'))).data,
            },
            'alertsAndWarnings': {
                'documentFrequency': {
                    'frequency': representation.get('Frequency', None),
                    'documentDateFirst': representation.get('DocumentDateFirst', None),
                    'documentDateLast': representation.get('DocumentDateLast', None),
                    'skipEvery': representation.get('SkipEvery', None),
                    'startSkip': representation.get('StartSkip', None),
                    'documentDateNext': representation.get('DocumentDateNext', None),

                },
                'alertAndWarningSettings': {
                    'alertDays': {
                        'alert': representation.get('AlertDays', None),
                        'warning': representation.get('WarningDays', None)
                    },
                    'alertDocumentStatus': {
                        'alert': representation.get('AlertDocumentStatus', None),
                        'warning': representation.get('WarningDocumentStatus', None)
                    },
                    'alertSource': {
                        'alert': representation.get('AlertSource', None),
                        'warning': representation.get('WarningSource', None)
                    },
                    'alertType': {
                        'alert': representation.get('AlertType', None),
                        'warning': representation.get('WarningType', None)
                    },
                    'alertSubType': {
                        'alert': representation.get('AlertSubType', None),
                        'warning': representation.get('WarningSubType', None)
                    },
                    'alertSeverity': {
                        'alert': representation.get('AlertSeverity', None),
                        'warning': representation.get('WarningSeverity', None)
                    },
                    'alertEmailFlag': {
                        'alert': representation.get('AlertEmailFlag', None),
                        'warning': representation.get('WarningEmailFlag', None)
                    },
                    'alertSender': {
                        'alert': representation.get('AlertSenderId', None),
                        'warning': representation.get('WarningSenderId', None)
                    },
                    'alertRecipients': {
                        'alert': representation.get('AlertRecipientId', None),
                        'warning': representation.get('WarningRecipientId', None)
                    },
                    'emailTemplate': {
                        'alert': representation.get('AlertTemplateId', None),
                        'warning': representation.get('WarningTemplateId', None)
                    },
                    'emailOption': {
                        'alert': representation.get('AlertEmailOption', None),
                        'warning': representation.get('WarningEmailOption', None)
                    },


                }
            },
            'clearance': {
                'alertsAndWarnings': [],
                'documentHistory': DocumentFileSerializer(DocumentFile.objects.filter(DocumentId=representation.get('DocumentId', None)), many=True).data
            }
        }

        return to_represent
