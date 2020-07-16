from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseNotFound
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import ensure_csrf_cookie
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
# from main.common.camel_case_parser import CamelCaseParser
# from common.configs.views.credit_application import *
# from common.models.credit_application import *
# from common.models.other.note import Note
# from common.serializers.credit_application import *
# from common.models.document.models import *
# from common.utils.credit_application_sections import generate_credit_application_sections_statuses
# from common.utils.checklists_data_by_tab_id import generate_checklists_data_by_tab_id
# from common.configs.other.documents_storage import documents_storage
from common.models import AccountRelatedParty
from common.configs.views.arrangement.account_related_party import generate_config
from common.serializers import ReadOnlyAccountRelatedPartySerializer, EditAccountRelatedPartySerializer


class AccountRelatedPartyAPI(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        account_related_party_id = kwargs['id']
        try:
            account_related_party = AccountRelatedParty.objects.get(AccountRelatedPartyId=account_related_party_id)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('AccountRelatedParty with {}id doesn\'t exist'.format(account_related_party_id))

        edit_host_values = account_related_party.EditHostValuesFlag

        response = EditAccountRelatedPartySerializer(account_related_party).data if edit_host_values else ReadOnlyAccountRelatedPartySerializer(account_related_party).data

        response = {
            "data": response,
            "config": generate_config(True,
                                      edit_host_values,
                                      account_related_party.RelatedPartyId_id,
                                      account_related_party.AccountId_id,
                                      account_related_party_id)
        }

        return JsonResponse(response)
