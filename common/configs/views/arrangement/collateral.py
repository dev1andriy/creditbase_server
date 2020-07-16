from django.db.models import Q
from django.utils import timezone

from common.serializers import CreditApplicationsSerializer
from common.serializers.configs import *
from common.models import BaseParty, RelatedParty, Collateral, CreditApplication, Facility, CollateralArchived
from common.models.general import *


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

    facilities = []
    for party in base_parties:
        party_dict = {"id": None, "name": party.BasePartyName, "children": []}
        party_has_facilities = False
        facility_parents_query_set = Facility.objects.filter(BasePartyId=party.BasePartyId,
                                                             FacilityIdParent=None)
        if facility_parents_query_set.exists():
            party_has_facilities = True
            for facility in facility_parents_query_set:
                facility_children_query_set = Facility.objects.filter(BasePartyId=party.BasePartyId,
                                                                      FacilityIdParent=facility.FacilityId)
                if facility_children_query_set.exists():
                    facility_dict = {"id": facility.FacilityId, 'name': facility.Description1.get('HostValue', None) if facility.Description1 is not None else None, 'children': []}
                    for facility_child in facility_children_query_set:
                        facility_dict['children'].append({'id': facility_child.FacilityId, 'name': facility_child.Description1.get('HostValue', None) if facility_child.Description1 is not None else None})
                    party_dict['children'].append(facility_dict)

                else:
                    party_dict['children'].append({"id": facility.FacilityId, 'name': facility.Description1.get('HostValue', None) if facility.Description1 is not None else None})
        if party_has_facilities:
            facilities.append(party_dict)


    # TEMP CODE

    credit_applications = [
        {'id': None, 'title': 'Active applications', 'clickable': False, 'children': []},
        {'id': None, 'title': 'Archived applications', 'clickable': False, 'children': []},
    ]

    credit_applications_from_db = CreditApplication.objects.filter(BasePartyId_id__in=base_party_ids)

    for credit_application in credit_applications_from_db:
        archived_collaterals = CollateralArchived.objects.filter(CreditApplicationId_id=credit_application.CreditApplicationId)
        if archived_collaterals.exists():
            credit_application_dict = {'id': credit_application.CreditApplicationId, 'title': 'App {} ({})'.format(credit_application.CreditApplicationId, credit_application.ApplicationStatus.Description if credit_application.ApplicationStatus is not None else None), 'children': [], 'clickable': True, 'view': False}
            for collateral in archived_collaterals:
                credit_application_dict['children'].append({'id': collateral.CollateralId, 'title': 'v{} - {}'.format(collateral.ArchiveVersion, collateral.ArchiveStatus.Description if collateral.ArchiveStatus is not None else None), 'clickable': True, 'view': True})

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
                    "label": "Collateral Type",
                    "name": "arrangementType",
                    "order": 2,
                    'options': arrangement_types
                },
                {
                    "type": "select",
                    "label": "Parent Collateral",
                    "name": "parentCollateral",
                    "options": CollateralConfigSerializer(Collateral.objects.filter(ArrangementType__ParentFlag=True,
                                                                              BasePartyId_id__in=base_party_ids_linked_banking_info), many=True).data,
                    "order": 3
                },
                {
                    "type": "readOnly",
                    "label": "Collateral ID",
                    "name": "collateralId",
                    "order": 4
                },
                {
                    "type": "input",
                    "inputType": "text",
                    "label": "Host Collateral ID",
                    "name": "hostCollateralId",
                    "order": 5
                },
            ],
            "grid": [
                {
                    'required': True,
                    "name": "requestType",
                    "parameterCategory": "General parameters",
                    'parameterName': {
                        'value': 'Request Type',
                        'color': '#707070'
                    },
                    "hostValue": None,
                    "modify": {
                        "statesAmount": 2,
                        "rewritable": False,
                        "data": 1
                    },
                    "proposedValue": {
                        "config": {
                            "type": "select",
                            "options": RequestTypeSerializer(RequestType.objects.all(), many=True).data
                        },
                        "data": None
                    },
                    "print": {
                        "statesAmount": 3,
                        "rewritable": True,
                        "data": 2
                    }
                }
            ] if edit is None or edit is False else None
        },
        'coverage': {
            'collateralLinkages': [
                {
                    "type": "readOnly",
                    "label": "Collateral Description",
                    "name": "collateralDescription",
                    "order": 1
                },
                {
                    "type": "tree",
                    "label": "Facility",
                    "name": "facilityId",
                    "options": facilities,
                    "order": 2
                },
                {
                    "type": "readOnly",
                    "label": "Host Facility Id",
                    "name": "hostFacilityId",
                    "order": 3
                },
                {
                    "type": "readOnly",
                    "label": "Facility Owner",
                    "name": "facilityOwner",
                    "order": 4
                },
                {
                    "type": "readOnly",
                    "label": "Facility Description",
                    "name": "facilityDescription",
                    "order": 5
                },
                {
                    "type": "readOnly",
                    "label": "Currency",
                    "name": "currency",
                    "order": 6
                },
                {
                    "type": "readOnly",
                    "label": "Tenor",
                    "name": "tenor",
                    "order": 7
                },
                {
                    "type": "readOnly",
                    "label": "Frequency",
                    "name": "frequency",
                    "order": 8
                },
                {
                    "type": "readOnly",
                    "label": "Facility Limit",
                    "name": "facilityLimit",
                    "order": 9
                },
                {
                    "type": "readOnly",
                    "label": "Outstanding Balance",
                    "name": "outstandingBalance",
                    "order": 10
                },
                {
                    "type": "readOnly",
                    "label": "Proposed Limit",
                    "name": "proposedLimit",
                    "order": 11
                },
                {
                    "type": "readOnly",
                    "label": "Total Exposure",
                    "name": "totalExposure",
                    "order": 12
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Assignment",
                    "name": "assignment",
                    "order": 13
                },
                {
                    "type": "input",
                    "inputType": "number",
                    "label": "Lien Order",
                    "name": "lienOrder",
                    "order": 14
                }
            ]
        }
    }

    return config
