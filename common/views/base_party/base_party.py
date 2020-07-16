from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from common.serializers.base_party.base_party import BasePartySerializer
from common.utils.return_value_or_none import return_value_or_none

from common.models import BaseParty, BasePartyBankingSummary, BasePartyFinancialsSummary, BasePartyNonIndividual, BasePartyIndividual, BasePartyIdentifier, BasePartyEmail, BasePartyTelephone, BasePartyAddress, Country
from common.serializers import BasePartiesSerializer
from common.configs.views.base_party import generate_config
from common.views.recent_item import set_recent_item

base_party_details_basic_details_base_party_fields = [
    {'db_field': 'BasePartyName', 'field_label': 'basePartyName'},
    {'db_field': 'LegalEntityType', 'field_label': 'legalEntityType'},
    {'db_field': 'PrimaryRM', 'field_label': 'primaryRM'},
    {'db_field': 'BasePartyHostId', 'field_label': 'basePartyHostId'},
    {'db_field': 'BasePartyType_id', 'field_label': 'basePartyType'},
    {'db_field': 'PrimaryLegalId', 'field_label': 'primaryLegalId'},
    {'db_field': 'ProfileType_id', 'field_label': 'profileType'},
    {'db_field': 'FinancialInstitution_id', 'field_label': 'financialInstitution'},
    {'db_field': 'BusinessUnit_id', 'field_label': 'businessUnit'},
    {'db_field': 'RelationshipStartDate', 'field_label': 'relationshipStartDate'},
    {'db_field': 'CRMStrategy_id', 'field_label': 'CRMStrategy'}
]

base_party_details_basic_details_non_individual_fields = [
    {'db_field': 'PrimarySector_id', 'field_label': 'primarySector'},
    {'db_field': 'RegistrationDate', 'field_label': 'registrationDate'},
    {'db_field': 'PrimaryIndustry_id', 'field_label': 'primaryIndustry'},
    {'db_field': 'PrimaryActivity_id', 'field_label': 'primaryActivity'},
    {'db_field': 'OperationalStatus_id', 'field_label': 'operationalStatus'},
    {'db_field': 'CountryRegistration_id', 'field_label': 'countryRegistration'},
]


base_party_details_banking_summary_fields = [
    {'db_field': 'CommitmentTotal', 'field_label': 'commitmentTotal'},
    {'db_field': 'CoverageRatiobyMV', 'field_label': 'coverageRatiobyMV'},
    {'db_field': 'ExposureTotal', 'field_label': 'exposureTotal'},
    {'db_field': 'ExposureAtRisk', 'field_label': 'exposureAtRisk'},
    {'db_field': 'AssetClassification_id', 'field_label': 'assetClassification'},
]


base_party_details_financial_summary_fields = [
    {'db_field': 'FinancialModel_id', 'field_label': 'financialModel'},
    {'db_field': 'FiscalYearEnd_id', 'field_label': 'fiscalYearEnd'},
    {'db_field': 'RecentStatementDate', 'field_label': 'recentStatementDate'},
    {'db_field': 'StatementHistory', 'field_label': 'statementHistory'},
    {'db_field': 'TotalRevenue', 'field_label': 'totalRevenue'},
    {'db_field': 'TotalAssets', 'field_label': 'totalAssets'},
    {'db_field': 'RetainedEarnings', 'field_label': 'retainedEarnings'},
    {'db_field': 'DSCR', 'field_label': 'DSCR'},
    {'db_field': 'TotalEquity', 'field_label': 'totalEquity'},
]


base_party_details_other_information_fields = [
    {'db_field': 'Governance_id', 'field_label': 'governance'},
    {'db_field': 'DecisionMakingType_id', 'field_label': 'decisionMakingType'},
    {'db_field': 'PeriodAtAddress', 'field_label': 'periodAtAddress'},
    {'db_field': 'IsFamilyBusiness', 'field_label': 'isFamilyBusiness'},
    {'db_field': 'EmployeeCountTotal', 'field_label': 'employeeCountTotal'},
    {'db_field': 'IsGroupOwned', 'field_label': 'isGroupOwned'},
    {'db_field': 'KeyProductIncome', 'field_label': 'keyProductIncome'},
]


class BasePartyAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        global base_party_type
        global base_party_non_individual

        global primary_email_id
        global primary_telephone_id
        global primary_contact_id

        if request.data is None:
            return Response('Data is missing', status=400)

        base_party = BaseParty.objects.create()
        base_party_banking_summary = BasePartyBankingSummary.objects.create(BasePartyId=base_party)
        base_party_financial_summary = BasePartyFinancialsSummary.objects.create(BasePartyId=base_party)

        if 'details' in request.data:
            details = request.data.get('details', {})

            if 'basicDetails' in details:
                basic_details = details.get('basicDetails', {})

                primary_email_id = basic_details.get('primaryEmailId', None)
                primary_telephone_id = basic_details.get('primaryTelephoneId', None)
                primary_contact_id = basic_details.get('primaryContactId', None)

                base_party_type = basic_details.get('basePartyType') if basic_details.get('basePartyType') is not None else None
                if int(base_party_type) == 1:
                    base_party_individual = BasePartyIndividual.objects.create(BasePartyId=base_party)
                elif int(base_party_type) == 2:
                    base_party_non_individual = BasePartyNonIndividual.objects.create(BasePartyId=base_party)

                    for field in base_party_details_basic_details_non_individual_fields:
                        setattr(base_party_non_individual, field['db_field'], basic_details.get(field['field_label'], None))

                for field in base_party_details_basic_details_base_party_fields:
                    setattr(base_party, field['db_field'], basic_details.get(field['field_label'], None))

                base_party.save()

            if 'bankingHighlights' in details:
                banking_highlights = details.get('bankingHighlights', {})

                for field in base_party_details_banking_summary_fields:
                    setattr(base_party_banking_summary, field['db_field'], banking_highlights.get(field['field_label'], None))

                base_party_banking_summary.save()

            if 'financialHighlights' in details:
                financial_highlights = details.get('financialHighlights', {})

                for field in base_party_details_financial_summary_fields:
                    setattr(base_party_financial_summary, field['db_field'], financial_highlights.get(field['field_label'], None))

                base_party_financial_summary.save()

            if 'otherInformation' in details and base_party_type is not None and base_party_non_individual is not None:
                other_information = details.get('otherInformation', {})

                for field in base_party_details_other_information_fields:
                    setattr(base_party_non_individual, field['db_field'], other_information.get(field['field_label'], None))

                base_party_non_individual.save()

        if 'identifiers' in request.data:
            _identifiers = request.data.get('identifiers', {})

            if 'identifiers' in _identifiers:
                identifiers = _identifiers.get('identifiers', [])

                if len(identifiers) > 0:
                    for identifier in identifiers:
                        if 'temp' in str(identifier.get('id', '')):
                            base_party_identifier = BasePartyIdentifier()
                            base_party_identifier.BasePartyId = base_party
                            base_party_identifier.Identifier = identifier.get('identifier', None)
                            base_party_identifier.IdentifierCategory_id = identifier.get('identifierCategory', None)
                            base_party_identifier.IdentifierType_id = identifier.get('identifierType', None)
                            base_party_identifier.save()

        if 'contactsAndAddresses' in request.data:
            contacts_and_addresses = request.data.get('contactsAndAddresses', {})

            if 'telephones' in contacts_and_addresses:
                telephones = contacts_and_addresses.get('telephones', [])

                if len(telephones) > 0:
                    for telephone in telephones:
                        if 'temp' in str(telephone.get('id', '')):
                            base_party_telephone = BasePartyTelephone()
                            base_party_telephone.BasePartyId = base_party
                            base_party_telephone.TelFormattedFinal = telephone.get('value', None)
                            base_party_telephone.PreferenceType_id = telephone.get('preferenceType', None)
                            base_party_telephone.TelephoneType_id = telephone.get('telephoneType', None)
                            base_party_telephone.save()

                            if primary_telephone_id == telephone.get('id', None):
                                base_party.PrimaryTelephoneId = base_party_telephone
                                base_party.save()

            if 'addresses' in contacts_and_addresses:
                addresses = contacts_and_addresses.get('addresses', [])

                if len(addresses) > 0:
                    for address in addresses:
                        if address.get('addressType', None) is not None and address.get('addressType', None).isdigit() and int(address.get('addressType', None)) == 1:
                            if 'temp' in str(address.get('id', '')):
                                base_party_address = BasePartyAddress()
                                base_party_address.BasePartyId = base_party
                                base_party_address.AddressType_id = address.get('addressType', None)
                                base_party_address.PreferenceType_id = address.get('preferenceType', None)
                                base_party_address.Street1 = address.get('street1', None)
                                base_party_address.Street2 = address.get('street2', None)
                                base_party_address.Level1Location = return_value_or_none(address.get('cityAndState', {}), 'location1')
                                base_party_address.Level2Location = return_value_or_none(address.get('cityAndState', {}), 'location2')
                                base_party_address.Level3Location = return_value_or_none(address.get('cityAndState', {}), 'location3')
                                base_party_address.Country_id = return_value_or_none(address.get('countryAndPostCode', {}), 'country')
                                base_party_address.PostCode = return_value_or_none(address.get('countryAndPostCode', {}), 'postCode')

                                country_query_set = Country.objects.filter(CountryId=return_value_or_none(address.get('countryAndPostCode', {}), 'country'))

                                address_final = '{} {} {} {} {} {}'.format(country_query_set.first().Description if country_query_set.exists() else '',
                                                                           return_value_or_none(address.get('cityAndState', {}), 'location1'),
                                                                           return_value_or_none(address.get('cityAndState', {}), 'location2'),
                                                                           return_value_or_none(address.get('cityAndState', {}), 'location3'),
                                                                           address.get('street1', None),
                                                                           address.get('street2', None))

                                base_party_address.AddressFinal = address_final
                                base_party_address.save()

                                if primary_contact_id == address.get('id', None):
                                    base_party.PrimaryContactId = base_party_address
                                    base_party.save()

                        elif address.get('addressType', None) is not None and address.get('addressType', None).isdigit() and int(address.get('addressType', None)) == 2:
                            if 'temp' in str(address.get('id', '')):
                                base_party_email = BasePartyEmail()
                                base_party_email.BasePartyId = base_party
                                base_party_email.EmailFinal = address.get('value', None)
                                base_party_email.EmailType_id = address.get('emailType', None)
                                base_party_email.AddressType_id = address.get('addressType', None)
                                base_party_email.PreferenceType_id = address.get('preferenceType', None)
                                base_party_email.save()

                                if primary_email_id == address.get('id', None):
                                    base_party.PrimaryEmailId = base_party_email
                                    base_party.save()

        response = BasePartiesSerializer(base_party).data

        return JsonResponse(response)

    def put(self, request, *args, **kwargs):
        global base_party_type
        global base_party_non_individual

        primary_email_id = None
        primary_telephone_id = None
        primary_contact_id = None

        if request.data is None:
            return Response('Data is missing', status=400)

        base_party_id = request.data.get('basePartyId', None)
        if base_party_id is None:
            return Response('Base Party Id is missing', status=400)

        base_party = BaseParty.objects.get(BasePartyId=base_party_id)
        base_party_banking_summary = BasePartyBankingSummary.objects.get(BasePartyId=base_party_id)
        base_party_financial_summary = BasePartyFinancialsSummary.objects.get(BasePartyId=base_party_id)

        existing_identifiers = []
        existing_telephones = []
        existing_addresses = []
        existing_emails = []

        base_party_type = base_party.BasePartyType_id

        if int(base_party_type) == 1:
            pass
        elif int(base_party_type) == 2:
            base_party_non_individual = BasePartyNonIndividual.objects.get_or_create(BasePartyId=base_party_id)[0]

        if 'details' in request.data:
            details = request.data.get('details', {})

            if 'basicDetails' in details:
                basic_details = details.get('basicDetails', {})

                primary_email_id = basic_details.get('primaryEmailId', None)
                primary_telephone_id = basic_details.get('primaryTelephoneId', None)
                primary_contact_id = basic_details.get('primaryContactId', None)

                if 'temp' not in str(primary_email_id):
                    base_party.PrimaryEmailId_id = primary_email_id

                if 'temp' not in str(primary_telephone_id):
                    base_party.PrimaryTelephoneId_id = primary_telephone_id

                if 'temp' not in str(primary_contact_id):
                    base_party.PrimaryContactId_id = primary_contact_id

                base_party_type = basic_details.get('basePartyType') if basic_details.get('basePartyType') is not None else base_party_type
                if int(base_party_type) == 1:
                    pass
                elif int(base_party_type) == 2:
                    for field in base_party_details_basic_details_non_individual_fields:
                        setattr(base_party_non_individual, field['db_field'], basic_details.get(field['field_label'], None))

                    base_party_non_individual.save()

                for field in base_party_details_basic_details_base_party_fields:
                    setattr(base_party, field['db_field'], basic_details.get(field['field_label'], None))

                base_party.save()

            if 'bankingHighlights' in details:
                banking_highlights = details.get('bankingHighlights', {})

                for field in base_party_details_banking_summary_fields:
                    setattr(base_party_banking_summary, field['db_field'], banking_highlights.get(field['field_label'], None))

                base_party_banking_summary.save()

            if 'financialHighlights' in details:
                financial_highlights = details.get('financialHighlights', {})

                for field in base_party_details_financial_summary_fields:
                    setattr(base_party_financial_summary, field['db_field'], financial_highlights.get(field['field_label'], None))

                base_party_financial_summary.save()

            if 'otherInformation' in details and base_party_type is not None and base_party_non_individual is not None:
                other_information = details.get('otherInformation', {})

                for field in base_party_details_other_information_fields:

                    setattr(base_party_non_individual, field['db_field'], other_information.get(field['field_label'], None))

                base_party_non_individual.save()
        if 'identifiers' in request.data:
            _identifiers = request.data.get('identifiers', {})

            if 'identifiers' in _identifiers:
                identifiers = _identifiers.get('identifiers', [])

                if len(identifiers) > 0:
                    for identifier in identifiers:
                        if 'temp' in str(identifier.get('id', '')):
                            base_party_identifier = BasePartyIdentifier()
                            base_party_identifier.BasePartyId = base_party
                            base_party_identifier.Identifier = identifier.get('identifier', None)
                            base_party_identifier.IdentifierCategory_id = identifier.get('identifierCategory', None)
                            base_party_identifier.IdentifierType_id = identifier.get('identifierType', None)
                            base_party_identifier.save()

                            existing_identifiers.append(base_party_identifier.BasePartyIdentifierId)
                        elif 'temp' not in str(identifier.get('id', '')) and 'isChange' in identifier and identifier.get('isChange', False):
                            base_party_identifier = BasePartyIdentifier.objects.get(BasePartyIdentifierId=identifier.get('id'))
                            base_party_identifier.Identifier = identifier.get('identifier', None)
                            base_party_identifier.IdentifierCategory_id = identifier.get('identifierCategory', None)
                            base_party_identifier.IdentifierType_id = identifier.get('identifierType', None)
                            base_party_identifier.save()

                            existing_identifiers.append(base_party_identifier.BasePartyIdentifierId)

                        elif 'temp' not in str(identifier.get('id', '')) and isinstance(identifier.get('id', None), int) and 'isChange' not in identifier:
                            existing_identifiers.append(identifier.get('id'))

                BasePartyIdentifier.objects.exclude(BasePartyIdentifierId__in=existing_identifiers).delete()

        if 'contactsAndAddresses' in request.data:
            contacts_and_addresses = request.data.get('contactsAndAddresses', {})

            if 'telephones' in contacts_and_addresses:
                telephones = contacts_and_addresses.get('telephones', [])

                if len(telephones) > 0:
                    for telephone in telephones:
                        if 'temp' in str(telephone.get('id', '')):
                            base_party_telephone = BasePartyTelephone()
                            base_party_telephone.BasePartyId = base_party
                            base_party_telephone.TelFormattedFinal = telephone.get('value', None)
                            base_party_telephone.PreferenceType_id = telephone.get('preferenceType', None)
                            base_party_telephone.TelephoneType_id = telephone.get('telephoneType', None)
                            base_party_telephone.save()

                            existing_telephones.append(base_party_telephone.BasePartyTelephoneId)

                            if primary_telephone_id == telephone.get('id', None):
                                base_party.PrimaryTelephoneId = base_party_telephone
                                base_party.save()

                        elif 'temp' not in str(telephone.get('id', '')) and 'isChange' in telephone and telephone.get('isChange', False):
                            base_party_telephone = BasePartyTelephone.objects.get(BasePartyTelephoneId=telephone.get('id'))
                            base_party_telephone.BasePartyId = base_party
                            base_party_telephone.TelFormattedFinal = telephone.get('value', None)
                            base_party_telephone.PreferenceType_id = telephone.get('preferenceType', None)
                            base_party_telephone.TelephoneType_id = telephone.get('telephoneType', None)
                            base_party_telephone.save()

                            existing_telephones.append(base_party_telephone.BasePartyTelephoneId)

                        elif 'temp' not in str(telephone.get('id', '')) and isinstance(telephone.get('id', None), int) and 'isChange' not in telephone:
                            existing_telephones.append(telephone.get('id'))
                BasePartyTelephone.objects.exclude(BasePartyTelephoneId__in=[*existing_telephones, base_party.PrimaryTelephoneId_id]).delete()

            if 'addresses' in contacts_and_addresses:
                addresses = contacts_and_addresses.get('addresses', [])

                if len(addresses) > 0:
                    for address in addresses:
                        if address.get('addressType', None) is not None and str(address.get('addressType', None)).isdigit() and int(address.get('addressType', None)) == 1:
                            if 'temp' in str(address.get('id', '')):
                                base_party_address = BasePartyAddress()
                                base_party_address.BasePartyId = base_party
                                base_party_address.AddressType_id = address.get('addressType', None)
                                base_party_address.PreferenceType_id = address.get('preferenceType', None)
                                base_party_address.Street1 = address.get('street1', None)
                                base_party_address.Street2 = address.get('street2', None)
                                base_party_address.Level1Location = return_value_or_none(address.get('cityAndState', {}), 'location1')
                                base_party_address.Level2Location = return_value_or_none(address.get('cityAndState', {}), 'location2')
                                base_party_address.Level3Location = return_value_or_none(address.get('cityAndState', {}), 'location3')
                                base_party_address.Country_id = return_value_or_none(address.get('countryAndPostCode', {}), 'country')
                                base_party_address.PostCode = return_value_or_none(address.get('countryAndPostCode', {}), 'postCode')

                                country_query_set = Country.objects.filter(CountryId=return_value_or_none(address.get('countryAndPostCode', {}), 'country'))

                                address_final = '{} {} {} {} {} {}'.format(country_query_set.first().Description if country_query_set.exists() else '',
                                                                           return_value_or_none(address.get('cityAndState', {}), 'location1'),
                                                                           return_value_or_none(address.get('cityAndState', {}), 'location2'),
                                                                           return_value_or_none(address.get('cityAndState', {}), 'location3'),
                                                                           address.get('street1', None),
                                                                           address.get('street2', None))

                                base_party_address.AddressFinal = address_final
                                base_party_address.save()

                                existing_addresses.append(base_party_address.BasePartyAddressId)

                                if primary_contact_id == address.get('id', None):
                                    base_party.PrimaryContactId = base_party_address
                                    base_party.save()

                            elif 'temp' not in str(address.get('id', '')) and 'isChange' in address and address.get('isChange', False):
                                base_party_address = BasePartyAddress.objects.get(BasePartyAddressId=address.get('id'))
                                base_party_address.BasePartyId = base_party
                                base_party_address.AddressType_id = address.get('addressType', None)
                                base_party_address.PreferenceType_id = address.get('preferenceType', None)
                                base_party_address.Street1 = address.get('street1', None)
                                base_party_address.Street2 = address.get('street2', None)
                                base_party_address.Level1Location = return_value_or_none(address.get('cityAndState', {}), 'location1')
                                base_party_address.Level2Location = return_value_or_none(address.get('cityAndState', {}), 'location2')
                                base_party_address.Level3Location = return_value_or_none(address.get('cityAndState', {}), 'location3')
                                base_party_address.Country_id = return_value_or_none(address.get('countryAndPostCode', {}), 'country')
                                base_party_address.PostCode = return_value_or_none(address.get('countryAndPostCode', {}), 'postCode')

                                country_query_set = Country.objects.filter(CountryId=return_value_or_none(address.get('countryAndPostCode', {}), 'country'))

                                address_final = '{} {} {} {} {} {}'.format(country_query_set.first().Description if country_query_set.exists() else '',
                                                                           return_value_or_none(address.get('cityAndState', {}), 'location1'),
                                                                           return_value_or_none(address.get('cityAndState', {}), 'location2'),
                                                                           return_value_or_none(address.get('cityAndState', {}), 'location3'),
                                                                           address.get('street1', None),
                                                                           address.get('street2', None))

                                base_party_address.AddressFinal = address_final
                                base_party_address.save()

                                existing_addresses.append(base_party_address.BasePartyAddressId)

                            elif 'temp' not in str(address.get('id', '')) and isinstance(address.get('id', None), int) and 'isChange' not in address:
                                existing_addresses.append(address.get('id'))

                        elif address.get('addressType', None) is not None and address.get('addressType', None).isdigit() and int(address.get('addressType', None)) == 2:
                            if 'temp' in str(address.get('id', '')):
                                base_party_email = BasePartyEmail()
                                base_party_email.BasePartyId = base_party
                                base_party_email.EmailFinal = address.get('value', None)
                                base_party_email.EmailType_id = address.get('emailType', None)
                                base_party_email.AddressType_id = address.get('addressType', None)
                                base_party_email.PreferenceType_id = address.get('preferenceType', None)
                                base_party_email.save()

                                existing_emails.append(base_party_email.BasePartyEmailId)

                                if primary_email_id == address.get('id', None):
                                    base_party.PrimaryEmailId = base_party_email
                                    base_party.save()
                            elif 'temp' not in str(address.get('id', '')) and 'isChange' in address and address.get('isChange', False):
                                base_party_email = BasePartyEmail.objects.get(BasePartyEmailId=address.get('id'))
                                base_party_email = BasePartyEmail()
                                base_party_email.BasePartyId = base_party
                                base_party_email.EmailFinal = address.get('value', None)
                                base_party_email.EmailType_id = address.get('emailType', None)
                                base_party_email.AddressType_id = address.get('addressType', None)
                                base_party_email.PreferenceType_id = address.get('preferenceType', None)
                                base_party_email.save()

                                existing_emails.append(base_party_email.BasePartyEmailId)
                            elif 'temp' not in str(address.get('id', '')) and isinstance(address.get('id', None), int) and 'isChange' not in address:
                                existing_emails.append(address.get('id'))

                BasePartyAddress.objects.exclude(BasePartyAddressId__in=[*existing_addresses, base_party.PrimaryContactId_id]).delete()
                BasePartyEmail.objects.exclude(BasePartyEmailId__in=[*existing_emails, base_party.PrimaryEmailId_id]).delete()

        response = BasePartiesSerializer(base_party).data

        return JsonResponse(response)


    def get(self, request, **kwargs):
        base_party_id = kwargs.get('id')
        base_party_query_set = BaseParty.objects.filter(BasePartyId=base_party_id)
        if not base_party_query_set.exists():
            return HttpResponse(content='Base Party with {}id does not exist'.format(base_party_id), status=400)

        base_party = base_party_query_set.first()
        set_recent_item(1, base_party_id, "user")
        response = {
            'data': BasePartySerializer(base_party).data,
            'config': generate_config(base_party_id)
        }

        return JsonResponse(response)

    def delete(self, request, *args, **kwargs):
        base_party_query_set = BaseParty.objects.filter(BasePartyId=kwargs.get('id'))
        if not base_party_query_set.exists():
            return HttpResponse(content='Base Party with {}id does not exist'.format(kwargs.get('id')), status=400)

        base_party_query_set.delete()

        return JsonResponse({'message': 'Success'}, status=200)


