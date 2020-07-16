from rest_framework import serializers
from common.models import CreditApplication, CreditApplicationBankingSummary, CreditApplicationStaff, BaseParty, Facility, FacilityArchived, Collateral, CollateralArchived
from common.models.general import *
from common.serializers import FacilitiesSerializer, CollateralsSerializer
from common.serializers.general import ProductsApplicableSerializer, PurposesApplicableSerializer
from common.serializers.credit_application.credit_application_staff import CreditApplicationStaffSerializer
from common.utils.checklists_data import generate_checklists_data
from common.utils.credit_application_notes_data import generate_credit_applications_notes_data
from common.utils.credit_application_sections import get_credit_application_sections_statues


class CreditApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditApplication
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        credit_application_id = representation['CreditApplicationId']
        banking_summary = CreditApplicationBankingSummary.objects.filter(CreditApplicationId=credit_application_id).first()

        if representation['DecisionType'] is not None:
            facility_model = FacilityArchived
            collateral_model = CollateralArchived
        else:
            facility_model = Facility
            collateral_model = Collateral

        to_represent = {
            'creditApplicationId': credit_application_id,
            'basePartyId': representation['BasePartyId'],
            'general': {
                'applicationHighlights': {
                    'baseParty': BaseParty.objects.get(BasePartyId=representation['BasePartyId']).BasePartyName if representation['BasePartyId'] is not None else None,
                    'applicationSource': representation['ApplicationSource'],
                    'financialInstitution': representation['FinancialInstitution'],
                    'businessUnit': representation['BusinessUnit'],
                    'creditApplicationId': representation['CreditApplicationId'],
                    'productsApplicable': ProductsApplicableSerializer(ProductType.objects.filter(ProductTypeId__in=representation['ProductsApplicable']), many=True).data if representation['ProductsApplicable'] is not None else None,
                    'applicationType': ApplicationType.objects.get(ApplicationTypeId=representation['ApplicationType']).Description if representation['ApplicationType'] is not None else None,
                    'templateSelected': ApplicationTemplate.objects.get(ApplicationTemplateId=representation['ApplicationTemplate']).Description if representation['ApplicationTemplate'] is not None else None,
                    'purposesApplicable': PurposesApplicableSerializer(Purpose.objects.filter(PurposeId__in=representation['PurposesApplicable']), many=True).data if representation['PurposesApplicable'] is not None else None,
                    'dateReceived': representation['ReceivedDate'],
                    'applicationStatus': representation['ApplicationStatus'],
                    'dateCreated': representation['InsertDate'],
                    'workflowProcess': WorkflowProcess.objects.get(WorkflowProcessId=representation['WorkflowProcess']).Description if representation['WorkflowProcess'] is not None else None,
                    'lastUpdated': representation['LastUpdatedDate'],
                    'decisionType': representation['DecisionType'],
                    'requiredAuthorityLevel': representation['RequiredAuthorityLevel'],
                    'lastReviewedDate': representation['LastReviewDate'],
                    'declineReason': representation['DeclineReason'],
                    'decisionDate': representation['DecisionDate'],
                    'applicationPriority': representation['ApplicationPriority'],
                    'expiryDate': representation['DecisionExpiryDate'],
                    'nextReviewDate': representation['DecisionNextReviewDate'],
                },
                "applicationStaff": CreditApplicationStaffSerializer(CreditApplicationStaff.objects.filter(CreditApplicationId=representation['CreditApplicationId']), many=True).data,
                "facilityHighlights": {
                    "grid": FacilitiesSerializer(facility_model.objects.filter(ActionableFlag=True, CreditApplicationId_id=credit_application_id), model=facility_model),
                    "fields": {
                        "existingCommitment": "USD " + str(banking_summary.ExistingCommitment) if banking_summary else None,
                        "proposedExposure": "USD " + str(banking_summary.ProposedExposure) if banking_summary else None,
                        "existingExposure": "USD " + str(banking_summary.ExistingExposure) if banking_summary else None,
                        "proposedIncrease": "USD " + str(banking_summary.ProposedIncrease) if banking_summary else None,
                    }
                },
                "collateralHighlights": {
                    "grid": CollateralsSerializer(collateral_model.objects.filter(ActionableFlag=True, CreditApplicationId_id=credit_application_id), model=collateral_model),
                    "fields": {
                        "proposedMarketValue": "USD " + str(banking_summary.ProposedMarketValue) if banking_summary else None,
                        "proposedCoverageByMV": banking_summary.ProposedCoverageByMV if banking_summary else None,
                        "proposedForcedSaleValue": "USD " + str(banking_summary.ProposedForcedSaleValue) if banking_summary else None,
                        "proposedCoverageByFSV": banking_summary.ProposedCoverageByFSV if banking_summary else None,
                        "proposedDiscountedValue": "USD " + str(banking_summary.ProposedDiscountedValue) if banking_summary else None,
                        "proposedCoverageByDV": banking_summary.ProposedCoverageByDV if banking_summary else None,
                        "proposedLienValue": "USD " + str(banking_summary.ProposedLienValue) if banking_summary else None,
                        "proposedCoverageByLV": banking_summary.ProposedCoverageByLV if banking_summary else None,
                    }
                },


            },
            "checklists": generate_checklists_data(credit_application_id, self.context.get('host')),
            "notes": generate_credit_applications_notes_data(credit_application_id, representation['BasePartyId'])
        }

        if self.context.get('get_statuses'):
            statuses = get_credit_application_sections_statues(credit_application_id)

            to_represent['applicationSectionsStatuses'] = statuses['application_sections_statuses']
            to_represent['creditApplicationStatus'] = statuses['credit_application_status']

        return to_represent
