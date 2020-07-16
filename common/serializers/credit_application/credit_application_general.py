from rest_framework import serializers
from common.models import CreditApplication, CreditApplicationBankingSummary, CreditApplicationStaff, BaseParty, Facility, FacilityArchived, Collateral, CollateralArchived
from common.models.general import *
from common.serializers import FacilitiesSerializer, CollateralsSerializer
from common.serializers.general import ProductsApplicableSerializer, PurposesApplicableSerializer
from common.serializers.credit_application.credit_application_staff import CreditApplicationStaffSerializer


class CreditApplicationGeneralSerializer(serializers.ModelSerializer):

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
                    "grid": FacilitiesSerializer(facility_model.objects.filter(ActionableFlag=True, CreditApplicationId_id=credit_application_id), many=True, model=facility_model).data,
                    "fields": {
                        "existingCommitment": "USD " + str(banking_summary.ExistingCommitment) if banking_summary else None,
                        "proposedExposure": "USD " + str(banking_summary.ProposedExposure) if banking_summary else None,
                        "existingExposure": "USD " + str(banking_summary.ExistingExposure) if banking_summary else None,
                        "proposedIncrease": "USD " + str(banking_summary.ProposedIncrease) if banking_summary else None,
                    }
                },
                "collateralHighlights": {
                    "grid": CollateralsSerializer(collateral_model.objects.filter(ActionableFlag=True, CreditApplicationId_id=credit_application_id), many=True, model=collateral_model).data,
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
        }

        return to_represent
