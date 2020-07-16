from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models import RelatedParty
from common.serializers import RelatedPartiesOwnersSerializer, RelatedPartyOwnerSerializer

related_party_details_fields = [
    {'db_field': 'BaseParty1Id_id', 'field_label': 'baseEntity'},
    {'db_field': 'RelationType_id', 'field_label': 'relationType'},
    {'db_field': 'BaseParty2Id_id', 'field_label': 'relatedParty'},
    {'db_field': 'PercentOwnership', 'field_label': 'percentOwnership'},
    {'db_field': 'PercentVoting', 'field_label': 'percentVoting'},
    {'db_field': 'SharesCount', 'field_label': 'sharesCount'},
    {'db_field': 'SharesValue', 'field_label': 'sharesValue'},
    {'db_field': 'StartDate', 'field_label': 'startDate'},
    {'db_field': 'EndDate', 'field_label': 'endDate'},
    {'db_field': 'Comment', 'field_label': 'comment'},
    {'db_field': 'SharesCount', 'field_label': 'sharesCount'},
    {'db_field': 'IsControllingOwner', 'field_label': 'isControllingOwner'},
    {'db_field': 'LinkFinancials', 'field_label': 'linkFinancials'},
    {'db_field': 'LinkBankingInfo', 'field_label': 'linkBankingInfo'},
    {'db_field': 'LinkApplications', 'field_label': 'linkApplications'},
]


class RelatedPartyAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if request.data is None:
            return Response('Data is missing', status=400)

        related_party = RelatedParty()

        if 'details' in request.data:
            details = request.data.get('details', {})

            for field in related_party_details_fields:
                if '_id' in field['db_field'] and field['field_label'] in details and details[field['field_label']] is not None:
                    setattr(related_party, field['db_field'], int(details[field['field_label']]))
                elif '_id' not in field['db_field'] and field['field_label'] in details and details[field['field_label']] is not None:
                    setattr(related_party, field['db_field'], details[field['field_label']])

        related_party.save()

        return JsonResponse(RelatedPartiesOwnersSerializer(related_party).data)

    def put(self, request, *args, **kwargs):
        if request.data is None:
            return Response('Data is missing', status=400)

        if 'relatedPartyId' not in request.data or request.data('relatedPartyId', None) is None:
            return Response('Related Party id is missing', status=400)

        related_party_id = request.data.get('relatedPartyId')
        related_party_query_set = RelatedParty.objects.filter(RelatedPartyId=related_party_id)

        if not related_party_query_set.exists():
            return HttpResponse(content='Related Party with {}id does not exist'.format(related_party_id), status=400)

        related_party = related_party_query_set.first()

        if 'details' in request.data:
            details = request.data.get('details', {})

            for field in related_party_details_fields:
                if '_id' in field['db_field'] and field['field_label'] in details and details[field['field_label']] is not None:
                    setattr(related_party, field['db_field'], int(details[field['field_label']]))
                elif '_id' not in field['db_field'] and field['field_label'] in details and details[field['field_label']] is not None:
                    setattr(related_party, field['db_field'], details[field['field_label']])

        related_party.save()

        return JsonResponse(RelatedPartiesOwnersSerializer(related_party).data)

    def get(self, request, **kwargs):
        related_party_id = kwargs.get('id')
        related_party_query_set = RelatedParty.objects.filter(RelatedPartyId=related_party_id)
        if not related_party_query_set.exists():
            return HttpResponse(content='Related Party with {}id does not exist'.format(related_party_id), status=400)

        related_party = related_party_query_set.first()

        return JsonResponse(RelatedPartyOwnerSerializer(related_party).data)


    def delete(self, request, *args, **kwargs):
        related_party_query_set = RelatedParty.objects.filter(RelatedPartyId=kwargs.get('id'))
        if not related_party_query_set.exists():
            return HttpResponse(content='Related Party with {}id does not exist'.format(kwargs.get('id')), status=400)

        related_party_query_set.delete()

        return JsonResponse({'message': 'Success'}, status=200)
