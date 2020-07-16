from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from rest_framework.views import APIView
from django.utils import timezone
from django.db.models import Q
from common.models.base_party import BaseParty
from common.models import RelatedParty, CreditApplication
from common.configs.views.arrangement.deposit import generate_config

from common.models.arrangement import Deposit, DepositArchived
from common.serializers import DepositsSerializer, DepositSerializer
from common.utils.params import generate_params

deposit_details_fields = [
    {'db_field': 'BasePartyId_id', 'field_label': 'baseParty'},
    {'db_field': 'ArrangementType_id', 'field_label': 'arrangementType'},
    {'db_field': 'DepositIdHost', 'field_label': 'hostDepositId'},
]


class DepositsAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        if 'id' in kwargs.keys():
            base_party = BaseParty.objects.filter(BasePartyId=kwargs['id']).first()
        else:
            base_party = None

        base_party_id = base_party.BasePartyId if base_party is not None else None

        data_view = request.GET.get('data_view', None)
        credit_application_id = request.GET.get('credit_application', None)

        if (data_view is None or credit_application_id is None) or (data_view is not None and credit_application_id is not None and data_view == 1):
            if 'id' in kwargs.keys():
                base_party_ids = [kwargs['id']]
                related_parties = RelatedParty.objects.filter((Q(BaseParty1Id=base_party) | Q(BaseParty2Id=base_party)), (Q(EndDate=None) | Q(EndDate__gte=timezone.now())))
                for party in related_parties:
                    if party.BaseParty1Id not in base_party_ids:
                        base_party_ids.append(party.BaseParty1Id)
                    if party.BaseParty2Id not in base_party_ids:
                        base_party_ids.append(party.BaseParty2Id)
                main_deposit = Deposit.objects.filter(BasePartyId_id=kwargs['id'])
                related_deposits = Deposit.objects.filter(BasePartyId_id__in=base_party_ids).exclude(BasePartyId_id=kwargs['id'])

                response_data = DepositsSerializer(main_deposit, many=True, model=Deposit).data + DepositsSerializer(related_deposits, many=True, model=Deposit).data
            else:
                response_data = DepositsSerializer(Deposit.objects.all(), many=True, model=Deposit).data

            base_party_id = base_party.BasePartyId if base_party is not None else None

        elif data_view is not None and credit_application_id is not None and data_view != 1:
            if data_view == 2 or data_view == 3:
                global deposit_model

                credit_application_query_set = CreditApplication.objects.filter(CreditApplicationId=credit_application_id)
                if not credit_application_query_set.exists():
                    return HttpResponseNotFound('Credit Application doesn\'t exist')

                credit_application = credit_application_query_set.first()

                if credit_application.DecisionType is None:
                    deposit_model = Deposit
                elif credit_application.DecisionType is not None:
                    deposit_model = DepositArchived

                response_data = DepositsSerializer(deposit_model.objects.filter(CreditApplicationId=credit_application_id), many=True, model=deposit_model).data
            else:
                response_data = []
        else:
            response_data = []

        response = {
            'data': response_data,
            'config': generate_config(False, base_party_id)
        }

        return JsonResponse(response)


class DepositAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        global deposit_model

        if 'dataView' not in request.data:
            return HttpResponseBadRequest('DataView is missing')

        credit_application_id = request.data.get('creditApplicationId', None)
        if credit_application_id is not None:
            credit_application_query_set = CreditApplication.objects.filter(CreditApplicationId=credit_application_id)
            if not credit_application_query_set.exists():
                return HttpResponseBadRequest('Credit Application doesn\'t exist')

            credit_application = credit_application_query_set.first()
        else:
            credit_application = None

        data_view = request.data.get('dataView', None)

        if credit_application_id is None or (credit_application_id is not None and credit_application.DecisionType is None):
            deposit_model = Deposit
        elif credit_application_id is not None and credit_application.DecisionType is not None:
            deposit_model = DepositArchived

        deposit = deposit_model()
        deposit.DataView = data_view
        deposit.CreditApplicationId = credit_application

        if 'details' in request.data:
            details = request.data.get('details', {})

            if 'fields' in details:
                fields = details.get('fields', [])

                for field in deposit_details_fields:
                    if '_id' in field['db_field'] and field['field_label'] in fields and fields[field['field_label']] is not None:
                        setattr(deposit, field['db_field'], int(fields[field['field_label']]))
                    elif '_id' not in field['db_field'] and field['field_label'] in fields and fields[field['field_label']] is not None:
                        setattr(deposit, field['db_field'], fields[field['field_label']])

            if 'grid' in details:
                grid = details.get('grid', [])

                for parameter in grid:
                    name = parameter.get('name', '')

                    if hasattr(deposit, name):
                        parameter_json = {
                            "ProposedValue": parameter.get('proposedValue'),
                            "HostValue": parameter.get('hostValue'),
                            "ModifyFlag": parameter.get('modify'),
                            "PrintFlag": parameter.get('print')
                        }

                        setattr(deposit, name, parameter_json)

        deposit.save()

        return JsonResponse(DepositsSerializer(deposit, model=deposit_model).data)

    def put(self, request, *args, **kwargs):
        global deposit_model

        if 'dataView' not in request.data:
            return HttpResponseBadRequest('DataView is missing')

        credit_application_id = request.data.get('creditApplicationId', None)
        if credit_application_id is not None:
            credit_application_query_set = CreditApplication.objects.filter(CreditApplicationId=credit_application_id)
            if not credit_application_query_set.exists():
                return HttpResponseBadRequest('Credit Application doesn\'t exist')

            credit_application = credit_application_query_set.first()
        else:
            credit_application = None

        data_view = request.data.get('dataView')
        deposit_id = request.data.get('depositId')

        if credit_application_id is None or (credit_application_id is not None and credit_application.DecisionType is None):
            deposit_model = Deposit
        elif credit_application_id is not None and credit_application.DecisionType is not None:
            deposit_model = DepositArchived

        deposit_query_set = deposit_model.objects.filter(DepositId=deposit_id)
        if not deposit_query_set.exists():
            return HttpResponseBadRequest('Deposit with {}id does not exist'.format(deposit_id))

        deposit = deposit_query_set.first()

        credit_application = deposit.CreditApplicationId if credit_application is None else credit_application

        deposit.DataView = data_view
        deposit.CreditApplicationId = credit_application

        if 'details' in request.data:
            details = request.data.get('details', {})

            if 'fields' in details:
                fields = details.get('fields', [])

                for field in deposit_details_fields:
                    if '_id' in field['db_field'] and field['field_label'] in fields and fields[field['field_label']] is not None:
                        setattr(deposit, field['db_field'], int(fields[field['field_label']]))
                    elif '_id' not in field['db_field'] and field['field_label'] in fields and fields[field['field_label']] is not None:
                        setattr(deposit, field['db_field'], fields[field['field_label']])

            if 'grid' in details:
                grid = details.get('grid', [])

                for parameter in grid:
                    name = parameter.get('name')

                    if hasattr(deposit, name):
                        parameter_json = {
                            "ProposedValue": parameter.get('proposedValue'),
                            "HostValue": parameter.get('hostValue'),
                            "ModifyFlag": parameter.get('modify'),
                            "PrintFlag": parameter.get('print')
                        }

                        setattr(deposit, name, parameter_json)

        deposit.save()

        return JsonResponse(DepositsSerializer(deposit, model=deposit_model).data)

    def get(self, request, **kwargs):
        global deposit_model

        id = kwargs.get('id', None)
        model = kwargs.get('model', None)

        if id is None or model is None:
            return HttpResponseNotFound('Wrong input data')

        # credit_application_query_set = CreditApplication.objects.filter(CreditApplicationId=credit_application_id)
        #
        # if not credit_application_query_set.exists():
        #     return HttpResponseNotFound('Credit Application with {}id doesn\'t exist'.format(credit_application_id))

        # credit_application = credit_application_query_set.first()

        if model == 'Deposit':
            deposit_model = Deposit
        elif model == 'DepositArchived':
            deposit_model = DepositArchived

        deposit_query_set = deposit_model.objects.filter(DepositId=id)

        if not deposit_query_set.exists():
            return HttpResponseNotFound('Deposit with {}id doesn\'t exist'.format(id))

        deposit = deposit_query_set.first()

        response = DepositSerializer(deposit, model=deposit_model).data

        response = {
            'data': response,
            'config': generate_config(edit=True, base_party_id=deposit.BasePartyId_id)
        }

        return JsonResponse(response)

    def delete(self, request, *args, **kwargs):
        global deposit_model

        id = kwargs.get('id', None)
        model = kwargs.get('model', None)

        if id is None or model is None:
            return HttpResponseNotFound('Wrong input data')

        if model == 'Deposit':
            deposit_model = Deposit
        elif model == 'DepositArchived':
            deposit_model = DepositArchived

        deposit_query_set = deposit_model.objects.filter(DepositId=kwargs['id'])
        if not deposit_query_set.exists():
            return HttpResponseBadRequest(content='Deposit with {}id does not exist'.format(kwargs['id']))

        deposit_query_set.delete()

        return HttpResponse(status=200)


class DepositGetParametersAPIView(APIView):

    def post(self, request, *args, **kwargs):
        if request.data is None:
            raise Exception('Wrong input data')

        data = request.data

        if 'dataView' in data and 'arrangementType' in data:
            data_view = data['dataView']
            arrangement_type = data['arrangementType']

            params_to_display = generate_params(data_view, arrangement_type, request_type=None)

            return JsonResponse(params_to_display, safe=False)

        raise Exception('Wrong input data')


class DepositArchiveAPIView(APIView):

    def get(self, request, **kwargs):
        global deposit_model

        model = kwargs.get('model')
        deposit_id = kwargs.get('id')

        if model == 'Deposit':
            deposit_model = Deposit
        else:
            deposit_model = DepositArchived

        deposit_query_set = deposit_model.objects.filter(DepositId=deposit_id)
        if not deposit_query_set.exists():
            return JsonResponse({'error': 'Deposit doesn\'t exist'}, status=400)

        deposit = deposit_query_set.first()
        if deposit.CreditApplicationId is None:
            return JsonResponse({'error': 'Deposit hasn\'t credit application'}, status=400)

        deposit_archived = DepositArchived()

        for field_name in deposit.__dict__:
            setattr(deposit_archived, field_name, getattr(deposit, field_name))

        deposit_archived.DepositId = None
        deposit_archived.ArchiveStatus = deposit.CreditApplicationId.ApplicationStatus

        if model == 'Deposit':
            deposit_archived.ArchiveVersion = DepositArchived.objects.filter(ActiveVersion_id=deposit.DepositId).count() + 1
            deposit_archived.ActiveVersion = deposit
        else:
            deposit_archived.ArchiveVersion = DepositArchived.objects.filter(ActiveVersion_id=deposit.ActiveVersion.DepositId).count() + 1
            deposit_archived.ActiveVersion = deposit.ActiveVersion

        deposit_archived.save()


        return JsonResponse({'message': 'Success'}, status=200)
