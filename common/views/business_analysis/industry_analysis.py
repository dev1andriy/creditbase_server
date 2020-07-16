from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models import IndustryAnalysis
from common.serializers import IndustryAnalysisSerializer, IndustryAnalyzesSerializer

industry_analysis_fields = [
    {'db_field': 'Industry_id', 'field_label': 'industry'},
    {'db_field': 'BasePartyId_id', 'field_label': 'baseParty'},
    {'db_field': 'ProductServiceSold', 'field_label': 'productServiceSold'},
    {'db_field': 'RevenueContribution', 'field_label': 'revenueContribution'},
    {'db_field': 'PercentTotalRevenue', 'field_label': 'percentTotalRevenue'},
    {'db_field': 'PercentMarketShare', 'field_label': 'percentMarketShare'},
    {'db_field': 'GrowthRate', 'field_label': 'growthRate'},
    {'db_field': 'BuyerPower_id', 'field_label': 'buyerPower'},
    {'db_field': 'SupplierPower_id', 'field_label': 'supplierPower'},
    {'db_field': 'NewEntrantThreat_id', 'field_label': 'newEntrantThreat'},
    {'db_field': 'SubstitutionThreat_id', 'field_label': 'substitutionThreat'},
    {'db_field': 'CompetitiveRivalry_id', 'field_label': 'competitiveRivalry'},
    {'db_field': 'StartDate', 'field_label': 'startDate'},
    {'db_field': 'EndDate', 'field_label': 'endDate'},
    {'db_field': 'Comment', 'field_label': 'comment'},
    {'db_field': 'IsPrimaryRevenueStream', 'field_label': 'isPrimaryRevenueStream'},
]


class IndustryAnalysisAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if request.data is None:
            return Response('Data is missing', status=400)

        industry_analysis = IndustryAnalysis()

        for field in industry_analysis_fields:
            if '_id' in field['db_field'] and field['field_label'] in request.data and request.data[field['field_label']] is not None:
                setattr(industry_analysis, field['db_field'], int(request.data[field['field_label']]))
            elif '_id' not in field['db_field'] and field['field_label'] in request.data and request.data[field['field_label']] is not None:
                setattr(industry_analysis, field['db_field'], request.data[field['field_label']])

        industry_analysis.save()

        return JsonResponse(IndustryAnalyzesSerializer(industry_analysis).data)

    def put(self, request, *args, **kwargs):
        if request.data is None:
            return Response('Data is missing', status=400)

        if 'industryAnalysisId' not in request.data or request.data('industryAnalysisId', None) is None:
            return Response('Industry Analysis id is missing', status=400)

        industry_analysis_id = request.data.get('industryAnalysisId')
        industry_analysis_query_set = IndustryAnalysis.objects.filter(IndustryAnalysisId=industry_analysis_id)

        if not industry_analysis_query_set.exists():
            return HttpResponse(content='Industry Analysis with {}id does not exist'.format(industry_analysis_id), status=400)

        industry_analysis = industry_analysis_query_set.first()

        for field in industry_analysis_fields:
            if '_id' in field['db_field'] and field['field_label'] in request.data and request.data[field['field_label']] is not None:
                setattr(industry_analysis, field['db_field'], int(request.data[field['field_label']]))
            elif '_id' not in field['db_field'] and field['field_label'] in request.data and request.data[field['field_label']] is not None:
                setattr(industry_analysis, field['db_field'], request.data[field['field_label']])

        industry_analysis.save()

        return JsonResponse(IndustryAnalyzesSerializer(industry_analysis).data)

    def get(self, request, **kwargs):
        industry_analysis_id = kwargs['id']
        industry_analysis_query_set = IndustryAnalysis.objects.filter(IndustryAnalysisId=industry_analysis_id)
        if not industry_analysis_query_set.exists():
            return HttpResponse(content='Industry Analysis with {}id does not exist'.format(industry_analysis_id), status=400)

        industry_analysis = industry_analysis_query_set.first()

        return JsonResponse(IndustryAnalysisSerializer(industry_analysis).data)

    def delete(self, request, *args, **kwargs):
        industry_analysis_query_set = IndustryAnalysis.objects.filter(IndustryAnalysisId=kwargs.get('id'))
        if not industry_analysis_query_set.exists():
            return HttpResponse(content='Industry Analysis with {}id does not exist'.format(kwargs.get('id')), status=400)

        industry_analysis_query_set.delete()

        return JsonResponse({'message': 'Success'}, status=200)
