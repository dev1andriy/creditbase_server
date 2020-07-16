from common.models.credit_application import *
from slugify import slugify
from common.models import BaseParty
from common.models.general import *
from common.serializers import ChecklistTabSerializer, ChecklistResponseSerializer


def generate_checklists_config(tab_level, credit_application_id, base_party_id=None):
    checklist_tabs = ChecklistTabSerializer(ChecklistTab.objects.all(), many=True).data
    if credit_application_id:
        credit_application = CreditApplication.objects.filter(CreditApplicationId=credit_application_id).first()
        answers = ChecklistAnswer.objects.filter(CreditApplicationId=credit_application_id).order_by("-LastUpdatedDate")

    config = []

    for tab in checklist_tabs:
        tab_config = {
            "id": tab['id'],
            "title": tab['title'],
            "name": tab['name'],
            "templates": [],
            "templatesList": [],
            "empty": False
        }

        if credit_application_id:
            # profile_type = str(BaseParty.objects.filter(BasePartyId=base_party_id).first().ProfileType.ProfileTypeId)
            profile_type = str(credit_application.BasePartyId.ProfileType.ProfileTypeId)
            application_type = str(credit_application.ApplicationType.ApplicationTypeId)
            products_applicable = credit_application.ProductsApplicable
            purposes_applicable = credit_application.PurposesApplicable
            # collateral_selection = ""

            templates = []
            templates_ids = []

            if answers.exists():
                for answer in answers:
                    if answer.TemplateId not in templates and answer.TemplateId.ChecklistTabId_id == tab['id']:
                        templates.append(answer.TemplateId)
                        templates_ids.append(answer.TemplateId_id)

            templates += ChecklistTemplate.objects.filter(ChecklistTabId=tab['id'],
                                                          ProfileTypes__contains=profile_type,
                                                          ApplicationTypes__contains=application_type,
                                                          ProductTypesApplicable__contains=products_applicable,
                                                          ApplicationPurposes__contains=purposes_applicable).exclude(TemplateId__in=templates_ids)
        else:
            if base_party_id is not None:
                profile_type = str(BaseParty.objects.filter(BasePartyId=base_party_id).first().ProfileType.ProfileTypeId)
                templates = ChecklistTemplate.objects.filter(ChecklistTabId=tab['id'],
                                                             ProfileTypes__contains=profile_type)
            else:
                templates = ChecklistTemplate.objects.filter(ChecklistTabId=tab['id'])

        if len(templates) < 1:
            tab_config['empty'] = True
            config.append(tab_config)
            continue

        for template in templates:
            if tab_level == 1:
                if credit_application_id is not None and ChecklistResult.objects.filter(CreditApplicationId=credit_application_id,
                                                                                        TemplateId=template.TemplateId).exists():
                    checklist_result = ChecklistResult.objects.filter(CreditApplicationId=credit_application_id,
                                                                      TemplateId=template.TemplateId)
                else:
                    checklist_result = None

            else:
                if base_party_id is not None and ChecklistResult.objects.filter(BasePartyId=base_party_id,
                                                                                TemplateId=template.TemplateId).exists():
                    checklist_result = ChecklistResult.objects.filter(BasePartyId=base_party_id,
                                                                      TemplateId=template.TemplateId)
                else:
                    checklist_result = None

            template_config = {
                "id": template.TemplateId,
                "title": template.Description,
                "name": slugify(template.Description, separator="_"),
                "sections": [],
                "empty": False
            }

            questions = ChecklistQuestion.objects.filter(TemplateId=template).order_by('OrderingRank')
            question_ids = [question.QuestionId for question in questions]

            stand_alone_questions = questions.filter(ParentSectionFlag=False, ParentSectionId=None)

            if len(stand_alone_questions) > 0:
                for question in stand_alone_questions:
                    template_config["sections"].append(generate_question_config(question,
                                                                                question_ids,
                                                                                template,
                                                                                checklist_result,
                                                                                base_party_id))

            sections = questions.filter(ParentSectionFlag=True)
            if len(sections) < 1:
                template_config['empty'] = True
                tab_config["templates"].append(template_config)
                continue

            for section in sections:
                section_config = {
                    "type": "section",
                    "id": section.QuestionId,
                    "title": section.Description,
                    "name": slugify(section.Description, separator="_"),
                    "subSections": [],
                    "empty": False,
                    "order": section.OrderingRank
                }
                sub_sections = questions.filter(ParentSectionFlag=False, ParentSectionId=section)
                if len(sub_sections) < 1:
                    section_config['empty'] = True
                    template_config["sections"].append(section_config)
                    continue

                for question in sub_sections:
                    section_config['subSections'].append(generate_question_config(question,
                                                                                  question_ids,
                                                                                  template,
                                                                                  checklist_result,
                                                                                  base_party_id))

                template_config["sections"].append(section_config)

            tab_config["templatesList"].append(template_config["name"])
            tab_config["templates"].append(template_config)

        config.append(tab_config)

    return config


def generate_question_config(question, question_ids, template, checklist_result, base_party_id):
    document_types = ""
    if question.DocumentType is not None:
        for index, document_type in enumerate(question.DocumentType):
            document_types += document_type
            if index + 1 < len(question.DocumentType):
                document_types += ", "

    if ChecklistResponse.objects.filter(QuestionId__in=question_ids,
                                        FollowupQuestionId__contains=str(
                                            question.QuestionId)).exists():
        checklist_response_followup = ChecklistResponse.objects.filter(QuestionId__in=question_ids,
                                                                       FollowupQuestionId__contains=str(
                                                                           question.QuestionId))

        required_by_questions = {}
        for response in checklist_response_followup:
            if response.QuestionId_id not in required_by_questions:
                required_by_questions[response.QuestionId_id] = [response.ResponseId]
            elif response.QuestionId_id in required_by_questions and isinstance(required_by_questions[response.QuestionId_id], list):
                required_by_questions[response.QuestionId_id].append(response.ResponseId)
    else:
        checklist_response_followup = None
        required_by_questions = None

    labels = []

    for i in range(1, 5):
        if getattr(template, 'Response{}Label'.format(i)) is not None and getattr(template, 'Response{}Role'.format(
                i)) is not None:
            labels.append({
                "value": getattr(template, 'Response{}Label'.format(i)),
                "enabled": not checklist_result.filter(
                    Role=getattr(template, 'Response{}Role'.format(
                        i))).first().FinalizedFlag if checklist_result and checklist_result.filter(
                    Role=getattr(template, 'Response{}Role'.format(i))).exists() else True
            })

    return {
        "type": "subSection",
        "subSectionType": "followUpQuestion" if checklist_response_followup is not None else "defaultQuestion",
        "requiredByQuestions": required_by_questions,
        "id": question.QuestionId,
        "title": question.Description,
        "name": slugify(question.Description, separator="_"),
        "helpText": question.HelpText,
        "order": question.OrderingRank,
        "fields": [
            {
                "name": "checklistAnswers",
                "type": "radioButtonsGroup",
                "labels": labels,
                "responses": ChecklistResponseSerializer(ChecklistResponse.objects.filter(QuestionId=question), many=True).data,
                "order": 1
            },
            {
                "type": "input",
                "inputType": "hidden",
                "name": "fileName",
                "order": 2
            },
            {
                "type": "input",
                "inputType": "hidden",
                "name": "fileType",
                "order": 3
            },
            {
                "type": "input",
                "inputType": "hidden",
                "name": "fileSize",
                "order": 4
            },
            {
                "type": "input",
                "fileSelect": True,
                "basePartyId": base_party_id,
                "inputType": "file",
                "infoField": "fileInfo",
                "name": "document/{}".format(slugify(question.Description, separator="_")),
                "accept": document_types,
                "label": "Document",
                "order": 5
            } if question.DocumentsFlag else {},
            {
                "type": "input",
                "inputType": "hidden",
                "name": "fileInfo",
                "order": 6
            },
            {
                "type": "inputTree",
                "label": "Comments",
                "name": "comments",
                "order": 7
            },
            {
                "type": "input",
                "inputType": "hidden",
                "name": "fileView",
                "order": 8
            },
            {
                "type": "input",
                "inputType": "hidden",
                "name": "fileDocumentExists",
                "order": 9
            }
        ]
    }
