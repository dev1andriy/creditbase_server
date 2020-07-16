from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView

from common.models import Communication
from common.serializers import CommunicationsSerializer, CommunicationSerializer

email_fields = [
    {'db_field': 'AddressFrom', 'field_label': 'from'},
    {'db_field': 'AddressTo', 'field_label': 'to'},
    {'db_field': 'AddressCC', 'field_label': 'CC'},
    {'db_field': 'BasePartyId_id', 'field_label': 'regarding'},
    {'db_field': 'Subject', 'field_label': 'subject'},
    {'db_field': 'Body', 'field_label': 'emailBody'},
]


class EmailAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if request.data is None:
            return HttpResponse('Data is missing', status=400)

        communication = Communication()

        if 'email' in request.data:
            email = request.data.get('email', {})


            for field in email_fields:
                if '_id' in field['db_field'] and field['field_label'] in email and email[field['field_label']] is not None:
                    setattr(communication, field['db_field'], int(email[field['field_label']]))
                elif '_id' not in field['db_field'] and field['field_label'] in email and email[field['field_label']] is not None:
                    setattr(communication, field['db_field'], email[field['field_label']])

            communication.save()

            return JsonResponse(CommunicationsSerializer(communication).data)


    def put(self, request, *args, **kwargs):
        if request.data is None:
            return HttpResponse('Data is missing', status=400)

        if 'communicationId' not in request.data or request.data('communicationId', None) is None:
            return HttpResponse('Communication id is missing', status=400)

        communication_id = request.data.get('communicationId')
        communication_query_set = Communication.objects.filter(CommucationId=communication_id)

        if not communication_query_set.exists():
            return HttpResponse(content='Communication with {}id does not exist'.format(communication_id), status=400)

        communication = communication_query_set.first()

        if 'email' in request.data:
            email = request.data.get('email', {})

            for field in email_fields:
                if '_id' in field['db_field'] and field['field_label'] in email and email[field['field_label']] is not None:
                    setattr(communication, field['db_field'], int(email[field['field_label']]))
                elif '_id' not in field['db_field'] and field['field_label'] in email and email[field['field_label']] is not None:
                    setattr(communication, field['db_field'], email[field['field_label']])

            communication.save()

            return JsonResponse(CommunicationsSerializer(communication).data)

    def get(self, request, **kwargs):
        communication_id = kwargs['id']
        email_query_set = Communication.objects.filter(CommunicationId=communication_id)
        if not email_query_set.exists():
            return HttpResponse(content='Email with {}id does not exist'.format(communication_id), status=400)

        email = email_query_set.first()

        return JsonResponse(CommunicationSerializer(email).data)


    def delete(self, request, *args, **kwargs):
        email_query_set = Communication.objects.filter(CommunicationId=kwargs.get('id'))
        if not email_query_set.exists():
            return HttpResponse(content='Email with {}id does not exist'.format(kwargs.get('id')), status=400)

        email_query_set.delete()

        return JsonResponse({'message': 'Success'}, status=200)
