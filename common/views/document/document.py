import base64
import os

from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from rest_framework.views import APIView

from common.configs.other.documents_storage import documents_storage
from common.models import Document, DocumentFile, DocumentRelatedItem
from django.contrib.auth.models import User
from common.serializers import DocumentsSerializer, DocumentSerializer



class DocumentAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = User.objects.filter().first()
        if request.data is not None:
            if request.data['document'] is not None:
                # global document_details
                document_tab = request.data['document']
                document = Document()

                if 'documentDetails' in document_tab and document_tab['documentDetails'] is not None:
                    document_details = document_tab['documentDetails']
                    base_party_id = document_details['baseParty']

                    document.BasePartyId_id = base_party_id

                    temp_related_field = [
                        {"db_field": 'BasePartyId_id', "field_label": 'baseParty'},
                        {"db_field": 'DocumentType_id', "field_label": 'documentType'},
                        {"db_field": 'Description1', "field_label": 'description'},
                        {"db_field": 'DocumentIdType_id', "field_label": 'documentIdType'},
                        {"db_field": 'CharDocumentId', "field_label": 'charDocumentId'},
                        {"db_field": 'DocumentStatus_id', "field_label": 'documentStatus'},
                    ]

                    for field in temp_related_field:
                        if "_id" in field['db_field'] and document_details[field['field_label']] is not None:
                            setattr(document, field['db_field'], int(document_details[field['field_label']]))
                        elif "_id" not in field['db_field']:
                            setattr(document, field['db_field'], document_details[field['field_label']])

                    # document.

                    if 'fileInfo' in document_details and document_details['fileInfo'] is not None:
                        document_file = DocumentFile()
                        if isinstance(document_details['fileInfo'], str):
                            document.FileName = document_details['fileName']
                            document.FileType = document_details['fileType']
                            document.FileSize = document_details['fileSize']
                            document.save()

                            document_file.FileName = document_details['fileName']
                            document_file.FileType = document_details['fileType']
                            document_file.FileSize = document_details['fileSize']
                            document_file.DocumentId = document

                            if documents_storage['storage_location'] == 1:
                                document_file.FileObject = document_details['fileInfo']
                                document.StorageLocation = 1
                            elif documents_storage['storage_location'] == 2:
                                document_base64_string = document_details['fileInfo'].split(",")[1]
                                new_file = base64.b64decode(document_base64_string)

                                dir_url = "{}/{}/{}".format(documents_storage['directory_path'], base_party_id,
                                                            document.DocumentId)
                                file_url = "{}/{}/{}/{}".format(documents_storage['directory_path'], base_party_id, document.DocumentId, document_details['fileName'])

                                if not os.path.exists(dir_url):
                                    os.makedirs(dir_url)

                                with open(file_url, 'wb') as file:
                                    file.write(new_file)

                                document.StorageLocation = 2
                                document.FileURL = file_url
                                document_file.FileURL = file_url

                            document_file.save()
                            document.save()

                    if 'relatedItems' in document_tab and document_tab['relatedItems'] is not None:
                        related_items = document_tab['relatedItems']

                        if len(related_items) > 0:
                            for item in related_items:
                                document_related_item = DocumentRelatedItem()
                                document_related_item.DocumentId = document
                                document_related_item.RelatedItemType_id = item.get('relatedItemType', None)
                                document_related_item.RelatedItemId = item.get('relatedItemId', None)
                                document_related_item.save()

                    if 'alertsAndWarnings' in request.data and request.data['alertsAndWarnings'] is not None:
                        alerts_tab = request.data['alertsAndWarnings']

                        if 'alertAndWarningSettings' in alerts_tab and alerts_tab['alertAndWarningSettings'] is not None:
                            alerts_data = alerts_tab['alertAndWarningSettings']

                            temp_related_field = [
                                {"db_field": 'AlertDays', "field_label": 'alertDays', 'second_field_label': 'alert'},
                                {"db_field": 'WarningDays', "field_label": 'alertDays', 'second_field_label': 'warning'},
                                {"db_field": 'AlertDocumentStatus_id', "field_label": 'alertDocumentStatus', 'second_field_label': 'alert'},
                                {"db_field": 'WarningDocumentStatus_id', "field_label": 'alertDocumentStatus', 'second_field_label': 'warning'},
                                {"db_field": 'AlertSource_id', "field_label": 'alertSource', 'second_field_label': 'alert'},
                                {"db_field": 'WarningSource_id', "field_label": 'alertSource', 'second_field_label': 'warning'},
                                {"db_field": 'AlertType_id', "field_label": 'alertType', 'second_field_label': 'alert'},
                                {"db_field": 'WarningType_id', "field_label": 'alertType', 'second_field_label': 'warning'},
                                {"db_field": 'AlertSubType_id', "field_label": 'alertSubType', 'second_field_label': 'alert'},
                                {"db_field": 'WarningSubType_id', "field_label": 'alertSubType', 'second_field_label': 'warning'},
                                {"db_field": 'AlertSeverity_id', "field_label": 'alertSeverity', 'second_field_label': 'alert'},
                                {"db_field": 'WarningSeverity_id', "field_label": 'alertSeverity', 'second_field_label': 'warning'},
                                {"db_field": 'AlertEmailFlag', "field_label": 'alertEmailFlag', 'second_field_label': 'alert'},
                                {"db_field": 'WarningEmailFlag', "field_label": 'alertEmailFlag', 'second_field_label': 'warning'},
                                {"db_field": 'AlertSenderId', "field_label": 'alertSender', 'second_field_label': 'alert'},
                                {"db_field": 'WarningSenderId', "field_label": 'alertSender', 'second_field_label': 'warning'},
                                {"db_field": 'AlertRecipientId', "field_label": 'alertRecipients', 'second_field_label': 'alert'},
                                {"db_field": 'WarningRecipientId', "field_label": 'alertRecipients', 'second_field_label': 'warning'},
                                {"db_field": 'AlertTemplateId', "field_label": 'emailTemplate', 'second_field_label': 'alert'},
                                {"db_field": 'WarningTemplateId', "field_label": 'emailTemplate', 'second_field_label': 'warning'},
                                {"db_field": 'AlertEmailOption_id', "field_label": 'emailOption', 'second_field_label': 'alert'},
                                {"db_field": 'WarningEmailOption_id', "field_label": 'emailOption', 'second_field_label': 'warning'},
                            ]

                            for field in temp_related_field:
                                if "_id" in field['db_field'] and alerts_data[field['field_label']][field['second_field_label']] is not None:
                                    setattr(document, field['db_field'], int(alerts_data[field['field_label']][field['second_field_label']]))
                                elif "_id" not in field['db_field']:
                                    setattr(document, field['db_field'], alerts_data[field['field_label']][field['second_field_label']])

                document.LastUpdatedDate = timezone.now()
                document.LastUpdatedBy = user
                document.InsertDate = timezone.now()
                document.InsertedBy = user
                document.save()



            response = DocumentsSerializer(document, context={"host": request.get_host()}).data

            return JsonResponse(response)

    def put(self, request, *args, **kwargs):
        user = User.objects.filter().first()
        if request.data is not None:
            if request.data['document'] is not None:
                document_tab = request.data['document']
                document = Document.objects.filter(DocumentId=request.data['documentId'])
                if not document.exists():
                    raise Exception('Wrong document id')
                document = document.first()

                if 'documentDetails' in document_tab and document_tab['documentDetails'] is not None:
                    document_details = document_tab['documentDetails']
                    base_party_id = document_details['baseParty']

                    temp_related_field = [
                        {"db_field": 'BasePartyId_id', "field_label": 'baseParty'},
                        {"db_field": 'DocumentType_id', "field_label": 'documentType'},
                        {"db_field": 'Description1', "field_label": 'description'},
                        {"db_field": 'DocumentIdType_id', "field_label": 'documentIdType'},
                        {"db_field": 'CharDocumentId', "field_label": 'charDocumentId'},
                        {"db_field": 'DocumentStatus_id', "field_label": 'documentStatus'},
                    ]

                    for field in temp_related_field:
                        if "_id" in field['db_field'] and document_details[field['field_label']] is not None:
                            setattr(document, field['db_field'], int(document_details[field['field_label']]))
                        elif "_id" not in field['db_field']:
                            setattr(document, field['db_field'], document_details[field['field_label']])

                    # document.

                    if 'relatedItems' in document_tab and document_tab['relatedItems'] is not None:
                        related_items = document_tab['relatedItems']

                        existing_document_related_items = []

                        for item in related_items:
                            if 'temp' in str(item.get('id', None)):
                                document_related_item = DocumentRelatedItem()
                                document_related_item.DocumentId = document
                                document_related_item.RelatedItemType_id = item.get('relatedItemType', None)
                                document_related_item.RelatedItemId = item.get('relatedItemId', None)
                                document_related_item.save()

                                existing_document_related_items.append(document_related_item.DocumentRelatedItemId)
                            elif 'temp' not in str(item.get('id', None)):
                                document_related_item = DocumentRelatedItem.objects.filter(DocumentRelatedItemId=item.get('id', None)).first()
                                # document_related_item.DocumentId = document
                                document_related_item.RelatedItemType_id = item.get('relatedItemType', None)
                                document_related_item.RelatedItemId = item.get('relatedItemId', None)
                                document_related_item.save()

                                existing_document_related_items.append(document_related_item.DocumentRelatedItemId)

                            elif 'temp' not in str(item.get('id', None)) and isinstance(item.get('id', None)) and 'isChange' not in item:
                                existing_document_related_items.append(item.get('id', None))

                        DocumentRelatedItem.objects.filter(DocumentId=document.DocumentId).exclude(DocumentRelatedItem__in=existing_document_related_items).delete()

                    if 'alertsAndWarnings' in request.data and request.data['alertsAndWarnings'] is not None:
                        alerts_tab = request.data['alertsAndWarnings']

                        if 'alertAndWarningSettings' in alerts_tab and alerts_tab['alertAndWarningSettings'] is not None:
                            alerts_data = alerts_tab['alertAndWarningSettings']

                            temp_related_field = [
                                {"db_field": 'AlertDays', "field_label": 'alertDays', 'second_field_label': 'alert'},
                                {"db_field": 'WarningDays', "field_label": 'alertDays', 'second_field_label': 'warning'},
                                {"db_field": 'AlertDocumentStatus_id', "field_label": 'alertDocumentStatus', 'second_field_label': 'alert'},
                                {"db_field": 'WarningDocumentStatus_id', "field_label": 'alertDocumentStatus', 'second_field_label': 'warning'},
                                {"db_field": 'AlertSource_id', "field_label": 'alertSource', 'second_field_label': 'alert'},
                                {"db_field": 'WarningSource_id', "field_label": 'alertSource', 'second_field_label': 'warning'},
                                {"db_field": 'AlertType_id', "field_label": 'alertType', 'second_field_label': 'alert'},
                                {"db_field": 'WarningType_id', "field_label": 'alertType', 'second_field_label': 'warning'},
                                {"db_field": 'AlertSubType_id', "field_label": 'alertSubType', 'second_field_label': 'alert'},
                                {"db_field": 'WarningSubType_id', "field_label": 'alertSubType', 'second_field_label': 'warning'},
                                {"db_field": 'AlertSeverity_id', "field_label": 'alertSeverity', 'second_field_label': 'alert'},
                                {"db_field": 'WarningSeverity_id', "field_label": 'alertSeverity', 'second_field_label': 'warning'},
                                {"db_field": 'AlertEmailFlag', "field_label": 'alertEmailFlag', 'second_field_label': 'alert'},
                                {"db_field": 'WarningEmailFlag', "field_label": 'alertEmailFlag', 'second_field_label': 'warning'},
                                {"db_field": 'AlertSenderId', "field_label": 'alertSender', 'second_field_label': 'alert'},
                                {"db_field": 'WarningSenderId', "field_label": 'alertSender', 'second_field_label': 'warning'},
                                {"db_field": 'AlertRecipientId', "field_label": 'alertRecipients', 'second_field_label': 'alert'},
                                {"db_field": 'WarningRecipientId', "field_label": 'alertRecipients', 'second_field_label': 'warning'},
                                {"db_field": 'AlertTemplateId', "field_label": 'emailTemplate', 'second_field_label': 'alert'},
                                {"db_field": 'WarningTemplateId', "field_label": 'emailTemplate', 'second_field_label': 'warning'},
                                {"db_field": 'AlertEmailOption_id', "field_label": 'emailOption', 'second_field_label': 'alert'},
                                {"db_field": 'WarningEmailOption_id', "field_label": 'emailOption', 'second_field_label': 'warning'},
                            ]

                            for field in temp_related_field:
                                if "_id" in field['db_field'] and alerts_data[field['field_label']][field['second_field_label']] is not None:
                                    setattr(document, field['db_field'], int(alerts_data[field['field_label']][field['second_field_label']]))
                                elif "_id" not in field['db_field']:
                                    setattr(document, field['db_field'], alerts_data[field['field_label']][field['second_field_label']])

                document.LastUpdatedDate = timezone.now()
                document.LastUpdatedBy = user
                document.save()

                if 'fileInfo' in document_details and document_details['fileInfo'] is not None and document_details['fileInfo'] != '':
                    document_file = DocumentFile()
                    if isinstance(document_details['fileInfo'], str):
                        document.BasePartyId_id = base_party_id
                        document.FileName = document_details['fileName']
                        document.FileType = document_details['fileType']
                        document.FileSize = document_details['fileSize']
                        document.save()

                        document_file.FileName = document_details['fileName']
                        document_file.FileType = document_details['fileType']
                        document_file.FileSize = document_details['fileSize']
                        document_file.DocumentId = document

                        if documents_storage['storage_location'] == 1:
                            document_file.FileObject = document_details['fileInfo']
                            document.StorageLocation = 1
                        elif documents_storage['storage_location'] == 2:
                            document_base64_string = document_details['fileInfo'].split(",")[1]
                            new_file = base64.b64decode(document_base64_string)

                            dir_url = "{}/{}/{}".format(documents_storage['directory_path'], base_party_id,
                                                        document.DocumentId)
                            file_url = "{}/{}/{}/{}".format(documents_storage['directory_path'], base_party_id, document.DocumentId, document_details['fileName'])

                            if not os.path.exists(dir_url):
                                os.makedirs(dir_url)

                            with open(file_url, 'wb') as file:
                                file.write(new_file)

                            document.StorageLocation = 2
                            document.FileURL = file_url
                            document_file.FileURL = file_url

                        document_file.save()
                        document.save()
                elif \
                    'fileInfo' in document_details and document_details['fileInfo'] is not None and document_details['fileInfo'] == '' and \
                    'fileName' in document_details and document_details['fileName'] is not None and document_details['fileName'] == '':
                    DocumentFile.objects.filter(DocumentId=document.DocumentId).delete()
                    document.FileName = None
                    document.FileSize = None
                    document.FileType = None
                    document.FileURL = None
                    document.save()


            response = DocumentsSerializer(document, context={"host": request.get_host()}).data

            return JsonResponse(response)

    def get(self, request, **kwargs):
        document_id = kwargs['id']
        document_query_set = Document.objects.filter(DocumentId=document_id)
        if not document_query_set.exists():
            return HttpResponse(content='Document with {}id does not exist'.format(document_id), status=400)

        document = document_query_set.first()

        return JsonResponse(DocumentSerializer(document, context={"host": request.get_host()}).data)

    def delete(self, request, *args, **kwargs):
        document_query_set = Document.objects.filter(DocumentId=kwargs.get('id'))
        if not document_query_set.exists():
            return HttpResponse(content='Document with {}id does not exist'.format(kwargs.get('id')), status=400)

        document_query_set.delete()

        return JsonResponse({'message': 'Success'}, status=200)
