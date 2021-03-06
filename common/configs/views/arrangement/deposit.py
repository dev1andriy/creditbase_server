from django.db.models import Q
from django.utils import timezone

from common.serializers.configs import *
from common.models import BaseParty, RelatedParty, Collateral, CreditApplication, Facility, Deposit, DepositArchived
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

    arrangement_types = []
    arrangement_types_db = ArrangementType.objects.filter(ParentFlag=True, ArrangementCategory_id=1)

    for type in arrangement_types_db:
        type_dict = {"id": type.ArrangementTypeId, "name": type.Description}
        arrangement_children_types = ArrangementType.objects.filter(ArrangementCategory_id=1, ArrangementTypeParent_id=type.ArrangementTypeId)
        if arrangement_children_types.exists():
            type_dict["children"] = []
            for children in arrangement_children_types:
                type_dict["children"].append({"id": children.ArrangementTypeId, "name": children.Description})
        arrangement_types.append(type_dict)

    # TEMP CODE

    base_party_ids = [base_party_id]
    related_parties = RelatedParty.objects.filter((Q(BaseParty1Id=base_party_id) | Q(BaseParty2Id=base_party_id)),
                                                  (Q(EndDate=None) | Q(EndDate__gte=timezone.now())))
    for party in related_parties:
        if party.BaseParty1Id_id not in base_party_ids:
            base_party_ids.append(party.BaseParty1Id_id)
        if party.BaseParty2Id_id not in base_party_ids:
            base_party_ids.append(party.BaseParty2Id_id)
    base_parties = BaseParty.objects.filter(BasePartyId__in=base_party_ids)

    collaterals = []
    for party in base_parties:
        party_dict = {"id": None, "name": party.BasePartyName, "children": []}
        party_has_collaterals = False
        collateral_parents_query_set = Collateral.objects.filter(BasePartyId=party.BasePartyId,
                                                                 CollateralIdParent=None)
        if collateral_parents_query_set.exists():
            party_has_collaterals = True
            for collateral in collateral_parents_query_set:
                collateral_children_query_set = Collateral.objects.filter(BasePartyId=party.BasePartyId,
                                                                          CollateralIdParent=collateral.CollateralId)
                if collateral_children_query_set.exists():
                    collateral_dict = {"id": collateral.CollateralId, 'name': collateral.Description1.get('HostValue', None) if collateral.Description1 is not None else None, 'children': []}
                    for collateral_child in collateral_children_query_set:
                        collateral_dict['children'].append({'id': collateral_child.CollateralId, 'name': collateral_child.Description1.get('HostValue', None) if collateral_child.Description1 is not None else None})
                    party_dict['children'].append(collateral_dict)

                else:
                    party_dict['children'].append({"id": collateral.CollateralId, 'name': collateral.Description1.get('HostValue', None) if collateral.Description1 is not None else None})
        if party_has_collaterals:
            collaterals.append(party_dict)

    # TEMP CODE

    credit_applications = [
        {'id': None, 'title': 'Active applications', 'clickable': False, 'children': []},
        {'id': None, 'title': 'Archived applications', 'clickable': False, 'children': []},
    ]

    credit_applications_from_db = CreditApplication.objects.filter(BasePartyId_id__in=base_party_ids)

    for credit_application in credit_applications_from_db:
        archived_deposits = DepositArchived.objects.filter(CreditApplicationId_id=credit_application.CreditApplicationId)
        if archived_deposits.exists():
            credit_application_dict = {'id': credit_application.CreditApplicationId, 'title': 'App {} ({})'.format(credit_application.CreditApplicationId, credit_application.ApplicationStatus.Description if credit_application.ApplicationStatus is not None else None), 'children': [], 'clickable': True, 'view': False}
            for deposit in archived_deposits:
                credit_application_dict['children'].append({'id': deposit.DepositId, 'title': 'v{} - {}'.format(deposit.ArchiveVersion, deposit.ArchiveStatus.Description if deposit.ArchiveStatus is not None else None), 'clickable': True, 'view': True})

            credit_applications[1]['children'].append(credit_application_dict)
        else:
            credit_applications[0]['children'].append({'id': credit_application.CreditApplicationId, 'title': 'App {} ({})'.format(credit_application.CreditApplicationId, credit_application.ApplicationStatus.Description if credit_application.ApplicationStatus is not None else None), 'clickable': True, 'view': False})

    # TEMP CODE

    config = {
        "creditApplications": credit_applications,
        "currencies": CurrencyListSerializer(Currency.objects.filter(), many=True).data,
        "details": {
            "fields": [
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
                    "type": "tree",
                    "label": "Deposit Type",
                    "name": "arrangementType",
                    "order": 2,
                    'options': arrangement_types
                },
                {
                    "type": "readOnly",
                    "label": "Deposit ID",
                    "name": "depositId",
                    "order": 3
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "Host Deposit ID",
                    "name": "hostDepositId",
                    "order": 4
                },
            ]
        }
    }

    return config
