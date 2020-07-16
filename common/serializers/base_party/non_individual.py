from rest_framework import serializers

from common.models.base_party import BasePartyNonIndividual


class NonIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePartyNonIndividual
        fields = ('Governance', 'DecisionMakingType', 'PeriodAtAddress', 'IsFamilyBusiness',
                  'EmployeeCountTotal', 'IsGroupOwned', 'KeyProductIncome', 'PrimarySector',
                  'RegistrationDate', 'PrimaryIndustry', 'PrimaryActivity', 'OperationalStatus',
                  'CountryRegistration')

    def to_representation(self, instance):
        representation = super().to_representation(instance)



        to_represent = {
            'other_information': {
                'governance': representation.get('Governance', None),
                'decisionMakingType': representation.get('DecisionMakingType', None),
                'periodAtAddress': representation.get('PeriodAtAddress', None),
                'isFamilyBusiness': representation.get('IsFamilyBusiness', None),
                'employeeCountTotal': representation.get('EmployeeCountTotal', None),
                'isGroupOwned': representation.get('IsGroupOwned', None),
                'keyProductIncome': representation.get('KeyProductIncome', None),
            },
            'basic_details': {
                'PrimarySector': representation.get('PrimarySector', None),
                'RegistrationDate': representation.get('RegistrationDate', None),
                'PrimaryIndustry': representation.get('PrimaryIndustry', None),
                'PrimaryActivity': representation.get('PrimaryActivity', None),
                'OperationalStatus': representation.get('OperationalStatus', None),
                'CountryRegistration': representation.get('CountryRegistration', None)
            }
        }

        return to_represent
