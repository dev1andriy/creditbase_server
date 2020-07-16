from django.db.models import Q
from django.utils import timezone

from common.models import BaseParty, RelatedParty, Facility


def generate_config(edit=None, base_party_id=None, collateral_id=None, collateral_description=None):

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

    config = {
        'collateralId': collateral_id,
        "coverage": [
            {
                "type": "readOnly",
                "label": "Collateral Description",
                "name": "collateralDescription",
                "order": 1,
                'value': collateral_description
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

    return config
