from django.contrib.auth.models import User

from common.models import BaseParty
from common.models.general import *
from common.serializers.configs import *

from common.configs.components.checklists import generate_checklists_config
from common.configs.components.credit_application_notes import generate_credit_applications_notes_config


def generate_config(edit=False, credit_application_id=None, base_party_id=None):

    business_unit_options = {}
    financial_institutions = FinancialInstitution.objects.all()
    for institution in financial_institutions:
        business_unit_options[str(institution.FinancialInstitutionId)] = BusinessUnitSerializer(BusinessUnit.objects.filter(FinancialInstitution=institution.FinancialInstitutionId), many=True).data

    config = {
        "creditApplicationId": credit_application_id,
        "basePartyId": base_party_id,
        # 'summary': {
        #     'applicationSummary': [
        #         {
        #             "type": "select",
        #             "label": "Base Party",
        #             "name": "baseParty",
        #             "options": BasePartySerializer(BaseParty.objects.all(), many=True).data,
        #             "placeholder": 'Select a party',
        #             "order": 1
        #         },
        #         {
        #             "type": "select",
        #             "label": "Application Source",
        #             "name": "applicationSource",
        #             "options": ApplicationSourceSerializer(ApplicationSource.objects.all(), many=True).data,
        #             "placeholder": 'Select a source',
        #             "order": 2
        #         },
        #         {
        #             "type": "readOnly",
        #             "label": "Application Id",
        #             "name": "creditApplicationId",
        #             "order": 3
        #         },
        #         {
        #             "type": "input",
        #             "inputType": "text",
        #             "label": "Products Selected",
        #             "name": "productsSelected",
        #             # "options": BasePartySerializer(BaseParty.objects.all(), many=True).data,
        #             # "placeholder": 'Select a party'
        #             "order": 4
        #         },
        #         {
        #             "type": "select",
        #             "label": "Application Type",
        #             "name": "applicationType",
        #             "options": ApplicationTypeSerializer(ApplicationType.objects.all(), many=True).data,
        #             "placeholder": 'Select a type',
        #             "order": 5
        #         },
        #         {
        #             "type": "input",
        #             "inputType": "text",
        #             "label": "Template Selected",
        #             "name": "templateSelected",
        #             # "options": BasePartySerializer(BaseParty.objects.all(), many=True).data,
        #             # "placeholder": 'Select a party'
        #             "order": 6
        #         },
        #
        #         {
        #             "type": "input",
        #             "inputType": "text",
        #             "label": "Application Purpose",
        #             "name": "applicationPurpose",
        #             # "options": ApplicationTypeSerializer(ApplicationType.objects.all(), many=True).data,
        #             # "placeholder": 'Select a purpose',
        #             "order": 7
        #         },
        #         {
        #             "type": "readOnly",
        #             "dataType": "date",
        #             "label": "Date Received",
        #             "name": "dateReceived",
        #             "order": 8
        #         },
        #
        #         {
        #             "type": "select",
        #             "label": "Application Status",
        #             "name": "applicationStatus",
        #             "options": ApplicationStatusSerializer(ApplicationStatus.objects.all(), many=True).data,
        #             "placeholder": 'Select a status',
        #             "order": 9
        #         },
        #         {
        #             "type": "readOnly",
        #             "dataType": "date",
        #             "label": "Date Created",
        #             "name": "dateCreated",
        #             "order": 10
        #         },
        #
        #         {
        #             "type": "select",
        #             "label": "Workflow Process",
        #             "name": "workflowProcess",
        #             "options": WorkflowProcessSerializer(WorkflowProcess.objects.all(), many=True).data,
        #             "placeholder": 'Select a workflow',
        #             "order": 11
        #         },
        #         {
        #             "type": "readOnly",
        #             "dataType": "date",
        #             "label": "Last updated",
        #             "name": "lastUpdated",
        #             "order": 12
        #         },
        #
        #         {
        #             "type": "select",
        #             "label": "Decision Status",
        #             "name": "decisionType",
        #             "options": DecisionTypeSerializer(DecisionType.objects.all(), many=True).data,
        #             "placeholder": 'Select a status',
        #             "order": 13
        #         },
        #         {
        #             "type": "readOnly",
        #             "dataType": "date",
        #             "label": "Last Reviewed Date",
        #             "name": "lastReviewedDate",
        #             "order": 14
        #         },
        #
        #         {
        #             "type": "select",
        #             "label": "Decline Reason",
        #             "name": "declineReason",
        #             "options": DeclineReasonSerializer(DeclineReason.objects.all(), many=True).data,
        #             "placeholder": 'Select a reason',
        #             "order": 15
        #         },
        #         {
        #             "type": "readOnly",
        #             "dataType": "date",
        #             "label": "Decision Date",
        #             "name": "decisionDate",
        #             "order": 16
        #         },
        #
        #         {
        #             "type": "select",
        #             "label": "Priority",
        #             "name": "applicationPriority",
        #             "options": ApplicationPrioritySerializer(ApplicationPriority.objects.all(), many=True).data,
        #             "placeholder": 'Select a priority',
        #             "order": 17
        #         },
        #         {
        #             "type": "readOnly",
        #             "dataType": "date",
        #             "label": "Expiry Date",
        #             "name": "expiryDate",
        #             "order": 18
        #         },
        #
        #         {
        #             "type": "select",
        #             "label": "Business Unit",
        #             "name": "businessUnit",
        #             "options": BusinessUnitSerializer(BusinessUnit.objects.all(), many=True).data,
        #             "placeholder": 'Select an unit',
        #             "order": 19
        #         },
        #         {
        #             "type": "readOnly",
        #             "dataType": "date",
        #             "label": "Next Review Date",
        #             "name": "nextReviewDate",
        #             "order": 20
        #         },
        #     ],
        #     "contacts": [
        #         {
        #             "type": "input",
        #             "inputType": "text",
        #             "label": "Telephone",
        #             "name": 'value',
        #             "order": 1
        #         },
        #         {
        #             "type": "select",
        #             "label": "Preference Type",
        #             "name": "preferenceType",
        #             "options": PreferenceTypeSerializer(PreferenceType.objects.all(), many=True).data,
        #             "placeholder": 'Select a preference type',
        #             "order": 2
        #         },
        #         {
        #             "type": "select",
        #             "label": "Telephone Type",
        #             "name": "telephoneType",
        #             "options": TelephoneTypeSerializer(TelephoneType.objects.all(), many=True).data,
        #             "placeholder": 'Select a telephone type',
        #             "order": 3
        #         }
        #     ],
        #     "addresses": [
        #         {
        #             "type": "select",
        #             "label": "Address Type",
        #             "name": "addressType",
        #             "options": AddressTypeSerializer(AddressType.objects.all(), many=True).data,
        #             "placeholder": 'Select a type',
        #             "order": 1
        #         },
        #         {
        #             "type": "select",
        #             "label": "Preference Type",
        #             "name": "preferenceType",
        #             "options": PreferenceTypeSerializer(PreferenceType.objects.all(), many=True).data,
        #             "placeholder": 'Select a type',
        #             "order": 2
        #         },
        #         {
        #             "type": "input",
        #             "inputType": "text",
        #             "label": "Address",
        #             "placeholder": "Street 1",
        #             "name": "street1",
        #             "order": 3,
        #             "requiredField": "addressType",
        #             "requiredValue": "1",
        #         },
        #         {
        #             "type": "input",
        #             "inputType": "text",
        #             "label": "",
        #             "placeholder": "Street 2",
        #             "name": "street2",
        #             "order": 4,
        #             "requiredField": "addressType",
        #             "requiredValue": "1",
        #         },
        #         {
        #             "type": "input",
        #             "inputType": "double",
        #             "names": [
        #                 "location1",
        #                 "location2",
        #                 "location3"
        #             ],
        #             "types": [
        #                 "input",
        #                 "input",
        #                 "input"
        #             ],
        #             "inputTypes": [
        #                 "text",
        #                 "text",
        #                 "text"
        #             ],
        #             "placeholders": [
        #                 "City",
        #                 "State",
        #                 ""
        #             ],
        #             "label": "",
        #             "name": "cityAndState",
        #             "order": 5,
        #             "requiredField": "addressType",
        #             "requiredValue": "1",
        #         },
        #         {
        #             "type": "input",
        #             "inputType": "double",
        #             "names": [
        #                 "country",
        #                 "postCode"
        #             ],
        #             "types": [
        #                 "select",
        #                 "input"
        #             ],
        #             "inputTypes": [
        #                 "",
        #                 "text"
        #             ],
        #             "options": [
        #                 CountrySerializer(Country.objects.all(), many=True).data,
        #                 ""
        #             ],
        #             "placeholders": [
        #                 "Country",
        #                 "Postal Code"
        #             ],
        #             "label": "",
        #             "name": "countryAndPostCode",
        #             "order": 6,
        #             "requiredField": "addressType",
        #             "requiredValue": "1",
        #         },
        #         {
        #             "type": "input",
        #             "inputType": "text",
        #             "label": "Email",
        #             "name": "value",
        #             "order": 7,
        #             "requiredField": "addressType",
        #             "requiredValue": "2",
        #         },
        #         {
        #
        #             "type": "select",
        #             "label": "Email Type",
        #             "name": "emailType",
        #             "options": EmailTypeSerializer(EmailType.objects.all(), many=True).data,
        #             "placeholder": 'Select a type',
        #             "requiredField": "addressType",
        #             "requiredValue": "2",
        #             "order": 8
        #         }
        #     ]
        # },
        "general": {
            "applicationHighlights": [
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
                }
                if base_party_id is not None else
                {
                    "type": "select",
                    "label": "Base Party",
                    "name": "baseParty",
                    "options": BasePartyConfigSerializer(BaseParty.objects.all(), many=True).data,
                    "order": 1,
                    "isRequired": True
                },
                {
                    "type": "select",
                    "label": "Application Source",
                    "name": "applicationSource",
                    "options": ApplicationSourceSerializer(ApplicationSource.objects.all(), many=True).data,
                    "placeholder": 'Select a source',
                    "order": 2
                },
                {
                    "type": "select",
                    "label": "Financial Institution",
                    "name": "financialInstitution",
                    "options": FinancialInstitutionSerializer(FinancialInstitution.objects.all(), many=True).data,
                    "placeholder": 'Select an institution',
                    "order": 3
                },
                {
                    "type": "select",
                    "label": "Business Unit",
                    "name": "businessUnit",
                    "optionsRelatedBy": "financialInstitution",
                    "relatedOptions": business_unit_options,
                    "placeholder": 'Select an unit',
                    "order": 4
                },
                {
                    "type": "readOnly",
                    "label": "Application Id",
                    "name": "creditApplicationId",
                    "order": 5
                },
                {
                    "type": "multiselect" if not edit else "readOnly",
                    "label": "Products Applicable",
                    "name": "productsApplicable",
                    "options": ProductTypeSerializer(ProductType.objects.all(), many=True).data,
                    "placeholder": 'Select applicable products',
                    "order": 6,
                    "isRequired": True if not edit else False
                },
                {
                    "type": "select" if not edit else "readOnly",
                    "label": "Application Type",
                    "name": "applicationType",
                    "options": ApplicationTypeSerializer(ApplicationType.objects.all(), many=True).data if not edit else None,
                    "placeholder": 'Select a type' if not edit else None,
                    "order": 7,
                    "isRequired": True if not edit else False
                },
                {
                    "type": "readOnly",
                    "label": "Template Selected",
                    "name": "templateSelected",
                    "order": 8
                },
                {
                    "type": "multiselect" if not edit else "readOnly",
                    "label": "Purposes Applicable",
                    "name": "purposesApplicable",
                    "options": PurposeSerializer(Purpose.objects.all(), many=True).data,
                    "placeholder": 'Select applicable products',
                    "order": 9,
                    "isRequired": True if not edit else False
                },
                {
                    "type": "input",
                    "inputType": "date",
                    "label": "Date Received",
                    "name": "dateReceived",
                    "order": 10
                },
                {
                    "type": "select",
                    "label": "Application Status",
                    "name": "applicationStatus",
                    "options": ApplicationStatusSerializer(ApplicationStatus.objects.all(), many=True).data,
                    "placeholder": 'Select a status',
                    "order": 11
                },
                {
                    "type": "readOnly",
                    "dataType": "date",
                    "label": "Date Created",
                    "name": "dateCreated",
                    "order": 12
                },
                {
                    "type": "readOnly",
                    "label": "Workflow Process",
                    "name": "workflowProcess",
                    "order": 13
                },
                {
                    "type": "readOnly",
                    "dataType": "date",
                    "label": "Last updated",
                    "name": "lastUpdated",
                    "order": 14
                },
                {
                    "type": "select",
                    "label": "Required authority level",
                    "name": "requiredAuthorityLevel",
                    "options": AuthorityLevelSerializer(AuthorityLevel.objects.all(), many=True).data,
                    "placeholder": 'Select a status',
                    "order": 15,
                    "isRequired": True,
                },
                {
                    "type": "select",
                    "label": "Decision Status",
                    "name": "decisionType",
                    "options": DecisionTypeSerializer(DecisionType.objects.all(), many=True).data,
                    "placeholder": 'Select a status',
                    "order": 16
                },
                {
                    "type": "input",
                    "inputType": "date",
                    "label": "Last Reviewed Date",
                    "name": "lastReviewedDate",
                    "order": 17
                },

                {
                    "type": "select",
                    "label": "Decline Reason",
                    "name": "declineReason",
                    "options": DeclineReasonSerializer(DeclineReason.objects.all(), many=True).data,
                    "placeholder": 'Select a reason',
                    "order": 18
                },
                {
                    "type": "readOnly",
                    "dataType": "date",
                    "label": "Decision Date",
                    "name": "decisionDate",
                    "order": 19
                },

                {
                    "type": "select",
                    "label": "Priority",
                    "name": "applicationPriority",
                    "options": ApplicationPrioritySerializer(ApplicationPriority.objects.all(), many=True).data,
                    "placeholder": 'Select a priority',
                    "order": 20
                },
                {
                    "type": "input",
                    "inputType": "date",
                    "label": "Expiry Date",
                    "name": "expiryDate",
                    "order": 21
                },
                {
                    "type": "input",
                    "inputType": "date",
                    "label": "Next Review Date",
                    "name": "nextReviewDate",
                    "order": 22
                },
            ],
            "applicationStaff": [
                {
                    "type": "select",
                    "label": "Staff Name",
                    "name": "relationshipStaffName",
                    "options": UserSerializer(User.objects.all().order_by('id'), many=True).data,
                    "placeholder": "Select a staff name",
                    "order": 1,
                    "isRequired": True
                },
                {
                    "type": "select",
                    "label": "Application Role",
                    "name": "relationType",
                    "options": RelationTypeSerializer(RelationType.objects.all(), many=True).data,
                    "placeholder": "Select a role",
                    "order": 2
                },
                {
                    "type": "checkbox",
                    "label": "Primary Contact",
                    "name": "primaryContact",
                    "order": 3
                },
            ],
            "facilityHighlights": [
                {
                    "type": "readOnly",
                    "label": "Total Limit",
                    "name": "existingCommitment",
                    "order": 1
                },
                {
                    "type": "readOnly",
                    "label": "Proposed Exposure",
                    "name": "proposedExposure",
                    "order": 2
                },
                {
                    "type": "readOnly",
                    "label": "Total Exposure",
                    "name": "existingExposure",
                    "order": 3
                },
                {
                    "type": "readOnly",
                    "label": "Total Increase",
                    "name": "proposedIncrease",
                    "order": 4
                },
            ],
            "collateralHighlights": [
                {
                    "type": "readOnly",
                    "label": "Total Market Value",
                    "name": "proposedMarketValue",
                    "order": 1
                },
                {
                    "type": "readOnly",
                    "label": "Coverage by MV",
                    "name": "proposedCoverageByMV",
                    "order": 2
                },
                {
                    "type": "readOnly",
                    "label": "Total Forced Sale Value",
                    "name": "proposedForcedSaleValue",
                    "order": 3
                },
                {
                    "type": "readOnly",
                    "label": "Coverage by FSV",
                    "name": "proposedCoverageByFSV",
                    "order": 4
                },
                {
                    "type": "readOnly",
                    "label": "Total Discounted Value",
                    "name": "proposedDiscountedValue",
                    "order": 5
                },
                {
                    "type": "readOnly",
                    "label": "Coverage by DV",
                    "name": "proposedCoverageByDV",
                    "order": 6
                },
                {
                    "type": "readOnly",
                    "label": "Total Lien Value",
                    "name": "proposedLienValue",
                    "order": 7
                },
                {
                    "type": "readOnly",
                    "label": "Coverage by LV",
                    "name": "proposedCoverageByLV",
                    "order": 8
                },
            ]
        },
        "checklists": generate_checklists_config(1, credit_application_id, base_party_id),
        "notes": generate_credit_applications_notes_config(),
    }

    return config
