from django.db.models import Q
from django.utils import timezone

from common.serializers.configs import *
from common.models import BaseParty, RelatedParty, Collateral, CreditApplication, Facility
from common.models.general import *
from common.serializers import CreditApplicationsListSerializer


def generate_config(edit=None, base_party_id=None, facility_id=None, facility_description=None):

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
    print(base_parties)

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

    config = {
        'facilityId': facility_id,
        'coverage': [
            {
                "type": "readOnly",
                "label": "Facility Description",
                "name": "facilityDescription",
                "order": 1,
                'value': facility_description
            },
            {
                "type": "tree",
                "label": "Collateral",
                "name": "collateralId",
                "options": collaterals,
                "order": 2
            },
            {
                "type": "readOnly",
                "label": "Collateral Owner",
                "name": "collateralOwner",
                "order": 3
            },
            {
                "type": "readOnly",
                "label": "Collateral Description",
                "name": "collateralDescription",
                "order": 4
            },
            {
                "type": "readOnly",
                "label": "Currency",
                "name": "currency",
                "order": 5
            },
            {
                "type": "readOnly",
                "label": "Open Market Value",
                "name": "openMarketValue",
                "order": 6
            },
            # {
            #     "type": "readOnly",
            #     "label": "Discount Factor",
            #     "name": "discountFactor",
            #     "order": 7
            # },
            {
                "type": "readOnly",
                "label": "Discounted Value",
                "name": "discountedValue",
                "order": 7
            },
            {
                "type": "readOnly",
                "label": "Forced Sale Value",
                "name": "forcedSaleValue",
                "order": 8
            },
            # {
            #     "type": "readOnly",
            #     "label": "Prior Liens",
            #     "name": "priorLiens",
            #     "order": 10
            # },
            {
                "type": "input",
                "inputType": "number",
                "label": "Assignment",
                "name": "assignment",
                "order": 9
            },
            {
                "type": "input",
                "inputType": "number",
                "label": "Lien Order",
                "name": "lienOrder",
                "order": 10
            }
        ]
    }

    return config
