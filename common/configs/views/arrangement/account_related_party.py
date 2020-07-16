from common.serializers.configs import *
from common.models import BaseParty, AccountRelatedParty
from common.models.general import *


def generate_config(edit=None, edit_host_values=None, base_party_id=None, account_id=None, account_related_party_id=None):

    relation_type_options = {}
    relation_categories = RelationCategory.objects.all()
    for category in relation_categories:
        relation_type_options[str(category.RelationCategoryId)] = RelationTypeSerializer(RelationType.objects.filter(RelationCategory_id=category.RelationCategoryId), many=True).data

    config = {
        "details": [
            {
                "type": "input" if edit_host_values or edit_host_values is None else 'readOnly',
                "inputType": "text" if edit_host_values or edit_host_values is None else None,
                "label": "Related Party Name",
                "name": "relatedPartyName",
                "requiredField": "relatedParty",
                "requiredValue": None,
                "order": 1,
                "isRequired": True
            },
            {
                "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                "label": "Related Party",
                "name": "relatedParty",
                "options": BasePartyConfigSerializer(BaseParty.objects.all(), many=True).data,
                "placeholder": 'Select a related party',
                "order": 2,
            },
            {
                "type": "readOnly",
                "label": "Account ID",
                "name": "accountId",
                "order": 3,
                "value": account_id
            },
            {
                "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                "label": "Relation Category",
                "name": "relationCategory",
                "options": RelationCategorySerializer(relation_categories, many=True).data,
                "placeholder": 'Select a related category',
                "order": 4,
                "isRequired": True
            },
            {
                "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                "label": "Relation Type",
                "name": "relationType",
                "optionsRelatedBy": "relationCategory",
                "relatedOptions": relation_type_options,
                "placeholder": 'Select a related type',
                "order": 5,
                "isRequired": True
            },
            {
                "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                "label": "Primary A/C Owner?",
                "name": "isPrimaryAccountOwner",
                "options": FlagSerializer(Flag.objects.all(), many=True).data,
                "placeholder": 'Select a flag',
                "order": 6
            } if not AccountRelatedParty.objects.filter(AccountId_id=account_id, IsPrimaryAccountOwner_id=1).exists() or AccountRelatedParty.objects.filter(AccountId_id=account_id, AccountRelatedPartyId=account_related_party_id, IsPrimaryAccountOwner_id=1).exists()  else None,
            {
                "type": "input",
                "inputType": "text",
                "label": "Comment",
                "name": "comment",
                "order": 7,
            },
            {
                "type": "input" if edit_host_values or edit_host_values is None else 'readOnly',
                "inputType": "date" if edit_host_values or edit_host_values is None else None,
                "dataType": None if edit_host_values or edit_host_values is None else 'date',
                "label": "Start Date",
                "name": "startDate",
                "order": 8,
                "isRequired": True
            },
            {
                "type": "input",
                "inputType": "date",
                "label": "End Date",
                "name": "endDate",
                "order": 9
            },
            {
                "type": "select",
                "label": "Edit Host values",
                "name": "editHostValues",
                "options": FlagSerializer(Flag.objects.all(), many=True).data,
                "placeholder": 'Select a flag',
                "order": 10
            },
            {
                "type": "readOnly",
                "label": "Order",
                "name": "order",
                "order": 11
            },
            {
                "type": "checkbox",
                "label": "Print",
                "name": "print",
                "order": 12
            },
        ],
        "audit": []
    }

    return config
