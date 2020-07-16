from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from rest_framework.views import APIView
from main.common.camel_case_parser import CamelCaseParser
from django.utils import timezone
from common.configs.views.credit_application import *
from common.models.credit_application import *
from common.models.other.note import Note
from common.models.related_party import RelatedParty
from django.db.models import Q
from django.contrib.auth.models import User
from common.models.document import *
from common.utils.credit_application_sections import generate_credit_application_sections_statuses
from common.utils.checklists_data_by_tab_id import generate_checklists_data_by_tab_id
from common.configs.other.documents_storage import documents_storage
from common.serializers import CreditApplicationNotesSerializer, CreditApplicationGeneralSerializer, CreditApplicationStatusesSerializer, CreditApplicationsSerializer, CreditApplicationSerializer

import base64
import os


class CreditApplicationsAPIView(APIView):
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
            main_credit_applications = CreditApplication.objects.filter(BasePartyId_id=kwargs['id']).order_by('-CreditApplicationId')
            related_credit_applications = CreditApplication.objects.filter(BasePartyId_id__in=base_party_ids).exclude(BasePartyId_id=kwargs['id']).order_by('-CreditApplicationId')

            response_data = CreditApplicationsSerializer(main_credit_applications, many=True).data + CreditApplicationsSerializer(related_credit_applications, many=True).data
        else:
            base_party = None
            credit_applications = CreditApplication.objects.all()
            response_data = CreditApplicationsSerializer(credit_applications, many=True).data

        base_party_id = base_party.BasePartyId if base_party is not None else None

        response = {
            "data": CamelCaseParser.to_camel_case_array(response_data),
            "config": generate_config(False, None, base_party_id)
        }

        return JsonResponse(response)


class CreditApplicationAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if request.data is None:
            raise Exception("Wrong input data")

        if request.data is not None:
            user = User.objects.filter().first()

            if "general" in request.data:
                general = request.data["general"]

                if "applicationHighlights" in general:
                    application_highlights = general['applicationHighlights']

                    if 'baseParty' not in application_highlights:
                        raise Exception('Base Party is required')
                    base_party_id = int(application_highlights['baseParty'])

                    credit_application = CreditApplication()

                    temp_related_field = [
                        {"db_field": 'BasePartyId_id', "field_label": 'baseParty'},
                        {"db_field": 'ApplicationSource_id', "field_label": 'applicationSource'},
                        {"db_field": 'ApplicationType_id', "field_label": 'applicationType'},
                        {"db_field": 'ApplicationStatus_id', "field_label": 'applicationStatus'},
                        {"db_field": 'WorkflowProcess_id', "field_label": 'workflowProcess'},
                        {"db_field": 'DecisionType_id', "field_label": 'decisionType'},
                        {"db_field": 'DeclineReason_id', "field_label": 'declineReason'},
                        {"db_field": 'ApplicationPriority_id', "field_label": 'applicationPriority'},
                        {"db_field": 'FinancialInstitution_id', "field_label": 'financialInstitution'},
                        {"db_field": 'BusinessUnit_id', "field_label": 'businessUnit'},
                        {"db_field": 'DecisionExpiryDate', "field_label": 'expiryDate'},
                        {"db_field": 'DecisionNextReviewDate', "field_label": 'nextReviewDate'},
                        {"db_field": 'ReceivedDate', "field_label": 'dateReceived'},
                        {"db_field": 'LastReviewDate', "field_label": 'lastReviewedDate'},
                        {"db_field": 'RequiredAuthorityLevel_id', "field_label": 'requiredAuthorityLevel'},
                        {"db_field": 'ProductsApplicable', "field_label": 'productsApplicable'},
                        {"db_field": 'PurposesApplicable', "field_label": 'purposesApplicable'},
                    ]

                    for field in temp_related_field:
                        try:
                            if "_id" in field['db_field']:
                                setattr(credit_application, field['db_field'], int(application_highlights[field['field_label']]))
                            elif "_id" not in field['db_field']:
                                setattr(credit_application, field['db_field'], application_highlights[field['field_label']])
                        except:
                            pass

                    profile_type = str(credit_application.BasePartyId.ProfileType.ProfileTypeId)
                    application_type = str(credit_application.ApplicationType.ApplicationTypeId)
                    products_applicable = credit_application.ProductsApplicable
                    purposes_applicable = credit_application.PurposesApplicable
                    # collateral_selection = ""

                    application_templates = ApplicationTemplate.objects.filter(ProfileTypes__contains=profile_type,
                                                                               ApplicationTypes__contains=application_type,
                                                                               ProductTypesApplicable__contains=products_applicable,
                                                                               ApplicationPurposes__contains=purposes_applicable)

                    workflow_processes = WorkflowProcess.objects.filter(ProfileTypes__contains=profile_type,
                                                                        ApplicationTypes__contains=application_type,
                                                                        ProductTypesApplicable__contains=products_applicable,
                                                                        ApplicationPurposes__contains=purposes_applicable)

                    if application_templates.exists():
                        credit_application.ApplicationTemplate = application_templates.first()

                    if workflow_processes.exists():
                        credit_application.WorkflowProcess = workflow_processes.first()

                    credit_application.DecisionDate = timezone.now()
                    credit_application.InsertDate = timezone.now()
                    credit_application.LastUpdatedDate = timezone.now()
                    credit_application.LastWFLStepDate = timezone.now()

                    credit_application.save()

                    credit_application_id = credit_application.CreditApplicationId

                if 'applicationStaff' in general and len(general['applicationStaff']) > 0:
                    temp_staff_fields = [
                        {"db_field": 'IsPrimaryRelatedStaff', "field_label": 'primaryContact'},
                        {"db_field": 'RelationType_id', "field_label": 'relationType'},
                        {"db_field": 'StaffId_id', "field_label": 'relationshipStaffName'},
                    ]
                    for staff in general['applicationStaff']:
                        if 'id' in staff and 'temp' in str(staff['id']):
                            new_staff = CreditApplicationStaff()
                            new_staff.CreditApplicationId_id = credit_application.CreditApplicationId

                            for field in temp_staff_fields:
                                try:
                                    if staff[field['field_label']] is not None:
                                        setattr(new_staff, field['db_field'], int(staff[field['field_label']]) if '_id' in field['db_field'] else staff[field['field_label']])
                                except:
                                    pass

                            # new_contact.InsertedBy = request.user
                            new_staff.InsertDate = timezone.now()
                            # new_contact.LastUpdatedBy = request.user
                            new_staff.LastUpdatedDate = timezone.now()
                            new_staff.save()
                        elif 'id' in staff and 'temp' not in str(staff['id']):
                            existing_staff = CreditApplicationStaff.objects.get(id=staff['id'])
                            for field in temp_staff_fields:
                                try:
                                    if staff[field['field_label']] is not None:
                                        setattr(existing_staff, field['db_field'],int(staff[field['field_label']]) if '_id' in field['db_field'] else staff[field['field_label']])
                                except:
                                    pass
                            # existing_contact.LastUpdatedBy = request.user
                            existing_staff.LastUpdatedDate = timezone.now()
                            existing_staff.save()

            if 'checklists' in request.data:
                process_checklists_data(request.data['checklists'], base_party_id, credit_application_id, user)

            if 'notes' in request.data:
                tabs = request.data['notes']
                for tab_key in tabs:
                    tab = tabs[tab_key]
                    for note_level_key in tab:
                        note_level_key_int = int(note_level_key)
                        try:
                            if note_level_key_int == 1:
                                note = Note.objects.get(BasePartyId=base_party_id, NoteLevel=note_level_key_int, Tab=tab_key, NoteKey1=base_party_id)
                            elif note_level_key_int == 2:
                                note = Note.objects.get(BasePartyId=base_party_id, NoteLevel=note_level_key_int, Tab=tab_key, NoteKey1=credit_application_id)

                        except:
                            note = Note()
                            note.BasePartyId_id = base_party_id
                            note.NoteLevel = note_level_key_int
                            note.Tab = tab_key
                            if note_level_key_int == 1:
                                note.NoteKey1 = base_party_id
                            elif note_level_key_int == 2:
                                note.NoteKey1 = credit_application_id

                        note.Note = tab[note_level_key]
                        note.save()


            banking_summary_fields = ['ExistingCommitment', 'ProposedExposure', 'ExistingExposure', 'ProposedIncrease',
                                      'ProposedMarketValue', 'ProposedCoverageByMV', 'ProposedForcedSaleValue',
                                      'ProposedCoverageByFSV', 'ProposedDiscountedValue', 'ProposedCoverageByDV',
                                      'ProposedLienValue', 'ProposedCoverageByLV']
            banking_summary = CreditApplicationBankingSummary()
            banking_summary.CreditApplicationId = credit_application
            for field in banking_summary_fields:
                setattr(banking_summary, field, 100)
            banking_summary.save()

            response = CamelCaseParser.to_camel_case_single(CreditApplicationsSerializer(credit_application).data)

            generate_credit_application_sections_statuses(CreditApplicationSerializer(credit_application, context={"get_statuses": False}).data)

            return JsonResponse(response)

    def put(self, request, *args, **kwargs):
        if request.data is not None:
            user = User.objects.filter(pk=1).first()
            if 'creditApplicationId' in request.data:
                credit_application_id = int(request.data['creditApplicationId'])
                credit_application = CreditApplication.objects.get(CreditApplicationId=credit_application_id)
            else:
                raise Exception('There is no credit application id')

            if 'basePartyId' in request.data:
                base_party_id = int(request.data['basePartyId'])
            else:
                raise Exception('There is no base party id')

            if 'general' in request.data:
                general = request.data['general']

                if 'applicationHighlights' in general:
                    application_highlights = general['applicationHighlights']

                    temp_related_field = [
                        # {"db_field": 'BasePartyId_id', "field_label": 'baseParty'},
                        {"db_field": 'ApplicationSource_id', "field_label": 'applicationSource'},
                        {"db_field": 'ApplicationStatus_id', "field_label": 'applicationStatus'},
                        {"db_field": 'DecisionType_id', "field_label": 'decisionType'},
                        {"db_field": 'DeclineReason_id', "field_label": 'declineReason'},
                        {"db_field": 'ApplicationPriority_id', "field_label": 'applicationPriority'},
                        {"db_field": 'BusinessUnit_id', "field_label": 'businessUnit'},
                        {"db_field": 'FinancialInstitution_id', "field_label": 'financialInstitution'},
                        {"db_field": 'DecisionExpiryDate', "field_label": 'expiryDate'},
                        {"db_field": 'DecisionNextReviewDate', "field_label": 'nextReviewDate'},
                        {"db_field": 'ReceivedDate', "field_label": 'dateReceived'},
                        {"db_field": 'LastReviewDate', "field_label": 'lastReviewedDate'},
                        {"db_field": 'RequiredAuthorityLevel_id', "field_label": 'requiredAuthorityLevel'},
                    ]

                    for field in temp_related_field:
                        if application_highlights[field['field_label']] is not None:
                            if "_id" in field['db_field']:
                                setattr(credit_application, field['db_field'],
                                        int(application_highlights[field['field_label']]))
                            elif "_id" not in field['db_field']:
                                setattr(credit_application,
                                        field['db_field'], application_highlights[field['field_label']])

                    credit_application.LastUpdatedDate = timezone.now()
                    credit_application.save()

                if 'applicationStaff' in general and len(general['applicationStaff']) > 0:
                    temp_staff_fields = [
                        {"db_field": 'IsPrimaryRelatedStaff', "field_label": 'primaryContact'},
                        {"db_field": 'RelationType_id', "field_label": 'relationType'},
                        {"db_field": 'StaffId_id', "field_label": 'relationshipStaffName'},
                    ]
                    for staff in general['applicationStaff']:
                        if 'id' in staff and 'temp' in str(staff['id']):
                            new_staff = CreditApplicationStaff()
                            new_staff.CreditApplicationId_id = credit_application.CreditApplicationId

                            for field in temp_staff_fields:
                                try:
                                    if staff[field['field_label']] is not None:
                                        setattr(new_staff, field['db_field'], int(staff[field['field_label']]) if '_id' in field['db_field'] else staff[field['field_label']])
                                except:
                                    pass

                            # new_contact.InsertedBy = request.user
                            new_staff.InsertDate = timezone.now()
                            # new_contact.LastUpdatedBy = request.user
                            new_staff.LastUpdatedDate = timezone.now()
                            new_staff.save()
                        elif 'id' in staff and 'temp' not in str(staff['id']):
                            existing_staff = CreditApplicationStaff.objects.get(id=staff['id'])
                            for field in temp_staff_fields:
                                try:
                                    if staff[field['field_label']] is not None:
                                        setattr(existing_staff, field['db_field'],
                                            int(staff[field['field_label']]) if '_id' in field['db_field'] else staff[
                                                field['field_label']])
                                except:
                                    pass
                            # existing_contact.LastUpdatedBy = request.user
                            existing_staff.LastUpdatedDate = timezone.now()
                            existing_staff.save()

            if 'checklists' in request.data:
                process_checklists_data(request.data['checklists'], base_party_id, credit_application_id, user)

            if 'notes' in request.data:
                tabs = request.data['notes']
                for tab_key in tabs:
                    tab = tabs[tab_key]
                    for note_level_key in tab:
                        note_level_key_int = int(note_level_key)
                        try:
                            if note_level_key_int == 1:
                                note = Note.objects.get(BasePartyId=base_party_id, NoteLevel=note_level_key_int, Tab=tab_key, NoteKey1=base_party_id)
                            elif note_level_key_int == 2:
                                note = Note.objects.get(BasePartyId=base_party_id, NoteLevel=note_level_key_int, Tab=tab_key, NoteKey1=credit_application_id)

                        except:
                            note = Note()
                            note.BasePartyId_id = base_party_id
                            note.NoteLevel = note_level_key_int
                            note.Tab = tab_key
                            if note_level_key_int == 1:
                                note.NoteKey1 = base_party_id
                            elif note_level_key_int == 2:
                                note.NoteKey1 = credit_application_id

                        note.Note = tab[note_level_key]
                        note.save()

            response = CamelCaseParser.to_camel_case_single(CreditApplicationsSerializer(credit_application).data)

            generate_credit_application_sections_statuses(CreditApplicationSerializer(credit_application, context={"get_statuses": False}).data)

            return JsonResponse(response)

    def get(self, request, **kwargs):
        credit_application_id = kwargs['id']
        try:
            credit_application = CreditApplication.objects.get(CreditApplicationId=credit_application_id)
        except ObjectDoesNotExist:
            return HttpResponseNotFound('Credit Application with {}id doesn\'t exist'.format(credit_application_id))

        response = CreditApplicationSerializer(credit_application, context={"host": request.get_host(), "get_statuses": True}).data

        response = {
            "data": response,
            "config": generate_config(edit=True, credit_application_id=credit_application.CreditApplicationId, base_party_id=credit_application.BasePartyId_id)
        }

        return JsonResponse(response)

    def delete(self, request, *args, **kwargs):
        try:
            CreditApplication.objects.get(CreditApplicationId=kwargs['id']).delete()
        except ObjectDoesNotExist:
            return HttpResponseNotFound(content='Credit Application with {}id does not exist'.format(kwargs['id']))

        return HttpResponse('200')


class CreditApplicationArchiveAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs.keys():
            base_party = BaseParty.objects.filter(BasePartyId=kwargs['id']).first()
            base_party_ids = [kwargs['id']]
            related_parties = RelatedParty.objects.filter((Q(BaseParty1Id=base_party) | Q(BaseParty2Id=base_party)),
                                                          (Q(EndDate=None) | Q(EndDate__gte=timezone.now())))
            for party in related_parties:
                if party.BaseParty1Id not in base_party_ids:
                    base_party_ids.append(party.BaseParty1Id)
                if party.BaseParty2Id not in base_party_ids:
                    base_party_ids.append(party.BaseParty2Id)
            main_credit_applications = CreditApplication.objects.filter(BasePartyId_id=kwargs['id'], IsArchived=True).order_by('-CreditApplicationId')
            related_credit_applications = CreditApplication.objects.filter(BasePartyId_id__in=base_party_ids, IsArchived=True).exclude(BasePartyId_id=kwargs['id']).order_by('-CreditApplicationId')

            response_data = CreditApplicationsSerializer(main_credit_applications, many=True).data + CreditApplicationsSerializer(related_credit_applications, many=True).data
        else:
            base_party = None
            credit_applications = CreditApplication.objects.all()
            response_data = CreditApplicationsSerializer(credit_applications, many=True).data

        base_party_id = base_party.BasePartyId if base_party is not None else None

        response = {
            "data": CamelCaseParser.to_camel_case_array(response_data),
            "config": generate_config(False, None, base_party_id)
        }

        return JsonResponse(response)

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            CreditApplication.objects.filter(CreditApplicationId__in=request.data).update(IsArchived=True, ArchivedDate=datetime.now())
            return HttpResponse(200)
        return HttpResponseBadRequest('Wrong input data')


class CreditApplicationUnArchiveAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs.keys():
            base_party = BaseParty.objects.filter(BasePartyId=kwargs['id']).first()
            base_party_ids = [kwargs['id']]
            related_parties = RelatedParty.objects.filter((Q(BaseParty1Id=base_party) | Q(BaseParty2Id=base_party)),
                                                          (Q(EndDate=None) | Q(EndDate__gte=timezone.now())))
            for party in related_parties:
                if party.BaseParty1Id not in base_party_ids:
                    base_party_ids.append(party.BaseParty1Id)
                if party.BaseParty2Id not in base_party_ids:
                    base_party_ids.append(party.BaseParty2Id)
            main_credit_applications = CreditApplication.objects.filter(BasePartyId_id=kwargs['id'], IsArchived=False).order_by('-CreditApplicationId')
            related_credit_applications = CreditApplication.objects.filter(BasePartyId_id__in=base_party_ids, IsArchived=False).exclude(BasePartyId_id=kwargs['id']).order_by('-CreditApplicationId')

            response_data = CreditApplicationsSerializer(main_credit_applications, many=True).data + CreditApplicationsSerializer(related_credit_applications, many=True).data
        else:
            base_party = None
            credit_applications = CreditApplication.objects.all()
            response_data = CreditApplicationsSerializer(credit_applications, many=True).data

        base_party_id = base_party.BasePartyId if base_party is not None else None

        response = {
            "data": CamelCaseParser.to_camel_case_array(response_data),
            "config": generate_config(False, None, base_party_id)
        }

        return JsonResponse(response)

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            CreditApplication.objects.filter(CreditApplicationId__in=request.data, DecisionDate=None).update(IsArchived=False)
            return HttpResponse(200)
        return HttpResponseBadRequest('Wrong input data')


class CreditApplicationStatusesAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            credit_application = CreditApplication.objects.get(CreditApplicationId=kwargs.get('id'))
        except ObjectDoesNotExist:
            return HttpResponseNotFound('Credit Application with {}id doesn\'t exist'.format(kwargs.get('id')))

        response = CreditApplicationStatusesSerializer(credit_application).data

        return JsonResponse(response)


class CreditApplicationGeneralAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            credit_application = CreditApplication.objects.get(CreditApplicationId=kwargs.get('id'))
        except ObjectDoesNotExist:
            return HttpResponseNotFound('Credit Application with {}id doesn\'t exist'.format(kwargs.get('id')))

        response = CreditApplicationGeneralSerializer(credit_application).data

        return JsonResponse(response)


class CreditApplicationChecklistsAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            credit_application = CreditApplication.objects.get(CreditApplicationId=kwargs.get('id'))
        except ObjectDoesNotExist:
            return HttpResponseNotFound('Credit Application with {}id doesn\'t exist'.format(kwargs.get('id')))

        response = generate_checklists_data_by_tab_id(credit_application.CreditApplicationId, kwargs.get('tab_id'), request.get_host())

        return JsonResponse({"checklists": response})


class CreditApplicationNotesAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            credit_application = CreditApplication.objects.get(CreditApplicationId=kwargs.get('id'))
        except ObjectDoesNotExist:
            return HttpResponseNotFound('Credit Application with {}id doesn\'t exist'.format(kwargs.get('id')))

        response = CreditApplicationNotesSerializer(credit_application).data

        return JsonResponse(response)


class CreditApplicationConfigAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            credit_application = CreditApplication.objects.get(CreditApplicationId=kwargs.get('id'))
        except ObjectDoesNotExist:
            return HttpResponseNotFound('Credit Application with {}id doesn\'t exist'.format(kwargs.get('id')))

        response = generate_config(edit=True, credit_application_id=credit_application.CreditApplicationId, base_party_id=credit_application.BasePartyId_id)

        return JsonResponse(response)


def process_checklists_data(checklists, base_party_id, credit_application_id, user):
    affected_templates = []
    affected_questions = []
    for tab in checklists:
        for key in checklists[tab]:
            if key == "results":
                for template_name in checklists[tab][key]:
                    for template_result in checklists[tab][key][template_name]:
                        result = ChecklistResult.objects.filter(ChecklistResultId=template_result['id']).first()
                        result.FinalizedFlag = template_result['finalized']
                        result.Comment = template_result['comment']
                        result.save()
                continue

            if key not in affected_questions:
                affected_questions.append(key)

            if 'checklistAnswers' in checklists[tab][key]:
                if ChecklistAnswer.objects.filter(QuestionId=int(key), CreditApplicationId=credit_application_id).exists():
                    checklist_answer = ChecklistAnswer.objects.get(QuestionId=int(key), CreditApplicationId=credit_application_id)

                    array_index = 0
                    for i in range(1, 5):
                        if getattr(checklist_answer.TemplateId, 'Response{}Label'.format(i)) is not None and getattr(checklist_answer.TemplateId, 'Response{}Role'.format(i)) is not None:
                            answer = checklists[tab][key]['checklistAnswers'][array_index]

                            if answer['response'] is None or int(answer['response']) == 0:
                                array_index = array_index + 1
                                continue

                            checklist_response = ChecklistResponse.objects.filter(
                                ResponseId=int(answer['response'])).first()

                            if answer['response'] is not None and answer['response'] != 0 and getattr(checklist_answer, 'Response{}Id_id'.format(i)) != answer['response']:
                                checklist_answer.LastUpdatedDate = timezone.now()

                            setattr(checklist_answer, 'Response{}Id_id'.format(i), answer['response'])
                            setattr(checklist_answer, 'Response{}Score'.format(i), checklist_response.Points)
                            array_index = array_index + 1
                    checklist_answer.save()

                    if checklist_answer.TemplateId_id not in affected_templates:
                        affected_templates.append(checklist_answer.TemplateId_id)
                else:
                    question = ChecklistQuestion.objects.filter(QuestionId=int(key)).first()

                    new_checklist_answer = ChecklistAnswer()
                    new_checklist_answer.BasePartyId_id = base_party_id
                    new_checklist_answer.CreditApplicationId_id = credit_application_id
                    new_checklist_answer.QuestionId_id = int(key)
                    new_checklist_answer.TemplateId = question.TemplateId
                    new_checklist_answer.InsertDate = timezone.now()

                    array_index = 0
                    for i in range(1, 5):
                        if getattr(question.TemplateId, 'Response{}Label'.format(i)) is not None and getattr(
                                question.TemplateId, 'Response{}Role'.format(i)) is not None:
                            answer = checklists[tab][key]['checklistAnswers'][array_index]

                            if answer['response'] is None or int(answer['response']) == 0:
                                array_index = array_index + 1
                                continue

                            checklist_response = ChecklistResponse.objects.filter(
                                ResponseId=int(answer['response'])).first()

                            if answer['response'] is not None and answer['response'] != 0 and getattr(new_checklist_answer, 'Response{}Id_id'.format(i)) != answer['response']:
                                new_checklist_answer.LastUpdatedDate = timezone.now()

                            setattr(new_checklist_answer, 'Response{}Id_id'.format(i), answer['response'])
                            setattr(new_checklist_answer, 'Response{}Score'.format(i), checklist_response.Points)
                            array_index = array_index + 1
                        new_checklist_answer.save()

                    if question.TemplateId_id not in affected_templates:
                        affected_templates.append(question.TemplateId_id)

            if 'comments' in checklists[tab][key] and checklists[tab][key]['comments'] is not None:
                comments = checklists[tab][key]['comments']
                ChecklistComment.objects.filter(CreditApplicationId=credit_application_id, QuestionId=int(key)).delete()

                for comment in comments:
                    new_comment = ChecklistComment()
                    new_comment.BasePartyId_id = base_party_id
                    new_comment.CreditApplicationId_id = credit_application_id
                    new_comment.QuestionId_id = int(key)
                    new_comment.Comment = comment['text']
                    new_comment.InsertDate = comment['date']
                    new_comment.save()
                    if 'answers' in comment and len(comment['answers']) > 0:
                        for sub_comment in comment['answers']:
                            new_sub_comment = ChecklistComment()
                            new_sub_comment.BasePartyId_id = base_party_id
                            new_sub_comment.CreditApplicationId_id = credit_application_id
                            new_sub_comment.QuestionId_id = int(key)
                            new_sub_comment.Comment = sub_comment['text']
                            new_sub_comment.CommentIdRelated = new_comment
                            new_sub_comment.InsertDate = sub_comment['date']
                            new_sub_comment.save()

            if 'fileName' in checklists[tab][key] and checklists[tab][key]['fileName'] is not None:
                document_exists = False
                if ChecklistDocument.objects.filter(QuestionId=int(key),
                                                    CreditApplicationId=credit_application_id).exists():
                    checklist_document = ChecklistDocument.objects.filter(QuestionId=int(key),
                                                                          CreditApplicationId=credit_application_id).first()
                    document = Document.objects.get(DocumentId=checklist_document.DocumentId_id)
                    document_file = DocumentFile.objects.get(DocumentId=checklist_document.DocumentId_id)
                    document_exists = True
                else:
                    document = Document()
                    document.InsertDate = timezone.now()
                    document_file = DocumentFile()
                    document_file.InsertDate = timezone.now()
                    checklist_document = ChecklistDocument()
                    checklist_document.InsertDate = timezone.now()

                if 'fileInfo' in checklists[tab][key] and checklists[tab][key]['fileInfo'] is not None:
                    if isinstance(checklists[tab][key]['fileInfo'], str):
                        if not document_exists:
                            document.CreditApplicationId_id = credit_application_id
                            document.BasePartyId_id = base_party_id
                            document.FileName = checklists[tab][key]['fileName']
                            document.FileType = checklists[tab][key]['fileType']
                            document.FileSize = checklists[tab][key]['fileSize']
                            document.InsertedBy = user
                            document.InsertDate = timezone.now()
                            document.LastUpdatedDate = timezone.now()
                            document.LastUpdatedBy = user
                            document.save()

                            document_file.FileName = checklists[tab][key]['fileName']
                            document_file.FileType = checklists[tab][key]['fileType']
                            document_file.FileSize = checklists[tab][key]['fileSize']
                            document_file.DocumentId = document

                            checklist_document.CreditApplicationId_id = credit_application_id
                            checklist_document.BasePartyId_id = base_party_id
                            checklist_document.QuestionId_id = int(key)
                            checklist_document.DocumentId = document
                            checklist_document.FileType = checklists[tab][key]['fileType']
                            checklist_document.FileSize = checklists[tab][key]['fileSize']

                            if documents_storage['storage_location'] == 1:
                                document_file.FileObject = checklists[tab][key]['fileInfo']
                                document.StorageLocation = 1
                            elif documents_storage['storage_location'] == 2:
                                document_base64_string = checklists[tab][key]['fileInfo'].split(",")[1]
                                new_file = base64.b64decode(document_base64_string)

                                dir_url = "{}/{}/{}".format(documents_storage['directory_path'], base_party_id, document.DocumentId)
                                file_url = "{}/{}/{}/{}".format(documents_storage['directory_path'], base_party_id, document.DocumentId, checklists[tab][key]['fileName'])

                                if not os.path.exists(dir_url):
                                    os.makedirs(dir_url)

                                with open(file_url, 'wb') as file:
                                    file.write(new_file)

                                document.StorageLocation = 2
                                document.FileURL = file_url
                                document_file.FileURL = file_url

                            document_file.save()
                            document.save()
                            checklist_document.save()

                    elif isinstance(checklists[tab][key]['fileInfo'], dict):
                        file_id = checklists[tab][key]['fileInfo']['fileId']

                        if Document.objects.filter(DocumentId=file_id).exists():
                            existing_document = Document.objects.filter(DocumentId=file_id).first()

                            checklist_document.CreditApplicationId_id = credit_application_id
                            checklist_document.BasePartyId_id = base_party_id
                            checklist_document.QuestionId_id = int(key)
                            checklist_document.DocumentId = existing_document
                            checklist_document.FileType = existing_document.FileType
                            checklist_document.FileSize = existing_document.FileSize
                            checklist_document.save()
            else:
                if ChecklistDocument.objects.filter(QuestionId=int(key),
                                                    CreditApplicationId=credit_application_id).exists():
                    ChecklistDocument.objects.filter(QuestionId=int(key),
                                                     CreditApplicationId=credit_application_id).delete()

    ChecklistAnswer.objects.filter(CreditApplicationId=credit_application_id, TemplateId__in=affected_templates).exclude(QuestionId__in=affected_questions).delete()

    templates = ChecklistTemplate.objects.filter(TemplateId__in=affected_templates)
    for template in templates:
        template_answers = ChecklistAnswer.objects.filter(CreditApplicationId=credit_application_id,
                                                          TemplateId=template.TemplateId)

        score_pass = template.ScorePass
        score_fail = template.ScoreFail
        score_pending = template.ScorePending

        for result_number in range(1, 5):
            if ChecklistResult.objects.filter(CreditApplicationId=credit_application_id, TemplateId=template.TemplateId,
                                              TEMP_FIELD=result_number).exists():
                checklist_result = ChecklistResult.objects.filter(CreditApplicationId=credit_application_id,
                                                                  TemplateId=template.TemplateId,
                                                                  TEMP_FIELD=result_number).first()
            else:
                checklist_result = ChecklistResult()
                checklist_result.CreditApplicationId_id = credit_application_id
                checklist_result.BasePartyId_id = base_party_id
                checklist_result.TemplateId = template
                checklist_result.Role = getattr(template, "Response{}Role".format(result_number), 'Default role')
                checklist_result.InsertedBy = user
                checklist_result.InsertDate = timezone.now()
                checklist_result.TEMP_FIELD = result_number

            score = 0

            for answer in template_answers:
                score += getattr(answer, "Response{}Score".format(result_number), 0) if getattr(answer,
                                                                                                "Response{}Score".format(
                                                                                                    result_number),
                                                                                                0) is not None else 0

            checklist_result.Score = score

            if score_pass <= score:
                checklist_result.Status_id = 1
            elif score_fail <= score < score_pass:
                checklist_result.Status_id = 2
            elif score_pending <= score < score_fail:
                checklist_result.Status_id = 3

            checklist_result.LastUpdatedBy = user
            checklist_result.LastUpdatedDate = timezone.now()
            checklist_result.save()
