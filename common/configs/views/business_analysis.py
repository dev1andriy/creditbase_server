from common.models import BaseParty
from common.models.general import *
from common.serializers.configs import *


def generate_config():
    return {
        "details": [
            {
                "type": "select",
                "label": "Industry",
                "name": "industry",
                "isRequired": True,
                "options": IndustrySerializer(Industry.objects.all(), many=True).data,
                "placeholder": 'Select an industry'
            },
            {
                "type": "select",
                "label": "Base Party",
                "name": "baseParty",
                "options": BasePartyConfigSerializer(BaseParty.objects.all(), many=True).data,
                "placeholder": 'Select a party'
            },
            {
                "type": "input",
                "inputType": "text",
                "label": "Product/Service",
                "name": 'productServiceSold'
            },
            {
                "type": "input",
                "inputType": "number",
                "label": "Revenue Contribution",
                "name": 'revenueContribution'
            },
            {
                "type": "input",
                "inputType": "number",
                "label": "% Total Revenue",
                "name": 'percentTotalRevenue'
            },
            {
                "type": "input",
                "inputType": "number",
                "label": "% Market Share",
                "name": 'percentMarketShare'
            },
            {
                "type": "input",
                "inputType": "number",
                "label": "Market Growth Rate",
                "name": 'growthRate'
            },
            {
                "type": "select",
                "label": "Buyer Power",
                "name": "buyerPower",
                "isRequired": True,
                "options": BuyerPowerSerializer(BuyerPower.objects.all(), many=True).data,
                "placeholder": 'Select a buyer power'
            },
            {
                "type": "select",
                "label": "Supplier Power",
                "name": "supplierPower",
                "isRequired": True,
                "options": SupplierPowerSerializer(SupplierPower.objects.all(), many=True).data,
                "placeholder": 'Select a supplier power'
            },
            {
                "type": "select",
                "label": "New Entrant Threat",
                "name": "newEntrantThreat",
                "isRequired": True,
                "options": NewEntrantThreatSerializer(NewEntrantThreat.objects.all(), many=True).data,
                "placeholder": 'Select a threat'
            },
            {
                "type": "select",
                "label": "Substitution Threat",
                "name": "substitutionThreat",
                "isRequired": True,
                "options": SubstitutionThreatSerializer(SubstitutionThreat.objects.all(), many=True).data,
                "placeholder": 'Select a threat'
            },
            {
                "type": "select",
                "label": "Competitive Rivalry",
                "name": "competitiveRivalry",
                "isRequired": True,
                "options": CompetitiveRivalrySerializer(CompetitiveRivalry.objects.all(), many=True).data,
                "placeholder": 'Select a rivalry'
            },
            {
                "type": "input",
                "inputType": "date",
                "label": "Start Date",
                "name": "startDate"
            },
            {
                "type": "input",
                "inputType": "date",
                "label": "End Date",
                "name": "endDate"
            },
            {
                "type": "input",
                "inputType": "text",
                "label": "Comment",
                "name": "comment"
            },
            {
                "type": "checkbox",
                "label": "Primary revenue stream?",
                "name": "isPrimaryRevenueStream"
            },
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
