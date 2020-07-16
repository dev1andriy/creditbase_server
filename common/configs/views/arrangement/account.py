from common.serializers.configs import *
from common.models import BaseParty
from common.models.general import *

from common.configs.views.arrangement.account_related_party import generate_config as generate_account_related_party_config


def generate_config(edit=None, edit_host_values=None, base_party_id=None, account_id=None):

    business_unit_options = {}
    financial_institutions = FinancialInstitution.objects.all()
    for institution in financial_institutions:
        business_unit_options[str(institution.FinancialInstitutionId)] = BusinessUnitSerializer(BusinessUnit.objects.filter(FinancialInstitution=institution.FinancialInstitutionId), many=True).data

    account_type_options = {}
    account_categories = AccountCategory.objects.all()
    for category in account_categories:
        account_type_options[str(category.AccountCategoryId)] = AccountTypeSerializer(AccountType.objects.filter(AccountCategory=category.AccountCategoryId), many=True).data

    config = {
        "details": {
            "accountHighlights": [
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Account Owner",
                    "name": "accountOwner",
                    "options": [{
                        **BasePartyConfigSerializer(BaseParty.objects.get(BasePartyId=base_party_id)).data,
                        "autoSelect": True
                    }],
                    "order": 1,
                    "isRequired": True,
                }
                if base_party_id is not None else
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Account Owner",
                    "name": "accountOwner",
                    "options": BasePartyConfigSerializer(BaseParty.objects.all(), many=True).data,
                    "order": 1,
                    "isRequired": True
                },
                {
                    "type": "input" if edit_host_values or edit_host_values is None else 'readOnly',
                    "inputType": "text" if edit_host_values or edit_host_values is None else None,
                    "fullWide": True,
                    "label": "Account Title",
                    "name": "accountTitle",
                    "order": 2,
                    "isRequired": True,
                },
                {
                    "type": "readOnly",
                    "label": "Account ID",
                    "name": "accountId",
                    "order": 3
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Account Category",
                    "name": "accountCategory",
                    "options": AccountCategorySerializer(AccountCategory.objects.all(), many=True).data,
                    "placeholder": 'Select a category',
                    "order": 4,
                    "isRequired": True,
                },
                {
                    "type": "input" if edit_host_values or edit_host_values is None else 'readOnly',
                    "inputType": "text" if edit_host_values or edit_host_values is None else None,
                    "label": "Host Account ID",
                    "name": "hostAccountId",
                    "order": 5,
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Account Type",
                    "name": "accountType",
                    "optionsRelatedBy": "accountCategory",
                    "relatedOptions": account_type_options,
                    "placeholder": 'Select a type',
                    "order": 6,
                    "isRequired": True,
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Account Class",
                    "name": "accountClass",
                    "options": AccountClassSerializer(AccountClass.objects.all(), many=True).data,
                    "placeholder": 'Select a class',
                    "order": 7,
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Financial Institution",
                    "name": "financialInstitution",
                    "options": FinancialInstitutionSerializer(FinancialInstitution.objects.all(), many=True).data,
                    "placeholder": 'Select an institution',
                    "order": 8,
                    "isRequired": True,
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Currency",
                    "name": "currency",
                    "options": CurrencyConfigSerializer(Currency.objects.all(), many=True).data,
                    "placeholder": 'Select a currency',
                    "order": 9,
                    "isRequired": True,
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Business Unit",
                    "name": "businessUnit",
                    "optionsRelatedBy": "financialInstitution",
                    "relatedOptions": business_unit_options,
                    "placeholder": 'Select an unit',
                    "order": 10,
                    "isRequired": True,
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Account Status",
                    "name": "accountStatus",
                    "options": AccountStatusSerializer(AccountStatus.objects.all(), many=True).data,
                    "placeholder": 'Select a status',
                    "order": 11,
                    "isRequired": True,
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Account Officer",
                    "name": "accountOfficer",
                    "options": AccountOfficerSerializer(AccountOfficer.objects.all(), many=True).data,
                    "placeholder": 'Select an officer',
                    "order": 12,
                    "isRequired": True,
                },
                {
                    "type": "input" if edit_host_values or edit_host_values is None else 'readOnly',
                    "inputType": "date" if edit_host_values or edit_host_values is None else None,
                    "dataType": None if edit_host_values or edit_host_values is None else 'date',
                    "label": "Open Date",
                    "name": "openDate",
                    "order": 13,
                    "isRequired": True,
                },
                {
                    "type": "input" if edit_host_values or edit_host_values is None else 'readOnly',
                    "inputType": "date" if edit_host_values or edit_host_values is None else None,
                    "dataType": None if edit_host_values or edit_host_values is None else 'date',
                    "label": "Last Txn Date",
                    "name": "lastTxnDate",
                    "order": 14
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Joint account?",
                    "name": "jointAccount",
                    "options": FlagSerializer(Flag.objects.all(), many=True).data,
                    "placeholder": 'Select a flag',
                    "order": 15
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Overdraft allowed?",
                    "name": "overdraftAllowed",
                    "options": FlagSerializer(Flag.objects.all(), many=True).data,
                    "placeholder": 'Select a flag',
                    "order": 16
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Liquidation account?",
                    "name": "liquidationAccount",
                    "options": FlagSerializer(Flag.objects.all(), many=True).data,
                    "placeholder": 'Select a flag',
                    "order": 17
                },
                {
                    "type": "input" if edit_host_values or edit_host_values is None else 'readOnly',
                    "inputType": "text" if edit_host_values or edit_host_values is None else None,
                    "label": "Limit ID",
                    "name": "limitId",
                    "order": 18
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Lien marked?",
                    "name": "lienMarked",
                    "options": FlagSerializer(Flag.objects.all(), many=True).data,
                    "placeholder": 'Select a flag',
                    "order": 19
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Limit Currency",
                    "name": "limitCurrency",
                    "options": CurrencyConfigSerializer(Currency.objects.all(), many=True).data,
                    "placeholder": 'Select a currency',
                    "order": 20
                },
                {
                    "type": "select" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Collateralizable?",
                    "name": "collateralizable",
                    "options": FlagSerializer(Flag.objects.all(), many=True).data,
                    "placeholder": 'Select a flag',
                    "order": 21
                },
                {
                    "type": "input" if edit_host_values or edit_host_values is None else 'readOnly',
                    "inputType": "number" if edit_host_values or edit_host_values is None else None,
                    "label": "Limit amount",
                    "name": "limitAmount",
                    "order": 22
                },
                {
                    "type": "multiselect" if edit_host_values or edit_host_values is None else 'readOnly',
                    "label": "Posting restrictions",
                    "name": "postingRestrictionType",
                    "options": PostingRestrictionTypeSerializer(PostingRestrictionType.objects.all(), many=True).data,
                    "placeholder": 'Select a type',
                    "order": 23,
                },
                {
                    "type": "checkbox",
                    "label": "Edit Host Values",
                    "name": "editHostValues",
                    "order": 24
                },
                {
                    "type": "checkbox",
                    "label": "Print",
                    "name": "print",
                    "order": 25
                },
                {
                    "type": "readOnly",
                    "label": "Order",
                    "name": "order",
                    "order": 26
                },

            ],
            "relatedParties": generate_account_related_party_config(None, None, base_party_id, account_id),
            "balanceInformation": [
                {
                    "type": "input" if edit_host_values or edit_host_values is None else 'readOnly',
                    "inputType": "number" if edit_host_values or edit_host_values is None else None,
                    "color": True,
                    "colorType": "balanceInformation",
                    "fullWide": True,
                    "label": "Book Balance",
                    "name": "bookBalance",
                    "order": 1
                },
                {
                    "type": "input" if edit_host_values or edit_host_values is None else 'readOnly',
                    "inputType": "number" if edit_host_values or edit_host_values is None else None,
                    "color": True,
                    "colorType": "balanceInformation",
                    "fullWide": True,
                    "label": "Available Balance",
                    "name": "availableBalance",
                    "order": 2
                },
                {
                    "type": "input" if edit_host_values or edit_host_values is None else 'readOnly',
                    "inputType": "date" if edit_host_values or edit_host_values is None else None,
                    "dataType": None if edit_host_values or edit_host_values is None else 'date',
                    "fullWide": True,
                    "label": "Balance Date",
                    "name": "balanceDate",
                    "order": 3
                },
            ]
        }
    }

    return config
