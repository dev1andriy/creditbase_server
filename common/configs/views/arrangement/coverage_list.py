from django.db.models import Q
from django.utils import timezone

from common.serializers.configs import *
from common.models import BaseParty, RelatedParty, Collateral, CreditApplication, Coverage, CoverageArchived
from common.models.general import *
from common.serializers import CreditApplicationsListSerializer


def generate_config(edit=None, base_party_id=None):
    # TEMP CODE
    base_party = BaseParty.objects.filter(BasePartyId=base_party_id).first()
    base_party_ids = [base_party_id]
    base_party_ids_linked_banking_info = [base_party_id]

    related_parties = RelatedParty.objects.filter((Q(BaseParty1Id=base_party) | Q(BaseParty2Id=base_party)),
                                                  (Q(EndDate=None) | Q(EndDate__gte=timezone.now())))
    for party in related_parties:
        if party.BaseParty1Id not in base_party_ids:
            base_party_ids.append(party.BaseParty1Id)
        if party.BaseParty2Id not in base_party_ids:
            base_party_ids.append(party.BaseParty2Id)

    related_parties_linked_banking_info = related_parties.filter(LinkBankingInfo=True)

    for party in related_parties_linked_banking_info:
        if party.BaseParty1Id not in base_party_ids_linked_banking_info:
            base_party_ids_linked_banking_info.append(party.BaseParty1Id)
        if party.BaseParty2Id not in base_party_ids_linked_banking_info:
            base_party_ids_linked_banking_info.append(party.BaseParty2Id)


    base_party_ids = [base_party_id]
    related_parties = RelatedParty.objects.filter((Q(BaseParty1Id=base_party_id) | Q(BaseParty2Id=base_party_id)),
                                                  (Q(EndDate=None) | Q(EndDate__gte=timezone.now())))
    for party in related_parties:
        if party.BaseParty1Id_id not in base_party_ids:
            base_party_ids.append(party.BaseParty1Id_id)
        if party.BaseParty2Id_id not in base_party_ids:
            base_party_ids.append(party.BaseParty2Id_id)

    # TEMP CODE

    credit_applications = [
        {'id': None, 'title': 'Active applications', 'clickable': False, 'children': []},
        {'id': None, 'title': 'Archived applications', 'clickable': False, 'children': []},
    ]

    credit_applications_from_db = CreditApplication.objects.filter(BasePartyId_id__in=base_party_ids)

    for credit_application in credit_applications_from_db:
        archived_coverages = CoverageArchived.objects.filter(CreditApplicationId_id=credit_application.CreditApplicationId)
        if archived_coverages.exists():
            credit_application_dict = {'id': credit_application.CreditApplicationId, 'title': 'App {} ({})'.format(credit_application.CreditApplicationId, credit_application.ApplicationStatus.Description if credit_application.ApplicationStatus is not None else None), 'children': [], 'clickable': True, 'view': False}
            for coverage in archived_coverages:
                credit_application_dict['children'].append({'id': coverage.CoverageId, 'title': 'v{} - {}'.format(coverage.ArchiveVersion, coverage.ArchiveStatus.Description if coverage.ArchiveStatus is not None else None), 'clickable': True, 'view': True})

            credit_applications[1]['children'].append(credit_application_dict)
        else:
            credit_applications[0]['children'].append({'id': credit_application.CreditApplicationId, 'title': 'App {} ({})'.format(credit_application.CreditApplicationId, credit_application.ApplicationStatus.Description if credit_application.ApplicationStatus is not None else None), 'clickable': True, 'view': False})

    # TEMP CODE

    config = {
        "creditApplications": credit_applications,
        "currencies": CurrencyListSerializer(Currency.objects.filter(), many=True).data,
    }

    return config
