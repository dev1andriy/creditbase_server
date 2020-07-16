from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from rest_framework.views import APIView
from django.utils import timezone
from django.db.models import Q
from common.models.base_party import BaseParty
from common.models import RelatedParty, CreditApplication

from common.models.arrangement import Coverage, CoverageArchived, Facility, FacilityArchived,  Collateral, CollateralArchived
from common.serializers.arrangement.coverage import CoveragesSerializer, CoverageCollateralSerializer, CoverageFacilitySerializer
from common.configs.views.arrangement.coverage_list import generate_config as generate_config_coverage_list
from common.configs.views.arrangement.coverage_collateral import generate_config as generate_config_coverage_collateral
from common.configs.views.arrangement.coverage_facility import generate_config as generate_config_coverage_facility


class CoveragesAPIView(APIView):
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
                main_coverage = Coverage.objects.filter(Q(FacilityId__in=Facility.objects.filter(BasePartyId_id=kwargs['id'])) | Q(CollateralId__in=Collateral.objects.filter(BasePartyId_id=kwargs['id'])))
                related_coverages = Coverage.objects.filter(Q(FacilityId__in=Facility.objects.filter(BasePartyId_id__in=base_party_ids)) | Q(CollateralId__in=Collateral.objects.filter(BasePartyId_id__in=base_party_ids))).exclude(Q(FacilityId__in=Facility.objects.filter(BasePartyId_id=kwargs['id'])) | Q(CollateralId__in=Collateral.objects.filter(BasePartyId_id=kwargs['id'])))

                response_data = CoveragesSerializer(main_coverage, many=True, model=Coverage).data + CoveragesSerializer(related_coverages, many=True, model=Coverage).data
            else:
                response_data = CoveragesSerializer(Coverage.objects.all(), many=True, model=Coverage).data

            base_party_id = base_party.BasePartyId if base_party is not None else None

        elif data_view is not None and credit_application_id is not None and data_view != 1:
            if data_view == 2 or data_view == 3:
                global coverage_model

                credit_application_query_set = CreditApplication.objects.filter(CreditApplicationId=credit_application_id)
                if not credit_application_query_set.exists():
                    return HttpResponseNotFound('Credit Application doesn\'t exist')

                credit_application = credit_application_query_set.first()

                if credit_application.DecisionType is None:
                    coverage_model = Coverage
                elif credit_application.DecisionType is not None:
                    coverage_model = CoverageArchived

                response_data = CoveragesSerializer(coverage_model.objects.filter(CreditApplicationId=credit_application_id), many=True, model=coverage_model).data
            else:
                response_data = []
        else:
            response_data = []

        response = {
            'data': response_data,
            'config': generate_config_coverage_list(False, base_party_id)
        }

        return JsonResponse(response)


class CoverageAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        global facility_model
        global collateral_model
        global coverage_model

        bind = kwargs.get('bind')
        model = kwargs.get('model')
        coverage_id = kwargs.get('id')

        if model == 'Coverage':
            facility_model = Facility
            collateral_model = Collateral
            coverage_model = Coverage
        else:
            facility_model = FacilityArchived
            collateral_model = CollateralArchived
            coverage_model = CoverageArchived

        coverage_query_set = coverage_model.objects.filter(CoverageId=coverage_id)
        if not coverage_query_set.exists():
            return JsonResponse({'error': 'Coverage doesn\'t exist'}, status=400)

        coverage = coverage_query_set.first()

        if bind == 'Collateral':
            base_party_id = coverage.CollateralId.BasePartyId_id

            response = {
                'data': CoverageCollateralSerializer(coverage, model=coverage_model).data,
                'config': generate_config_coverage_collateral(False, base_party_id, coverage.CollateralId_id, coverage.CollateralId_id)
            }

            return JsonResponse(response)
        elif bind == 'Facility':
            base_party_id = coverage.FacilityId.BasePartyId_id

            response = {
                'data': CoverageFacilitySerializer(coverage, model=coverage_model).data,
                'config': generate_config_coverage_facility(False, base_party_id, coverage.FacilityId_id, coverage.FacilityId_id)
            }

            return JsonResponse(response)

    def post(self, request, **kwargs):
        global coverage_model

        bind = kwargs.get('bind')
        model = kwargs.get('model')
        coverage_data = request.data.get('coverage', {})

        if model == 'Coverage':
            coverage_model = Coverage
        else:
            coverage_model = CoverageArchived

        coverage = coverage_model()
        coverage.FacilityId_id = coverage_data.get('facilityId', None) if coverage_data.get('facilityId', None) is not None else request.data.get('facilityId')
        coverage.CollateralId_id = coverage_data.get('collateralId', None) if coverage_data.get('collateralId', None) is not None else request.data.get('collateralId')
        coverage.Assignment = coverage_data.get('assignment', None)
        coverage.LienOrder = coverage_data.get('lienOrder', None)
        coverage.BindWith = bind
        coverage.save()

        response = CoveragesSerializer(coverage, model=coverage_model).data

        return JsonResponse(response)

    def put(self, request, **kwargs):
        global coverage_model

        model = kwargs.get('model')
        coverage_id = request.data.get('coverageId', None)
        coverage_data = request.data.get('coverage', {})

        if model == 'Coverage':
            coverage_model = Coverage
        else:
            coverage_model = CoverageArchived

        coverage_query_set = coverage_model.objects.filter(CoverageId=coverage_id)
        if not coverage_query_set.exists():
            return JsonResponse({'error': 'Coverage doesn\'t exist'}, status=400)
        coverage = coverage_query_set.first()

        coverage.FacilityId_id = coverage_data.get('facilityId', None)
        coverage.CollateralId_id = coverage_data.get('collateralId', None)
        coverage.Assignment = coverage_data.get('assignment', None)
        coverage.LienOrder = coverage_data.get('lienOrder', None)
        coverage.save()

        response = CoveragesSerializer(coverage).data

        return JsonResponse(response)



class CoverageGetConfigAPIView(APIView):

    def get(self, request, **kwargs):
        global facility_model
        global collateral_model
        global coverage_model

        bind = kwargs.get('bind')
        model = kwargs.get('model')
        coverage_id = kwargs.get('id')

        if model == 'Coverage':
            facility_model = Facility
            collateral_model = Collateral
            coverage_model = Coverage
        else:
            facility_model = FacilityArchived
            collateral_model = CollateralArchived
            coverage_model = CoverageArchived

        coverage_query_set = coverage_model.objects.filter(CoverageId=coverage_id)
        if not coverage_query_set.exists():
            return JsonResponse({'error': 'Coverage doesn\'t exist'}, status=400)

        coverage = coverage_query_set.first()

        if bind == 'Collateral':
            base_party_id = coverage.CollateralId.BasePartyId_id

            response = {
                'config': generate_config_coverage_collateral(False, base_party_id, coverage.CollateralId_id, coverage.CollateralId_id)
            }

            return JsonResponse(response)
        elif bind == 'Facility':
            base_party_id = coverage.FacilityId.BasePartyId_id

            response = {
                'config': generate_config_coverage_facility(False, base_party_id, coverage.FacilityId_id, coverage.FacilityId_id)
            }

            return JsonResponse(response)


class CoverageArchiveAPIView(APIView):

    def get(self, request, **kwargs):
        global coverage_model

        print('archive')

        model = kwargs.get('model')
        coverage_id = kwargs.get('id')

        if model == 'Coverage':
            coverage_model = Coverage
        else:
            coverage_model = CoverageArchived

        coverage_query_set = coverage_model.objects.filter(CoverageId=coverage_id)
        if not coverage_query_set.exists():
            return JsonResponse({'error': 'Coverage doesn\'t exist'}, status=400)

        coverage = coverage_query_set.first()
        if coverage.CreditApplicationId is None:
            return JsonResponse({'error': 'Coverage hasn\'t credit application'}, status=400)

        coverage_archived = CoverageArchived()

        for field_name in coverage.__dict__:
            setattr(coverage_archived, field_name, getattr(coverage, field_name))

        coverage_archived.CoverageId = None
        coverage_archived.ArchiveStatus = coverage.CreditApplicationId.ApplicationStatus

        if model == 'Coverage':
            coverage_archived.ArchiveVersion = CoverageArchived.objects.filter(ActiveVersion_id=coverage.CoverageId).count() + 1
            coverage_archived.ActiveVersion = coverage
        else:
            coverage_archived.ArchiveVersion = CoverageArchived.objects.filter(ActiveVersion_id=coverage.ActiveVersion.CoverageId).count() + 1
            coverage_archived.ActiveVersion = coverage.ActiveVersion

        coverage_archived.save()


        return JsonResponse({'message': 'Success'}, status=200)
