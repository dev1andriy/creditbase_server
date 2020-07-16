from common.models import BaseParty
from common.serializers.configs import BasePartyConfigSerializer


def generate_config():
    return {
            "email": [
                {
                    "type": "toggleButtons",
                    "position": "right",
                    "label": "Respond mode",
                    "name": "respondMode",
                    "buttons": [
                        {
                            "label": "Reply all",
                            "value": "replyAll"
                        },
                        {
                            "label": "Reply",
                            "value": "reply"
                        },
                        {
                            "label": "Forward",
                            "value": "forward"
                        }
                    ],
                    "order": 1
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "From",
                    "name": 'from',
                    "order": 2
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "To",
                    "name": 'to',
                    "order": 3
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "CC",
                    "name": 'CC',
                    "order": 4
                },
                {
                    "type": "select",
                    "label": "Regarding",
                    "name": "regarding",
                    "options": BasePartyConfigSerializer(BaseParty.objects.all(), many=True).data,
                    "order": 5
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "Subject",
                    "name": 'subject',
                    "order": 6
                },
                {
                    "type": "wysiwyg",
                    "name": "emailBody",
                    "order": 7
                }
            ],
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

