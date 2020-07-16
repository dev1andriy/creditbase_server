from common.models import BasePartyEmail, BasePartyTelephone, BasePartyAddress
from common.models.general import *
from common.serializers.configs import *


def generate_config(base_party_id=None):
    config = {
        "details": {
            "basicDetails": [
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "Base Party Name",
                    "isRequired": True,
                    "name": 'basePartyName',
                    "order": 1
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "Host Party Id",
                    "name": "basePartyHostId",
                    "order": 2
                },
                {
                    "type": "select",
                    "label": "Party Category",
                    "name": "basePartyType",
                    "options": BasePartyTypeSerializer(BasePartyType.objects.all(), many=True).data,
                    "isRequired": True,
                    "placeholder": "Select a category",
                    "order": 3
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "Primary Legal ID",
                    "isRequired": True,
                    "name": "primaryLegalId",
                    "order": 4
                },
                {
                    "type": "select",
                    "label": "Party Profile",
                    "name": "profileType",
                    "isRequired": True,
                    "options": ProfileTypeSerializer(ProfileType.objects.all(), many=True).data,
                    "placeholder": 'Select a type',
                    "order": 5
                },
                {
                    "type": "select",
                    "label": "Financial Institution",
                    "name": "financialInstitution",
                    "isRequired": True,
                    "options": FinancialInstitutionSerializer(FinancialInstitution.objects.all(), many=True).data,
                    "placeholder": 'Select a financial institution',
                    "order": 6
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Legal Entity Type",
                    "isRequired": True,
                    "name": "legalEntityType",
                    "order": 7
                },
                {
                    "type": "select",
                    "label": "Business Unit",
                    "name": "businessUnit",
                    "isRequired": True,
                    "options": BusinessUnitSerializer(BusinessUnit.objects.all(), many=True).data,
                    "placeholder": 'Select a unit',
                    "order": 8
                },
                {
                    "type": "select",
                    "label": "Primary Sector",
                    "name": "primarySector",
                    "options": SectorSerializer(Sector.objects.all(), many=True).data,
                    "placeholder": 'Select a sector',
                    "isRequired": True,
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 9
                },
                {
                    "type": "input",
                    "inputType": "date",
                    "label": "Registration Date",
                    "name": "registrationDate",
                    "isRequired": True,
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 10
                },
                {
                    "type": "select",
                    "label": "Primary Industry",
                    "name": "primaryIndustry",
                    "options": IndustrySerializer(Industry.objects.all(), many=True).data,
                    "placeholder": 'Select an industry',
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 11
                },
                {
                    "type": "input",
                    "inputType": "date",
                    "label": "Start Date",
                    "name": "relationshipStartDate",
                    "order": 12
                },
                {
                    "type": "select",
                    "label": "Primary Activity",
                    "name": "primaryActivity",
                    "options": ActivityTypeSerializer(ActivityType.objects.all(), many=True).data,
                    "placeholder": 'Select an activity',
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 13
                },
                {
                    "type": "select",
                    "label": "Primary Email",
                    "name": "primaryEmailId",
                    "isRequired": True,
                    "options": [{
                        "label": "Add new email",
                        "value": "newItem",
                        "itemType": "email"
                    }],
                    "placeholder": 'Select an email',
                    "order": 14
                },
                {
                    "type": "select",
                    "label": "Operational Status",
                    "name": "operationalStatus",
                    "options": OperationalStatusSerializer(OperationalStatus.objects.all(), many=True).data,
                    "placeholder": 'Select a status',
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 15
                },
                {
                    "type": "select",
                    "label": "Primary Phone",
                    "name": "primaryTelephoneId",
                    "options": [{
                        "label": "Add a new phone",
                        "value": "newItem",
                        "itemType": "phone"
                    }],
                    "isRequired": True,
                    "placeholder": 'Select a phone',
                    "order": 16
                },
                {
                    "type": "select",
                    "label": "CRM Strategy",
                    "name": "CRMStrategy",
                    "options": CRMStrategySerializer(CRMStrategy.objects.all(), many=True).data,
                    "placeholder": 'Select a strategy',
                    "order": 17
                },
                {
                    "type": "select",
                    "label": "Primary Contact",
                    "name": "primaryContactId",
                    "options": [{
                        "label": "Add a new contact",
                        "value": "newItem",
                        "itemType": "contact"
                    }],
                    "placeholder": 'Select a contact',
                    "order": 18
                },
                {
                    "type": "select",
                    "label": "Registered in",
                    "name": "countryRegistration",
                    "options": CountryRegistrationSerializer(Country.objects.all(), many=True).data,
                    "placeholder": 'Select a country',
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 19
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Primary RM",
                    "isRequired": True,
                    "name": "primaryRM",
                    "order": 20
                },
            ],
            "bankingHighlights": [
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Total Commitment",
                    "name": 'commitmentTotal',
                    "order": 1
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Coverage Ratio",
                    "name": 'coverageRatiobyMV',
                    "order": 2
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Total Exposure",
                    "name": 'exposureTotal',
                    "order": 3
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Exposure at Risk",
                    "name": 'exposureAtRisk',
                    "order": 4
                },
                {
                    "type": "select",
                    "label": "Asset Classification",
                    "name": "assetClassification",
                    "options": AssetClassificationSerializer(AssetClassification.objects.all(),
                                                             many=True).data,
                    "placeholder": 'Select a classification',
                    "order": 5
                }
            ],
            "financialHighlights": [
                {
                    "type": "select",
                    "label": "Financial Model",
                    "name": "financialModel",
                    "options": FinancialModelSerializer(FinancialModel.objects.all(),
                                                        many=True).data,
                    "placeholder": 'Select a model',
                    "order": 1
                },
                {
                    "type": "select",
                    "label": "Fiscal Year End",
                    "name": "fiscalYearEnd",
                    "options": FiscalYearEndSerializer(FiscalYearEnd.objects.all(),
                                                       many=True).data,
                    "placeholder": 'Select an year end',
                    "order": 2
                },
                {
                    "type": "input",
                    "inputType": "date",
                    "label": "Recent statement",
                    "name": 'recentStatementDate',
                    "order": 3
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "History (Years)",
                    "name": 'statementHistory',
                    "order": 4
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Total Revenue",
                    "name": 'totalRevenue',
                    "order": 5
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Total Assets",
                    "name": 'totalAssets',
                    "order": 6
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Retained Earnings",
                    "name": 'retainedEarnings',
                    "order": 7
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "DSCR",
                    "name": 'DSCR',
                    "order": 8
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Total Equity",
                    "name": 'totalEquity',
                    "order": 9
                },
            ],
            "otherInformation": [
                {
                    "type": "select",
                    "label": "Governance",
                    "name": "governance",
                    "options": GovernanceTypeSerializer(GovernanceType.objects.all(),
                                                        many=True).data,
                    "placeholder": 'Select a governance',
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 1
                },
                {
                    "type": "select",
                    "label": "Decision making",
                    "name": "decisionMakingType",
                    "options": DecisionMakingTypeSerializer(DecisionMakingType.objects.all(),
                                                            many=True).data,
                    "placeholder": 'Select a decision making',
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 2
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Period at address",
                    "name": 'periodAtAddress',
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 3
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "Family business?",
                    "name": 'isFamilyBusiness',
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 4
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Total Employees",
                    "name": 'employeeCountTotal',
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 5
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "Group owned?",
                    "name": 'isGroupOwned',
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 6
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "Key Product Income",
                    "name": 'keyProductIncome',
                    "requiredField": "basePartyType",
                    "requiredValue": "2",
                    "order": 7
                },
            ]
        },
        "contactsAndAddresses": {
            "telephones": [
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "Telephone",
                    "name": 'value',
                    "order": 1
                },
                {
                    "type": "select",
                    "label": "Preference Type",
                    "name": "preferenceType",
                    "options": PreferenceTypeSerializer(PreferenceType.objects.all(), many=True).data,
                    "placeholder": 'Select a preference type',
                    "order": 2
                },
                {
                    "type": "select",
                    "label": "Telephone Type",
                    "name": "telephoneType",
                    "options": TelephoneTypeSerializer(TelephoneType.objects.all(), many=True).data,
                    "placeholder": 'Select a telephone type',
                    "order": 3
                }
            ],
            "addresses": [
                {
                    "type": "select",
                    "label": "Address Type",
                    "name": "addressType",
                    "options": AddressTypeSerializer(AddressType.objects.all(), many=True).data,
                    "placeholder": 'Select a type',
                    "order": 1
                },
                {
                    "type": "select",
                    "label": "Preference Type",
                    "name": "preferenceType",
                    "options": PreferenceTypeSerializer(PreferenceType.objects.all(), many=True).data,
                    "placeholder": 'Select a type',
                    "order": 2
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "Address",
                    "placeholder": "Street 1",
                    "name": "street1",
                    "order": 3,
                    "requiredField": "addressType",
                    "requiredValue": "1",
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "",
                    "placeholder": "Street 2",
                    "name": "street2",
                    "order": 4,
                    "requiredField": "addressType",
                    "requiredValue": "1",
                },
                {
                    "type": "input",
                    "inputType": "double",
                    "names": [
                        "location1",
                        "location2",
                        "location3"
                    ],
                    "types": [
                        "input",
                        "input",
                        "input"
                    ],
                    "inputTypes": [
                        "text",
                        "text",
                        "text"
                    ],
                    "placeholders": [
                        "City",
                        "State",
                        ""
                    ],
                    "label": "",
                    "name": "cityAndState",
                    "order": 5,
                    "requiredField": "addressType",
                    "requiredValue": "1",
                },
                {
                    "type": "input",
                    "inputType": "double",
                    "names": [
                        "country",
                        "postCode"
                    ],
                    "types": [
                        "select",
                        "input"
                    ],
                    "inputTypes": [
                        "",
                        "text"
                    ],
                    "options": [
                        CountrySerializer(Country.objects.all(), many=True).data,
                        ""
                    ],
                    "placeholders": [
                        "Country",
                        "Postal Code"
                    ],
                    "label": "",
                    "name": "countryAndPostCode",
                    "order": 6,
                    "requiredField": "addressType",
                    "requiredValue": "1",
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "Email",
                    "name": "value",
                    "order": 7,
                    "requiredField": "addressType",
                    "requiredValue": "2",
                },
                {

                    "type": "select",
                    "label": "Email Type",
                    "name": "emailType",
                    "options": EmailTypeSerializer(EmailType.objects.all(), many=True).data,
                    "placeholder": 'Select a type',
                    "requiredField": "addressType",
                    "requiredValue": "2",
                    "order": 8
                }
            ]
        },
        "identifiers": [
            {
                "type": "select",
                "label": "Identifier Category",
                "name": "identifierCategory",
                "options": IdentifierCategorySerializer(IdentifierCategory.objects.all(), many=True).data,
                "placeholder": 'Select an identifier category',
                "order": 1
            },
            {
                "type": "select",
                "label": "Identifier Type",
                "name": "identifierType",
                "options": IdentifierTypeSerializer(IdentifierType.objects.all(), many=True).data,
                "placeholder": 'Select an identifier type',
                "order": 2
            },
            {
                "type": "input",
                "inputType": "number",
                "label": "Identifier",
                "name": 'identifier',
                "order": 3
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
        },
        "tooltip": [
            {
                "type": "readOnly",
                "label": "Host Party ID",
                "name": "hostPartyId",
                "order": 1
            },
            {
                "type": "readOnly",
                "label": "Start Date",
                "name": "startDate",
                "order": 2
            },
            {
                "type": "readOnly",
                "label": "Party Profile",
                "name": "partyProfile",
                "order": 3
            },
            {
                "type": "readOnly",
                "label": "Sector",
                "name": "sector",
                "order": 4
            },
            {
                "type": "readOnly",
                "label": "Business Unit",
                "name": "businessUnit",
                "order": 5
            },
            {
                "type": "readOnly",
                "label": "Relationship Manager",
                "name": "relationshipManager",
                "order": 6
            }
        ]
    }

    # if base_party_id is not None:
    for i in config['details']['basicDetails']:
        if i['name'] == "primaryEmailId":
            i['options'] += EmailSerializer(BasePartyEmail.objects.filter(BasePartyId=base_party_id), many=True).data

        if i['name'] == "primaryTelephoneId":
            i['options'] += TelephoneSerializer(BasePartyTelephone.objects.filter(BasePartyId=base_party_id), many=True).data

        if i['name'] == "primaryContactId":
            i['options'] += AddressSerializer(BasePartyAddress.objects.filter(BasePartyId=base_party_id), many=True).data

    return config
