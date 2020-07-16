from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from rest_framework.views import APIView
from django.utils import timezone
from common.models.related_party import RelatedParty
from django.db.models import Q
from common.models.base_party import BaseParty
from common.models.arrangement import Account, AccountRelatedParty
from common.configs.views.arrangement.account import generate_config
from common.serializers import AccountsSerializer, ReadOnlyAccountSerializer, EditAccountSerializer

account_details_application_highlights_fields = [
    {"db_field": 'AccountTitle', "field_label": 'accountTitle'},
    {"db_field": 'BasePartyId_id', "field_label": 'accountOwner'},
    {"db_field": 'AccountCategory_id', "field_label": 'accountCategory'},
    {"db_field": 'AccountIdHost', "field_label": 'hostAccountId'},
    {"db_field": 'AccountType_id', "field_label": 'accountType'},
    {"db_field": 'EditHostValuesFlag', "field_label": 'editHostValues'},
    {"db_field": 'AccountClass_id', "field_label": 'accountClass'},
    {"db_field": 'FinancialInstitution_id', "field_label": 'financialInstitution'},
    {"db_field": 'Currency_id', "field_label": 'currency'},
    {"db_field": 'BusinessUnit_id', "field_label": 'businessUnit'},
    {"db_field": 'AccountStatus_id', "field_label": 'accountStatus'},
    {"db_field": 'OriginationDate', "field_label": 'openDate'},
    {"db_field": 'LastTransactionDate', "field_label": 'lastTxnDate'},
    {"db_field": 'JointAccountFlag_id', "field_label": 'jointAccount'},
    {"db_field": 'AccountOfficer_id', "field_label": 'accountOfficer'},
    {"db_field": 'OverdraftAllowedFlag_id', "field_label": 'overdraftAllowed'},
    {"db_field": 'LimitId', "field_label": 'limitId'},
    {"db_field": 'LienMarkedFlag_id', "field_label": 'lienMarked'},
    {"db_field": 'LimitCurrency_id', "field_label": 'limitCurrency'},
    {"db_field": 'CollateralizableFlag_id', "field_label": 'collateralizable'},
    {"db_field": 'LiquidationAccountFlag_id', "field_label": 'liquidationAccount'},
    {"db_field": 'LimitAmount', "field_label": 'limitAmount'},
    {"db_field": 'PostingRestrictionType', "field_label": 'postingRestrictionType'},
    {"db_field": 'PrintFlag', "field_label": 'print'},
]

account_details_balance_information = [
    {"db_field": 'BalanceBook', "field_label": 'bookBalance'},
    {"db_field": 'BalanceAvailable', "field_label": 'availableBalance'},
    {"db_field": 'BalanceDate', "field_label": 'balanceDate'},
]

account_details_related_parties = [
    {"db_field": "RelatedPartyId_id", "field_label": "relatedParty", "read_write_always": False},
    {"db_field": "RelationCategory_id", "field_label": "relationCategory", "read_write_always": False},
    {"db_field": "RelationType_id", "field_label": "relationType", "read_write_always": False},
    {"db_field": "IsPrimaryAccountOwner_id", "field_label": "isPrimaryAccountOwner", "read_write_always": False},
    {"db_field": "Comment", "field_label": "comment", "read_write_always": True},
    {"db_field": "StartDate", "field_label": "startDate", "read_write_always": False},
    {"db_field": "EndDate", "field_label": "endDate", "read_write_always": True},
    {"db_field": "EditHostValuesFlag", "field_label": "editHostValues", "read_write_always": True},
    {"db_field": "PrintFlag", "field_label": "print", "read_write_always": True},
    # {"db_field": "OrderingRank", "field_label": "relatedParty"},
]


class AccountsAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        if 'id' in kwargs.keys():
            base_party = BaseParty.objects.filter(BasePartyId=kwargs['id']).first()
            base_party_ids = [kwargs['id']]
            related_parties = RelatedParty.objects.filter((Q(BaseParty1Id=base_party) | Q(BaseParty2Id=base_party)), (Q(EndDate=None) | Q(EndDate__gte=timezone.now())))
            for party in related_parties:
                if party.BaseParty1Id not in base_party_ids:
                    base_party_ids.append(party.BaseParty1Id)
                if party.BaseParty2Id not in base_party_ids:
                    base_party_ids.append(party.BaseParty2Id)
            main_account = Account.objects.filter(BasePartyId_id=kwargs['id']).order_by('OrderingRank')
            related_accounts = Account.objects.filter(BasePartyId_id__in=base_party_ids).exclude(BasePartyId_id=kwargs['id']).order_by('OrderingRank')

            response_data = AccountsSerializer(main_account, many=True).data + AccountsSerializer(related_accounts, many=True).data
        else:
            base_party = None
            accounts = Account.objects.all()
            response_data = AccountsSerializer(accounts, many=True).data

        base_party_id = base_party.BasePartyId if base_party is not None else None

        response = {
            "data": response_data,
            "config": generate_config(False, None, base_party_id, None)
        }

        return JsonResponse(response)


class AccountAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if request.data is None:
            raise Exception("Wrong input data")

        if request.data['details'] is not None:
            details = request.data['details']
            account = Account()

            if 'accountHighlights' in details and details['accountHighlights'] is not None:
                account_highlights = details['accountHighlights']

                for field in account_details_application_highlights_fields:
                    if "_id" in field['db_field'] and field['field_label'] in account_highlights and account_highlights[field['field_label']] is not None:
                        setattr(account, field['db_field'], int(account_highlights[field['field_label']]))
                    elif "_id" not in field['db_field'] and field['field_label'] in account_highlights and account_highlights[field['field_label']] is not None:
                        setattr(account, field['db_field'], account_highlights[field['field_label']])

                account.save()

            if 'relatedParties' in details and details['relatedParties'] is not None:
                related_parties = details['relatedParties']

                for related_party in related_parties:
                    account_related_party = AccountRelatedParty()
                    account_related_party.AccountId = account

                    if 'relatedParty' not in related_party or related_party['relatedParty'] is None:
                        account_related_party.RelatedPartyName = related_party['relatedPartyName']
                    elif 'relatedParty' in related_party and related_party['relatedParty'] is not None:
                        account_related_party.RelatedPartyName = BaseParty.objects.get(BasePartyId=related_party['relatedParty']).BasePartyName

                    for field in account_details_related_parties:
                        if "_id" in field['db_field'] and field['field_label'] in related_party and related_party[field['field_label']] is not None:
                            setattr(account_related_party, field['db_field'], int(related_party[field['field_label']]))
                        elif "_id" not in field['db_field'] and field['field_label'] in related_party and related_party[field['field_label']] is not None:
                            setattr(account_related_party, field['db_field'], related_party[field['field_label']])

                    account_related_party.save()

            if 'balanceInformation' in details and details['balanceInformation'] is not None:
                balance_information = details['balanceInformation']

                for field in account_details_balance_information:
                    if field['field_label'] in balance_information and balance_information[field['field_label']] is not None:
                        setattr(account, field['db_field'], balance_information[field['field_label']])

            account.save()

            return JsonResponse(AccountsSerializer(account).data)

    def put(self, request, *args, **kwargs):
            if request.data is None:
                raise Exception("Wrong input data")

            if request.data['details'] is not None:
                details = request.data['details']
                account_query_set = Account.objects.filter(AccountId=request.data['accountId'])
                if not account_query_set.exists():
                    raise Exception('Account is not found')

                account = account_query_set.first()
                edit_host_values = account.EditHostValuesFlag

                if 'accountHighlights' in details and details['accountHighlights'] is not None:
                    account_highlights = details['accountHighlights']

                    if edit_host_values:
                        for field in account_details_application_highlights_fields:
                            if "_id" in field['db_field'] and field['field_label'] in account_highlights and account_highlights[field['field_label']] is not None:
                                setattr(account, field['db_field'], int(account_highlights[field['field_label']]))
                            elif "_id" not in field['db_field'] and field['field_label'] in account_highlights and account_highlights[field['field_label']] is not None:
                                setattr(account, field['db_field'], account_highlights[field['field_label']])

                    if "editHostValues" in account_highlights and account_highlights["editHostValues"] is not None:
                        account.EditHostValuesFlag = account_highlights["editHostValues"]

                if 'relatedParties' in details and details['relatedParties'] is not None and isinstance(details['relatedParties'], list):
                    related_parties = details['relatedParties']

                    existing_related_parties = []

                    for related_party in related_parties:
                        if 'temp' in str(related_party['id']):
                            account_related_party = AccountRelatedParty()
                            account_related_party.AccountId = account

                            if 'relatedParty' not in related_party or related_party['relatedParty'] is None:
                                account_related_party.RelatedPartyName = related_party['relatedPartyName']
                            elif 'relatedParty' in related_party and related_party['relatedParty'] is not None:
                                account_related_party.RelatedPartyName = BaseParty.objects.get(BasePartyId=related_party['relatedParty']).BasePartyName

                            for field in account_details_related_parties:
                                if "_id" in field['db_field'] and field['field_label'] in related_party and related_party[field['field_label']] is not None:
                                    setattr(account_related_party, field['db_field'], int(related_party[field['field_label']]))
                                elif "_id" not in field['db_field'] and field['field_label'] in related_party and related_party[field['field_label']] is not None:
                                    setattr(account_related_party, field['db_field'], related_party[field['field_label']])

                            account_related_party.save()
                            existing_related_parties.append(account_related_party.AccountRelatedPartyId)

                        elif 'temp' not in str(related_party['id']) and 'isChange' in related_party and related_party['isChange']:
                            account_related_party_query_set = AccountRelatedParty.objects.filter(AccountRelatedPartyId=related_party['id'])
                            if account_related_party_query_set.exists():
                                account_related_party = account_related_party_query_set.first()
                                edit_host_values = account.EditHostValuesFlag

                                if edit_host_values:
                                    if 'relatedParty' not in related_party or related_party['relatedParty'] is None:
                                        account_related_party.RelatedPartyName = related_party['relatedPartyName']
                                    elif 'relatedParty' in related_party and related_party['relatedParty'] is not None and isinstance(related_party['relatedParty'], int):
                                        account_related_party.RelatedPartyName = BaseParty.objects.get(BasePartyId=related_party['relatedParty']).BasePartyName

                                for field in account_details_related_parties:
                                    if "_id" in field['db_field'] and field['field_label'] in related_party and related_party[field['field_label']] is not None:
                                        if edit_host_values or not edit_host_values and field['read_write_always']:
                                            setattr(account_related_party, field['db_field'], int(related_party[field['field_label']]))
                                    elif "_id" not in field['db_field'] and field['field_label'] in related_party and related_party[field['field_label']] is not None:
                                        if edit_host_values or not edit_host_values and field['read_write_always']:
                                            setattr(account_related_party, field['db_field'], related_party[field['field_label']])

                                account_related_party.save()
                                existing_related_parties.append(account_related_party.AccountRelatedPartyId)

                        elif 'temp' not in str(related_party['id']) and isinstance(related_party['id'], int) and 'isChange' not in related_party:
                            existing_related_parties.append(related_party['id'])

                    AccountRelatedParty.objects.filter(AccountId=account.AccountId).exclude(AccountRelatedPartyId__in=existing_related_parties).delete()

                if 'balanceInformation' in details and details['balanceInformation'] is not None:
                    balance_information = details['balanceInformation']

                    if edit_host_values:
                        for field in account_details_balance_information:
                            if field['field_label'] in balance_information and balance_information[field['field_label']] is not None:
                                setattr(account, field['db_field'], balance_information[field['field_label']])

                account.save()

                return JsonResponse(AccountsSerializer(account).data)

    def get(self, request, **kwargs):
        account_id = kwargs['id']
        try:
            account = Account.objects.get(AccountId=account_id)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('Account with {}id doesn\'t exist'.format(account_id))

        edit_host_values = account.EditHostValuesFlag

        response = EditAccountSerializer(account).data if edit_host_values else ReadOnlyAccountSerializer(account).data

        response = {
            "data": response,
            "config": generate_config(True, account.EditHostValuesFlag, account.BasePartyId_id, account.AccountId)
        }

        return JsonResponse(response)

    def delete(self, request, *args, **kwargs):
        account_query_set = Account.objects.filter(AccountId=kwargs['id'])
        if not account_query_set.exists():
            return HttpResponseNotFound(content='Account with {}id does not exist'.format(kwargs['id']))

        account_query_set.delete()

        return HttpResponse(status=200)

        # return HttpResponse("Account is linked with Facility {}".format(1), status=400)

