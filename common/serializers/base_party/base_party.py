from rest_framework import serializers

from common.models.base_party import BaseParty, BasePartyBankingSummary, BasePartyFinancialsSummary, \
    BasePartyNonIndividual, BasePartyIdentifier, BasePartyAddress, BasePartyTelephone, BasePartyEmail
from common.serializers.base_party.banking_summary import BankingSummarySerializer
from common.serializers.base_party.financials_summary import FinancialsSummarySerializer
from common.serializers.base_party.non_individual import NonIndividualSerializer
from common.serializers.base_party.identifier import BasePartyIdentifierSerializer
from common.serializers.base_party.address import  BasePartyAddressSerializer
from common.serializers.base_party.email import BasePartyEmailSerializer
from common.serializers.base_party.telephone import BasePartyTelephoneSerializer



class BasePartySerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseParty
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        base_party_id = representation.get('BasePartyId', None)
        base_party_type = int(representation.get('BasePartyType')) if representation.get('BasePartyType') is not None else None
        if base_party_type == 2:
            non_individual = NonIndividualSerializer(BasePartyNonIndividual.objects.get(BasePartyId=base_party_id)).data

            basic_details = non_individual.get('basic_details')
            other_information = non_individual.get('other_information')

            print('basic details', basic_details)
        else:
            basic_details = {}
            other_information = None

        to_represent = {
            'basePartyId': representation.get('BasePartyId'),
            'details': {
                'basicDetails': {
                    'basePartyName': representation.get('BasePartyName', None),
                    'basePartyHostId': representation.get('BasePartyHostId', None),
                    'basePartyType': representation.get('BasePartyType', None),
                    'primaryLegalId': representation.get('PrimaryLegalId', None),
                    'profileType': representation.get('ProfileType', None),
                    'financialInstitution': representation.get('FinancialInstitution', None),
                    'legalEntityType': representation.get('LegalEntityType', None),
                    'businessUnit': representation.get('BusinessUnit', None),
                    'primarySector': basic_details.get('PrimarySector', None),
                    'registrationDate': basic_details.get('RegistrationDate', None),
                    'primaryIndustry': basic_details.get('PrimaryIndustry', None),
                    'relationshipStartDate': representation.get('RelationshipStartDate', None),
                    'primaryActivity': basic_details.get('PrimaryActivity', None),
                    'primaryEmailId': representation.get('PrimaryEmailId', None),
                    'operationalStatus': basic_details.get('OperationalStatus', None),
                    'primaryTelephoneId': representation.get('PrimaryTelephoneId', None),
                    'CRMStrategy': representation.get('CRMStrategy', None),
                    'primaryContactId': representation.get('PrimaryContactId', None),
                    'countryRegistration': basic_details.get('CountryRegistration', None),
                    'primaryRM': representation.get('PrimaryRM', None)
                },
                'bankingHighlights': BankingSummarySerializer(BasePartyBankingSummary.objects.get(BasePartyId=base_party_id)).data,
                'financialHighlights': FinancialsSummarySerializer(BasePartyFinancialsSummary.objects.get(BasePartyId=base_party_id)).data,
                'otherInformation': other_information
            },
            'identifiers': {
                'identifiers': BasePartyIdentifierSerializer(BasePartyIdentifier.objects.filter(BasePartyId=representation.get('BasePartyId')), many=True).data
            },
            'contactsAndAddresses': {
                'telephones': BasePartyTelephoneSerializer(BasePartyTelephone.objects.filter(BasePartyId=representation.get('BasePartyId')), many=True).data,
                'addresses': BasePartyEmailSerializer(BasePartyEmail.objects.filter(BasePartyId=representation.get('BasePartyId')), many=True).data + BasePartyAddressSerializer(BasePartyAddress.objects.filter(BasePartyId=representation.get('BasePartyId')), many=True).data
            },
            'tooltip': {
                'hostPartyId': representation.get('BasePartyHostId', None),
                'startDate': representation.get('RelationshipStartDate', None),
                'partyProfile': representation.get('ProfileType', None),
                'sector': basic_details.get('PrimarySector', None),
                'businessUnit': representation.get('BusinessUnit', None),
                'relationshipManager': representation.get('PrimaryRM', None)
            },
            'basePartyHighlights': [
                {
                    'title': 'Open applications',
                    'value': '123'
                },
                {
                    'title': 'Closed applications',
                    'value': '123'
                },
                {
                    'title': 'Current rating',
                    'value': '123'
                },
                {
                    'title': 'Last rating',
                    'value': '123'
                },
                {
                    'title': 'Last statement',
                    'value': '123'
                },
                {
                    'title': 'Total assets',
                    'value': '123'
                },
                {
                    'title': 'Total revenue',
                    'value': '123'
                },
                {
                    'title': 'Total exposure',
                    'value': '123'
                },
                {
                    'title': 'Total collateral',
                    'value': '123'
                },
                {
                    'title': 'Discounted Coverage',
                    'value': '123'
                },
                {
                    'title': 'BIS Classfication',
                    'value': '123'
                },
                {
                    'title': 'PD days',
                    'value': '123'
                },
                {
                    'title': 'Exposure at Risk',
                    'value': '123'
                },
            ]
        }

        return to_represent
