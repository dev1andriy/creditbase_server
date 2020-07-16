from common.models import BaseParty
from common.models.general import *
from common.serializers.configs import *


def generate_config(base_party_id=None):
    return {
            "document": {
                "documentsDetails": [
                    {
                        "type": "select",
                        "label": "Base Party",
                        "name": "baseParty",
                        "options": [{
                            **BasePartyConfigSerializer(BaseParty.objects.get(BasePartyId=base_party_id)).data,
                            "autoSelect": True
                        }],
                        "order": 1,
                        "isRequired": True,
                    } if base_party_id is not None
                    else {
                        "type": "select",
                        "label": "Base Party",
                        "name": "baseParty",
                        "options": BasePartyConfigSerializer(BaseParty.objects.all(), many=True).data,
                        "order": 1,
                        "isRequired": True
                    },
                    {
                        "type": "select",
                        "label": "Document Type",
                        "name": "documentType",
                        "options": DocumentTypeSerializer(DocumentType.objects.all(), many=True).data,
                        "placeholder": 'Select an entity',
                        "order": 2
                    },
                    {
                        "type": "input",
                        "inputType": "text",
                        "label": "Description",
                        "name": "description",
                        "order": 3
                    },
                    {
                        "type": "input",
                        "inputType": "file",
                        "infoField": "fileInfo",
                        "name": "file",
                        "label": "File",
                        "order": 4,
                    },
                    {
                        "type": "input",
                        "inputType": "hidden",
                        "name": "fileInfo"
                    },
                    {
                        "type": "input",
                        "inputType": "hidden",
                        "name": "fileView"
                    },
                    {
                        "type": "readOnly",
                        "label": "File name",
                        "name": "fileName",
                        "order": 5
                    },
                    {
                        "type": "readOnly",
                        "label": "File type",
                        "name": "fileType",
                        "order": 6
                    },
                    {
                        "type": "readOnly",
                        "label": "File size",
                        "name": "fileSize",
                        "order": 7
                    },
                    {
                        "type": "select",
                        "label": "Doc. ID Type",
                        "name": "documentIdType",
                        "options": DocumentIdTypeSerializer(DocumentIdType.objects.all(), many=True).data,
                        "placeholder": 'Select a type',
                        "order": 8
                    },
                    {
                        "type": "input",
                        "inputType": "text",
                        "label": "Doc. ID",
                        "name": "charDocumentId",
                        "order": 9
                    },
                    {
                        "type": "readOnly",
                        "label": "Status",
                        "name": "documentStatus",
                        "order": 10
                    },
                    {
                        "type": "readOnly",
                        "label": "Received Date",
                        "name": "receivedDate",
                        "order": 11
                    },
                    # {
                    #     "type": "input",
                    #     "inputType": "text",
                    #     "label": "Note",
                    #     "name": "note"
                    # },
                ],
                "relatedItems": [
                    {
                        "type": "select",
                        "label": "Item Type",
                        "name": "relatedItemType",
                        "options": RelatedItemTypeSerializer(RelatedItemType.objects.all(), many=True).data,
                        "placeholder": 'Select a type',
                        "order": 1
                    },
                    {
                        "type": "input",
                        "inputType": "text",
                        "label": "Item ID",
                        "name": "relatedItemId",
                        "order": 2
                    },
                    {
                        "type": "input",
                        "inputType": "text",
                        "label": "Item Description",
                        "name": "description",
                        "order": 3
                    }
                ]
            },
            "alertsAndWarnings": {
                "documentFrequency": [
                    {
                        "type": "readOnly",
                        "label": "Frequency",
                        "name": "frequency",
                        "order": 1
                    },
                    {
                        "type": "readOnly",
                        "label": "First Document Date",
                        "name": "documentDateFirst",
                        "order": 2
                    },
                    {
                        "type": "readOnly",
                        "label": "Last Document Date",
                        "name": "documentDateLast",
                        "order": 3
                    },
                    # {
                    #     "type": "readOnly",
                    #     "label": "Total Documents",
                    #     "name": "totalDocuments"
                    # },
                    {
                        "type": "readOnly",
                        "label": "Skip every",
                        "name": "skipEvery",
                        "order": 4
                    },
                    {
                        "type": "readOnly",
                        "label": "Starting",
                        "name": "startSkip",
                        "order": 5
                    },
                    {
                        "type": "readOnly",
                        "label": "Next Document Date",
                        "name": "documentDateNext",
                        "order": 6
                    },
                ],
                "alertAndWarningSettings": [
                    {
                        "type": "input",
                        "label": "Alert days before/after",
                        "inputType": "double",
                        "name": "alertDays",
                        "names": [
                            "alert", "warning"
                        ],
                        "types": [
                            "input", "input"
                        ],
                        "inputTypes": [
                            "number", "number"
                        ],
                        "order": 1
                    },
                    {
                        "type": "input",
                        "label": "Document Status",
                        "inputType": "double",
                        "name": "alertDocumentStatus",
                        "names": [
                            "alert", "warning"
                        ],
                        "types": [
                            "select", "select"
                        ],
                        "options": [
                            AlertDocumentStatusSerializer(AlertDocumentStatus.objects.all(), many=True).data,
                            AlertDocumentStatusSerializer(AlertDocumentStatus.objects.all(), many=True).data,
                        ],
                        "order": 2
                    },
                    {
                        "type": "input",
                        "label": "Alert/Warning Source",
                        "inputType": "double",
                        "name": "alertSource",
                        "names": [
                            "alert", "warning"
                        ],
                        "types": [
                            "select", "select"
                        ],
                        "options": [
                            AlertSourceSerializer(AlertSource.objects.all(), many=True).data,
                            AlertSourceSerializer(AlertSource.objects.all(), many=True).data
                        ],
                        "order": 3
                    },
                    {
                        "type": "input",
                        "label": "Alert/Warning Type",
                        "inputType": "double",
                        "name": "alertType",
                        "names": [
                            "alert", "warning"
                        ],
                        "types": [
                            "select", "select"
                        ],
                        "options": [
                            AlertTypeSerializer(AlertType.objects.all(), many=True).data,
                            AlertTypeSerializer(AlertType.objects.all(), many=True).data
                        ],
                        "order": 4
                    },
                    {
                        "type": "input",
                        "label": "Alert/Warning Subtype",
                        "inputType": "double",
                        "name": "alertSubType",
                        "names": [
                            "alert", "warning"
                        ],
                        "types": [
                            "select", "select"
                        ],
                        "options": [
                            AlertSubTypeSerializer(AlertSubType.objects.all(), many=True).data,
                            AlertSubTypeSerializer(AlertSubType.objects.all(), many=True).data
                        ],
                        "order": 5
                    },
                    {
                        "type": "input",
                        "label": "Alert/Warning Severity",
                        "inputType": "double",
                        "name": "alertSeverity",
                        "names": [
                            "alert", "warning"
                        ],
                        "types": [
                            "select", "select"
                        ],
                        "options": [
                            AlertSeveritySerializer(AlertSeverity.objects.all(), many=True).data,
                            AlertSeveritySerializer(AlertSeverity.objects.all(), many=True).data
                        ],
                        "order": 6
                    },
                    {
                        "type": "input",
                        "label": "Send Email?",
                        "inputType": "double",
                        "name": "alertEmailFlag",
                        "names": [
                            "alert", "warning"
                        ],
                        "types": [
                            "input", "input"
                        ],
                        "inputTypes": [
                            "number", "number"
                        ],
                        "order": 7
                    },
                    {
                        "type": "input",
                        "label": "Sender",
                        "inputType": "double",
                        "name": "alertSender",
                        "names": [
                            "alert", "warning"
                        ],
                        "types": [
                            "input", "input"
                        ],
                        "inputTypes": [
                            "number", "number"
                        ],
                        "order": 8
                    },
                    {
                        "type": "input",
                        "label": "Recipients",
                        "inputType": "double",
                        "name": "alertRecipients",
                        "names": [
                            "alert", "warning"
                        ],
                        "types": [
                            "input", "input"
                        ],
                        "inputTypes": [
                            "text", "text"
                        ],
                        "order": 9
                    },
                    {
                        "type": "input",
                        "label": "Email Template",
                        "inputType": "double",
                        "name": "emailTemplate",
                        "names": [
                            "alert", "warning"
                        ],
                        "types": [
                            "input", "input"
                        ],
                        "inputTypes": [
                            "text", "text"
                        ],
                        "order": 10
                    },
                    {
                        "type": "input",
                        "label": "Send email option",
                        "inputType": "double",
                        "name": "emailOption",
                        "names": [
                            "alert", "warning"
                        ],
                        "types": [
                            "select", "select"
                        ],
                        "options": [
                            AlertEmailOptionSerializer(AlertEmailOption.objects.all(), many=True).data,
                            AlertEmailOptionSerializer(AlertEmailOption.objects.all(), many=True).data
                        ],
                        "order": 11
                    },
                ]
            },
            "clearance": {
                "alertsAndWarnings": [

                ],
                "documentHistory": [

                ]
            },
            "audit": {
                "auditHighlights": [
                    {
                        "type": "readOnly",
                        "label": "Created On",
                        "name": "insertDate",
                        "order": 1
                    },
                    {
                        "type": "readOnly",
                        "label": "Created By",
                        "name": "insertedBy",
                        "order": 2
                    },
                    {
                        "type": "readOnly",
                        "label": "Last Updated",
                        "name": "lastUpdatedDate",
                        "order": 3
                    },
                    {
                        "type": "readOnly",
                        "label": "Last Updated By",
                        "name": "lastUpdatedBy",
                        "order": 4
                    },
                    {
                        "type": "readOnly",
                        "label": "Last Viewed",
                        "name": "lastViewedDate",
                        "order": 5
                    },
                    {
                        "type": "readOnly",
                        "label": "Last Viewed By",
                        "name": "lastViewedBy",
                        "order": 6
                    },
                    {
                        "type": "readOnly",
                        "label": "Host Record ID",
                        "name": "hostRecordID",
                        "order": 7
                    },
                    {
                        "type": "readOnly",
                        "label": "Internal Record ID",
                        "name": "internalRecordId",
                        "order": 8
                    },
                ]
            }
        }
