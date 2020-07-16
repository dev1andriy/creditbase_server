from common.models import BaseParty
from common.models.general import *
from common.serializers.configs import *


def generate_config(base_party_id):
    if base_party_id is None:
        base_party_config = {
            "type": "select",
            "label": "Base Party",
            "name": "baseParty",
            "isRequired": True,
            "options": BasePartyConfigSerializer(BaseParty.objects.all(), many=True).data,
            "placeholder": 'Select a party',
            "order": 1
        }
    else:
        base_party_config = {
            "type": "select",
            "label": "Base Party",
            "name": "baseParty",
            "isRequired": True,
            "options": [
                {
                    **BasePartyConfigSerializer(BaseParty.objects.get(BasePartyId=base_party_id)).data,
                    "autoSelect": True
                }
            ],
            "order": 1
        }

    return {
        "details": [
            base_party_config,
            {
                "type": "select",
                "label": "Relation type",
                "name": "relationType",
                "isRequired": True,
                "options": RelationTypeSerializer(RelationType.objects.all(), many=True).data,
                "placeholder": 'Select a type',
                "order": 2
            },
            # {
            #     "type": "input",
            #     "inputType": "search",
            #     "label": "Related Party",
            #     "name": "relatedParty",
            #     "order": 3
            # },
            {
                "type": "select",
                "label": "Related Party",
                "name": "relatedParty",
                "isRequired": True,
                "options": BasePartyConfigSerializer(BaseParty.objects.exclude(BasePartyId=base_party_id), many=True).data,
                "placeholder": 'Select a party',
                "order": 3
            },
            {
                "type": "input",
                "inputType": "number",
                "label": "Ownership %",
                "name": 'percentOwnership',
                "order": 4
            },
            {
                "type": "input",
                "inputType": "number",
                "label": "Voting Rights %",
                "name": 'percentVoting',
                "order": 5
            },
            {
                "type": "input",
                "inputType": "number",
                "label": "Number of shares",
                "name": "sharesCount",
                "order": 6
            },
            {
                "type": "input",
                "inputType": "number",
                "label": "Value of shared",
                "name": "sharesValue",
                "order": 7
            },
            {
                "type": "input",
                "inputType": "date",
                "label": "Relation Start Date",
                "name": "startDate",
                "order": 8
            },
            {
                "type": "input",
                "inputType": "date",
                "label": "Relation End Date",
                "name": "endDate",
                "order": 9
            },
            {
                "type": "input",
                "inputType": "text",
                "label": "Comment",
                "name": "comment",
                "order": 10
            },
            {
                "type": "checkbox",
                "label": "Controlling stake?",
                "name": "isControllingOwner",
                "order": 11
            },
            {
                "type": "checkbox",
                "label": "Link financials?",
                "name": "linkFinancials",
                "order": 12
            },
            {
                "type": "checkbox",
                "label": "Link banking information?",
                "name": "linkBankingInfo",
                "order": 13
            },
            {
                "type": "checkbox",
                "label": "Link applications?",
                "name": "linkApplications",
                "order": 14
            }],

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
