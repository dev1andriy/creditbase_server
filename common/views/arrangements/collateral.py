from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from rest_framework.views import APIView
from django.utils import timezone
from django.db.models import Q
from common.models.base_party import BaseParty
from common.models import RelatedParty, CreditApplication, Coverage, CoverageArchived
from common.configs.views.arrangement.collateral import generate_config

from common.models.arrangement import Collateral, CollateralArchived
from common.serializers import CollateralSerializer, CollateralsSerializer, CollateralCoverageDataSerializer
from common.utils.params import generate_params

collateral_details_fields = [
    {'db_field': 'BasePartyId_id', 'field_label': 'baseParty'},
    {'db_field': 'ArrangementType_id', 'field_label': 'arrangementType'},
    {'db_field': 'CollateralIdParent_id', 'field_label': 'parentCollateral'},
    {'db_field': 'CollateralIdHost', 'field_label': 'hostCollateralId'},
]


class CollateralsAPIView(APIView):
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
                main_collateral = Collateral.objects.filter(BasePartyId_id=kwargs['id']).order_by('OrderingRank')
                related_collaterals = Collateral.objects.filter(BasePartyId_id__in=base_party_ids).exclude(BasePartyId_id=kwargs['id']).order_by('OrderingRank')

                response_data = CollateralsSerializer(main_collateral, many=True, model=Collateral).data + CollateralsSerializer(related_collaterals, many=True, model=Collateral).data
            else:
                response_data = CollateralsSerializer(Collateral.objects.all(), many=True, model=Collateral).data

            base_party_id = base_party.BasePartyId if base_party is not None else None

        elif data_view is not None and credit_application_id is not None and data_view != 1:
            if data_view == 2 or data_view == 3:
                global collateral_model

                credit_application_query_set = CreditApplication.objects.filter(CreditApplicationId=credit_application_id)
                if not credit_application_query_set.exists():
                    return HttpResponseNotFound('Credit Application doesn\'t exist')

                credit_application = credit_application_query_set.first()

                if credit_application.DecisionType is None:
                    collateral_model = Collateral
                elif credit_application.DecisionType is not None:
                    collateral_model = CollateralArchived

                response_data = CollateralsSerializer(collateral_model.objects.filter(CreditApplicationId=credit_application_id), many=True, model=collateral_model).data
            else:
                response_data = []
        else:
            response_data = []

        response = {
            'data': response_data,
            'config': generate_config(False, base_party_id)
        }

        return JsonResponse(response)


class CollateralAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        global collateral_model
        global coverage_model

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
            collateral_model = Collateral
            coverage_model = Coverage
        elif credit_application_id is not None and credit_application.DecisionType is not None:
            collateral_model = CollateralArchived
            coverage_model = CoverageArchived

        collateral = collateral_model()
        collateral.DataView = data_view
        collateral.RequestType_id = list(filter(lambda param: param.get('name') == 'requestType', request.data.get('details', {}).get('grid', [])))[0].get('proposedValue')
        collateral.CreditApplicationId = credit_application

        if 'details' in request.data:
            details = request.data.get('details', {})

            if 'fields' in details:
                fields = details.get('fields', [])

                for field in collateral_details_fields:
                    if '_id' in field['db_field'] and field['field_label'] in fields and fields[field['field_label']] is not None:
                        setattr(collateral, field['db_field'], int(fields[field['field_label']]))
                    elif '_id' not in field['db_field'] and field['field_label'] in fields and fields[field['field_label']] is not None:
                        setattr(collateral, field['db_field'], fields[field['field_label']])

            if 'grid' in details:
                grid = details.get('grid', [])

                for parameter in grid:
                    name = parameter.get('name', '')

                    if hasattr(collateral, name):
                        parameter_json = {
                            "ProposedValue": parameter.get('proposedValue'),
                            "HostValue": parameter.get('hostValue'),
                            "ModifyFlag": parameter.get('modify'),
                            "PrintFlag": parameter.get('print')
                        }

                        setattr(collateral, name, parameter_json)

        if 'coverage' in request.data:
            coverage = request.data.get('coverage', {})

            if 'collateralLinkages' in coverage:
                collateral_linkages = coverage.get('collateralLinkages', [])

                if len(collateral_linkages) > 0:
                    for linkage in collateral_linkages:
                        if 'temp' in str(linkage.get('id', '')):
                            coverage = coverage_model()
                            coverage.CollateralId = collateral
                            coverage.FacilityId_id = linkage.get('facilityId', None)
                            coverage.CreditApplicationId = credit_application
                            coverage.Assignment = linkage.get('assignment', None)
                            coverage.LienOrder = linkage.get('lienOrder', None)
                            coverage.BindWith = 'Collateral'
                            coverage.save()

        collateral.save()

        return JsonResponse(CollateralsSerializer(collateral, model=collateral_model).data)

    def put(self, request, *args, **kwargs):
        global collateral_model
        global coverage_model

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
        collateral_id = request.data.get('collateralId')

        if credit_application_id is None or (credit_application_id is not None and credit_application.DecisionType is None):
            collateral_model = Collateral
            coverage_model = Coverage
        elif credit_application_id is not None and credit_application.DecisionType is not None:
            collateral_model = CollateralArchived
            coverage_model = CoverageArchived

        collateral_query_set = collateral_model.objects.filter(CollateralId=collateral_id)
        if not collateral_query_set.exists():
            return HttpResponseBadRequest('Collateral with {}id does not exist'.format(collateral_id))

        collateral = collateral_query_set.first()

        credit_application = collateral.CreditApplicationId if credit_application is None else credit_application

        collateral.DataView = data_view
        collateral.RequestType_id = list(filter(lambda param: param.get('name') == 'requestType', request.data.get('details', {}).get('grid', [])))[0].get('proposedValue')
        collateral.CreditApplicationId = credit_application

        existing_coverage_linkages = []

        if 'details' in request.data:
            details = request.data.get('details', {})

            if 'fields' in details:
                fields = details.get('fields', [])

                for field in collateral_details_fields:
                    if '_id' in field['db_field'] and field['field_label'] in fields and fields[field['field_label']] is not None:
                        setattr(collateral, field['db_field'], int(fields[field['field_label']]))
                    elif '_id' not in field['db_field'] and field['field_label'] in fields and fields[field['field_label']] is not None:
                        setattr(collateral, field['db_field'], fields[field['field_label']])

            if 'grid' in details:
                grid = details.get('grid', [])

                for parameter in grid:
                    name = parameter.get('name')

                    if hasattr(collateral, name):
                        parameter_json = {
                            "ProposedValue": parameter.get('proposedValue'),
                            "HostValue": parameter.get('hostValue'),
                            "ModifyFlag": parameter.get('modify'),
                            "PrintFlag": parameter.get('print')
                        }

                        setattr(collateral, name, parameter_json)

        if 'coverage' in request.data:
            coverage = request.data.get('coverage', {})

            if 'collateralLinkages' in coverage:
                collateral_linkages = coverage.get('collateralLinkages', [])

                if len(collateral_linkages) > 0:
                    for linkage in collateral_linkages:
                        if 'temp' in str(linkage.get('id', '')):
                            coverage = coverage_model()
                            coverage.CollateralId = collateral
                            coverage.FacilityId_id = linkage.get('facilityId', None)
                            coverage.CreditApplicationId = credit_application
                            coverage.Assignment = linkage.get('assignment', None)
                            coverage.LienOrder = linkage.get('lienOrder', None)
                            coverage.BindWith = 'Collateral'
                            coverage.save()

                            existing_coverage_linkages.append(coverage.CoverageId)

                        elif 'temp' not in str(linkage.get('id', '')) and 'isChange' in linkage and linkage.get('isChange', False):
                            coverage = coverage_model.objects.get(CoverageId=linkage.get('id'))
                            coverage.CollateralId = collateral
                            coverage.FacilityId_id = linkage.get('facilityId', None)
                            coverage.CreditApplicationId = credit_application
                            coverage.Assignment = linkage.get('assignment', None)
                            coverage.LienOrder = linkage.get('lienOrder', None)
                            coverage.save()

                            existing_coverage_linkages.append(coverage.CoverageId)

                        elif 'temp' not in str(linkage.get('id', '')) and isinstance(linkage.get('id', None), int) and 'isChange' not in linkage:
                            existing_coverage_linkages.append(linkage.get('id'))

                coverage_model.objects.filter(CollateralId=collateral.CollateralId).exclude(CoverageId__in=existing_coverage_linkages).delete()

        collateral.save()

        return JsonResponse(CollateralsSerializer(collateral, model=collateral_model).data)

    def get(self, request, **kwargs):
        global collateral_model

        id = kwargs.get('id', None)
        model = kwargs.get('model', None)

        if id is None or model is None:
            return HttpResponseNotFound('Wrong input data')

        # credit_application_query_set = CreditApplication.objects.filter(CreditApplicationId=credit_application_id)
        #
        # if not credit_application_query_set.exists():
        #     return HttpResponseNotFound('Credit Application with {}id doesn\'t exist'.format(credit_application_id))

        # credit_application = credit_application_query_set.first()

        if model == 'Collateral':
            collateral_model = Collateral
        elif model == 'CollateralArchived':
            collateral_model = CollateralArchived

        collateral_query_set = collateral_model.objects.filter(CollateralId=id)

        if not collateral_query_set.exists():
            return HttpResponseNotFound('Collateral with {}id doesn\'t exist'.format(id))

        collateral = collateral_query_set.first()

        response = CollateralSerializer(collateral, model=collateral_model).data

        response = {
            'data': response,
            'config': generate_config(edit=True, base_party_id=collateral.BasePartyId_id)
        }

        return JsonResponse(response)

    def delete(self, request, *args, **kwargs):
        global collateral_model

        id = kwargs.get('id', None)
        model = kwargs.get('model', None)

        if id is None or model is None:
            return HttpResponseNotFound('Wrong input data')

        if model == 'Collateral':
            collateral_model = Collateral
        elif model == 'CollateralArchived':
            collateral_model = CollateralArchived

        collateral_query_set = collateral_model.objects.filter(CollateralId=kwargs['id'])
        if not collateral_query_set.exists():
            return HttpResponseBadRequest(content='Collateral with {}id does not exist'.format(kwargs['id']))

        collateral_query_set.delete()

        return HttpResponse(status=200)


class CollateralGetParametersAPIView(APIView):

    def post(self, request, *args, **kwargs):
        if request.data is None:
            return HttpResponseBadRequest('Wrong input data')

        data = request.data

        if 'dataView' in data and 'arrangementType' in data and 'requestType' in data:
            data_view = data['dataView']
            arrangement_type = data['arrangementType']
            request_type = data['requestType']

            params_to_display = generate_params(data_view, arrangement_type, request_type)

            return JsonResponse(params_to_display, safe=False)

        raise Exception('Wrong input data')


class CollateralGetCoverageDataAPIView(APIView):

    def get(self, request, *args, **kwargs):
        global collateral_model

        credit_application = request.GET.get('credit_application', None)
        collateral_id = kwargs.get('id', None)
        if collateral_id is None:
            return HttpResponseBadRequest('Collateral Id is missing')

        if credit_application is None:
            collateral_model = Collateral
        else:
            credit_application_query_set = CreditApplication.objects.filter(CreditApplicationId=credit_application)
            if not credit_application_query_set.exists():
                return HttpResponseBadRequest('Credit Application doesn\'t exist')
            else:
                credit_application = credit_application_query_set.first()
                collateral_model = Collateral if credit_application.DecisionType is None else CollateralArchived

        collateral_query_set = collateral_model.objects.filter(CollateralId=collateral_id)
        if not collateral_query_set.exists():
            return HttpResponseBadRequest('Collateral doesn\'t exist')
        collateral = collateral_query_set.first()
        response_data = CollateralCoverageDataSerializer(collateral, model=collateral_model).data

        return JsonResponse(response_data)

class CollateralArchiveAPIView(APIView):

    def get(self, request, **kwargs):
        global collateral_model

        model = kwargs.get('model')
        collateral_id = kwargs.get('id')

        if model == 'Collateral':
            collateral_model = Collateral
        else:
            collateral_model = CollateralArchived

        collateral_query_set = collateral_model.objects.filter(CollateralId=collateral_id)
        if not collateral_query_set.exists():
            return JsonResponse({'error': 'Collateral doesn\'t exist'}, status=400)

        collateral = collateral_query_set.first()
        if collateral.CreditApplicationId is None:
            return JsonResponse({'error': 'Collateral hasn\'t credit application'}, status=400)

        collateral_archived = CollateralArchived()

        for field_name in collateral.__dict__:
            setattr(collateral_archived, field_name, getattr(collateral, field_name))

        collateral_archived.CollateralId = None
        collateral_archived.ArchiveStatus = collateral.CreditApplicationId.ApplicationStatus

        if model == 'Collateral':
            collateral_archived.ArchiveVersion = CollateralArchived.objects.filter(ActiveVersion_id=collateral.CollateralId).count() + 1
            collateral_archived.ActiveVersion = collateral
        else:
            collateral_archived.ArchiveVersion = CollateralArchived.objects.filter(ActiveVersion_id=collateral.ActiveVersion.CollateralId).count() + 1
            collateral_archived.ActiveVersion = collateral.ActiveVersion

        collateral_archived.save()


        return JsonResponse({'message': 'Success'}, status=200)
