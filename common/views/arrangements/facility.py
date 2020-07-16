from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from rest_framework.views import APIView
from django.utils import timezone
from django.db.models import Q
from common.models.base_party import BaseParty
from common.models import RelatedParty, CreditApplication, FacilityArchived, Coverage, CoverageArchived
from common.configs.views.arrangement.facility import generate_config

from common.models.arrangement import Facility
from common.serializers import FacilitySerializer, FacilitiesSerializer, FacilityCoverageDataSerializer
from common.utils.params import generate_params

facility_details_fields = [
    {'db_field': 'BasePartyId_id', 'field_label': 'baseParty'},
    {'db_field': 'ArrangementType_id', 'field_label': 'arrangementType'},
    {'db_field': 'FacilityIdParent_id', 'field_label': 'facilityParent'},
    {'db_field': 'FacilityIdHost', 'field_label': 'hostFacilityId'},
]

facility_coverage_linkages_fields = [
    {'db_field': 'Assignment', 'field_label': 'assignment'},
    {'db_field': 'LienOrder', 'field_label': 'lienOrder'}
]


class FacilitiesAPIView(APIView):
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
                main_facility = Facility.objects.filter(BasePartyId_id=kwargs['id']).order_by('OrderingRank')
                related_facilities = Facility.objects.filter(BasePartyId_id__in=base_party_ids).exclude(BasePartyId_id=kwargs['id']).order_by('OrderingRank')

                response_data = FacilitiesSerializer(main_facility, many=True, model=Facility).data + FacilitiesSerializer(related_facilities, many=True, model=Facility).data
            else:
                response_data = FacilitiesSerializer(Facility.objects.all(), many=True, model=Facility).data

            base_party_id = base_party.BasePartyId if base_party is not None else None

        elif data_view is not None and credit_application_id is not None and data_view != 1:
            if data_view == 2 or data_view == 3:
                global facility_model

                credit_application_query_set = CreditApplication.objects.filter(CreditApplicationId=credit_application_id)
                if not credit_application_query_set.exists():
                    return HttpResponseNotFound('Credit Application doesn\'t exist')

                credit_application = credit_application_query_set.first()

                if credit_application.DecisionType is None:
                    facility_model = Facility
                elif credit_application.DecisionType is not None:
                    facility_model = FacilityArchived

                response_data = FacilitiesSerializer(facility_model.objects.filter(CreditApplicationId=credit_application_id), many=True, model=facility_model).data
            else:
                response_data = []
        else:
            response_data = []

        response = {
            'data': response_data,
            'config': generate_config(False, base_party_id)
        }

        return JsonResponse(response)


class FacilityAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        global facility_model
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
            facility_model = Facility
            coverage_model = Coverage
        elif credit_application_id is not None and credit_application.DecisionType is not None:
            facility_model = FacilityArchived
            coverage_model = CoverageArchived

        facility = facility_model()
        facility.DataView = data_view
        facility.RequestType_id = list(filter(lambda param: param.get('name') == 'requestType', request.data.get('details', {}).get('grid', [])))[0].get('proposedValue')
        facility.CreditApplicationId = credit_application

        if 'details' in request.data:
            details = request.data.get('details', {})

            if 'fields' in details:
                fields = details.get('fields', [])

                for field in facility_details_fields:
                    if '_id' in field['db_field'] and field['field_label'] in fields and fields[field['field_label']] is not None:
                        setattr(facility, field['db_field'], int(fields[field['field_label']]))
                    elif '_id' not in field['db_field'] and field['field_label'] in fields and fields[field['field_label']] is not None:
                        setattr(facility, field['db_field'], fields[field['field_label']])

            if 'grid' in details:
                grid = details.get('grid', [])

                for parameter in grid:
                    name = parameter.get('name', '')

                    if hasattr(facility, name):
                        parameter_json = {
                            "ProposedValue": parameter.get('proposedValue'),
                            "HostValue": parameter.get('hostValue'),
                            "ModifyFlag": parameter.get('modify'),
                            "PrintFlag": parameter.get('print')
                        }

                        setattr(facility, name, parameter_json)

        if 'coverage' in request.data:
            coverage = request.data.get('coverage', {})

            if 'collateralLinkages' in coverage:
                collateral_linkages = coverage.get('collateralLinkages', [])

                if len(collateral_linkages) > 0:
                    for linkage in collateral_linkages:
                        if 'temp' in str(linkage.get('id', '')):
                            coverage = coverage_model()
                            coverage.FacilityId = facility
                            coverage.CollateralId_id = linkage.get('collateralId', None)
                            coverage.CreditApplicationId = credit_application
                            coverage.Assignment = linkage.get('assignment', None)
                            coverage.LienOrder = linkage.get('lienOrder', None)
                            coverage.BindWith = 'Facility'
                            coverage.save()

        facility.save()

        return JsonResponse(FacilitiesSerializer(facility, model=facility_model).data)

    def put(self, request, *args, **kwargs):
        global facility_model
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
        facility_id = request.data.get('facilityId')

        if credit_application_id is None or (credit_application_id is not None and credit_application.DecisionType is None):
            facility_model = Facility
            coverage_model = Coverage
        elif credit_application_id is not None and credit_application.DecisionType is not None:
            facility_model = FacilityArchived
            coverage_model = CoverageArchived

        facility_query_set = facility_model.objects.filter(FacilityId=facility_id)
        if not facility_query_set.exists():
            return HttpResponseBadRequest('Facility with {}id does not exist'.format(facility_id))

        facility = facility_query_set.first()

        credit_application = facility.CreditApplicationId if credit_application is None else credit_application

        facility.DataView = data_view
        facility.RequestType_id = facility.RequestType_id = list(filter(lambda param: param.get('name') == 'requestType', request.data.get('details', {}).get('grid', [])))[0].get('proposedValue')
        facility.CreditApplicationId = credit_application

        existing_coverage_linkages = []

        if 'details' in request.data:
            details = request.data.get('details', {})

            if 'fields' in details:
                fields = details.get('fields', [])

                for field in facility_details_fields:
                    if '_id' in field['db_field'] and field['field_label'] in fields and fields[field['field_label']] is not None:
                        setattr(facility, field['db_field'], int(fields[field['field_label']]))
                    elif '_id' not in field['db_field'] and field['field_label'] in fields and fields[field['field_label']] is not None:
                        setattr(facility, field['db_field'], fields[field['field_label']])

            if 'grid' in details:
                grid = details.get('grid', [])

                for parameter in grid:
                    name = parameter.get('name')

                    if hasattr(facility, name):
                        parameter_json = {
                            "ProposedValue": parameter.get('proposedValue'),
                            "HostValue": parameter.get('hostValue'),
                            "ModifyFlag": parameter.get('modify'),
                            "PrintFlag": parameter.get('print')
                        }

                        setattr(facility, name, parameter_json)

        if 'coverage' in request.data:
            coverage = request.data.get('coverage', {})

            if 'collateralLinkages' in coverage:
                collateral_linkages = coverage.get('collateralLinkages', [])

                if len(collateral_linkages) > 0:
                    for linkage in collateral_linkages:
                        if 'temp' in str(linkage.get('id', '')):
                            coverage = coverage_model()
                            coverage.FacilityId = facility
                            coverage.CollateralId_id = linkage.get('collateralId', None)
                            coverage.CreditApplicationId = credit_application
                            coverage.Assignment = linkage.get('assignment', None)
                            coverage.LienOrder = linkage.get('lienOrder', None)
                            coverage.BindWith = 'Facility'
                            coverage.save()

                            existing_coverage_linkages.append(coverage.CoverageId)

                        elif 'temp' not in str(linkage.get('id', '')) and 'isChange' in linkage and linkage.get('isChange', False):
                            coverage = coverage_model.objects.get(CoverageId=linkage.get('id'))
                            coverage.FacilityId = facility
                            coverage.CollateralId_id = linkage.get('collateralId', None)
                            coverage.CreditApplicationId = credit_application
                            coverage.Assignment = linkage.get('assignment', None)
                            coverage.LienOrder = linkage.get('lienOrder', None)
                            coverage.save()

                            existing_coverage_linkages.append(coverage.CoverageId)

                        elif 'temp' not in str(linkage.get('id', '')) and isinstance(linkage.get('id', None), int) and 'isChange' not in linkage:
                            existing_coverage_linkages.append(linkage.get('id'))

                coverage_model.objects.filter(FacilityId=facility.FacilityId).exclude(CoverageId__in=existing_coverage_linkages).delete()

        facility.save()

        return JsonResponse(FacilitiesSerializer(facility, model=facility_model).data)

    def get(self, request, **kwargs):
        global facility_model

        id = kwargs.get('id', None)
        model = kwargs.get('model', None)

        if id is None or model is None:
            return HttpResponseNotFound('Wrong input data')

        # credit_application_query_set = CreditApplication.objects.filter(CreditApplicationId=credit_application_id)
        #
        # if not credit_application_query_set.exists():
        #     return HttpResponseNotFound('Credit Application with {}id doesn\'t exist'.format(credit_application_id))

        # credit_application = credit_application_query_set.first()

        if model == 'Facility':
            facility_model = Facility
        elif model == 'FacilityArchived':
            facility_model = FacilityArchived

        facility_query_set = facility_model.objects.filter(FacilityId=id)

        if not facility_query_set.exists():
            return HttpResponseNotFound('Facility with {}id doesn\'t exist'.format(id))

        facility = facility_query_set.first()

        response = FacilitySerializer(facility, model=facility_model).data

        response = {
            'data': response,
            'config': generate_config(edit=True, base_party_id=facility.BasePartyId_id)
        }

        return JsonResponse(response)

    def delete(self, request, *args, **kwargs):
        global facility_model

        id = kwargs.get('id', None)
        model = kwargs.get('model', None)

        if id is None or model is None:
            return HttpResponseNotFound('Wrong input data')

        if model == 'Facility':
            facility_model = Facility
        elif model == 'FacilityArchived':
            facility_model = FacilityArchived

        facility_query_set = facility_model.objects.filter(FacilityId=kwargs['id'])
        if not facility_query_set.exists():
            return HttpResponseBadRequest(content='Facility with {}id does not exist'.format(kwargs['id']))

        facility_query_set.delete()

        return HttpResponse(status=200)

        # return HttpResponse('Account is linked with Facility {}'.format(1), status=400)


class FacilityGetParametersAPIView(APIView):

    def post(self, request, *args, **kwargs):
        if request.data is None:
            raise Exception('Wrong input data')

        data = request.data

        if 'dataView' in data and 'arrangementType' in data and 'requestType' in data:
            data_view = data['dataView']
            arrangement_type = data['arrangementType']
            request_type = data['requestType']

            params_to_display = generate_params(data_view, arrangement_type, request_type)

            return JsonResponse(params_to_display, safe=False)

        raise Exception('Wrong input data')


class FacilityGetCoverageDataAPIView(APIView):

    def get(self, request, *args, **kwargs):
        global facility_model

        credit_application = request.GET.get('credit_application', None)
        facility_id = kwargs.get('id', None)
        if facility_id is None:
            return HttpResponseBadRequest('Facility Id is missing')

        if credit_application is None:
            collateral_model = Facility
        else:
            credit_application_query_set = CreditApplication.objects.filter(CreditApplicationId=credit_application)
            if not credit_application_query_set.exists():
                return HttpResponseBadRequest('Credit Application doesn\'t exist')
            else:
                credit_application = credit_application_query_set.first()
                facility_model = Facility if credit_application.DecisionType is None else FacilityArchived

        facility_query_set = facility_model.objects.filter(FacilityId=facility_id)
        if not facility_query_set.exists():
            return HttpResponseBadRequest('Facility doesn\'t exist')
        facility = facility_query_set.first()
        response_data = FacilityCoverageDataSerializer(facility, model=facility_model).data

        return JsonResponse(response_data)

class FacilityArchiveAPIView(APIView):

    def get(self, request, **kwargs):
        global facility_model

        model = kwargs.get('model')
        facility_id = kwargs.get('id')

        if model == 'Facility':
            facility_model = Facility
        else:
            facility_model = FacilityArchived

        facility_query_set = facility_model.objects.filter(FacilityId=facility_id)
        if not facility_query_set.exists():
            return JsonResponse({'error': 'Facility doesn\'t exist'}, status=400)

        facility = facility_query_set.first()
        if facility.CreditApplicationId is None:
            return JsonResponse({'error': 'Facility hasn\'t credit application'}, status=400)

        facility_archived = FacilityArchived()

        for field_name in facility.__dict__:
            setattr(facility_archived, field_name, getattr(facility, field_name))

        facility_archived.FacilityId = None
        facility_archived.ArchiveStatus = facility.CreditApplicationId.ApplicationStatus

        if model == 'Facility':
            facility_archived.ArchiveVersion = FacilityArchived.objects.filter(ActiveVersion_id=facility.FacilityId).count() + 1
            facility_archived.ActiveVersion = facility
        else:
            facility_archived.ArchiveVersion = FacilityArchived.objects.filter(ActiveVersion_id=facility.ActiveVersion.FacilityId).count() + 1
            facility_archived.ActiveVersion = facility.ActiveVersion

        facility_archived.save()


        return JsonResponse({'message': 'Success'}, status=200)
