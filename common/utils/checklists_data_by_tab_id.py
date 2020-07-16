from common.models.credit_application import *
from slugify import slugify
from django.contrib.auth.models import User
from common.models.document import *
from common.serializers.credit_application import ChecklistTabSerializer, ChecklistResultSerializer


def generate_checklists_data_by_tab_id(credit_application_id, tab_id, host=None):
    if not ChecklistTab.objects.filter(ChecklistTabId=tab_id).exists():
        raise Exception("Wrong tab id")
    tab = ChecklistTabSerializer(ChecklistTab.objects.filter(ChecklistTabId=tab_id).first()).data
    config = {}
    user = User.objects.filter().first()

    config[tab['name']] = {}

    templates = ChecklistTemplate.objects.filter(ChecklistTabId=tab['id'])

    for template in templates:
        config[tab['name']][slugify(template.Description, separator="_")] = {
            "resultGrid": ChecklistResultSerializer(ChecklistResult.objects.filter(CreditApplicationId=credit_application_id, TemplateId=template.TemplateId, Score__gte=1), many=True).data
        }
        stand_alone_questions = ChecklistQuestion.objects.filter(TemplateId=template, ParentSectionFlag=False, ParentSectionId=None)
        for question in stand_alone_questions:
            section_data = generate_question_data(question, credit_application_id, template, host)
            section_data["type"] = "subSection"
            config[tab['name']][slugify(template.Description, separator="_")][slugify(question.Description, separator="_")] = section_data

        sections = ChecklistQuestion.objects.filter(TemplateId=template, ParentSectionFlag=True)
        for section in sections:
            config[tab['name']][slugify(template.Description, separator="_")][slugify(section.Description, separator="_")] = {"type": "section"}
            sub_sections = ChecklistQuestion.objects.filter(TemplateId=template, ParentSectionFlag=False, ParentSectionId=section)

            for question in sub_sections:
                section_data = generate_question_data(question, credit_application_id, template, host)
                config[tab['name']][slugify(template.Description, separator="_")][slugify(section.Description, separator="_")][slugify(question.Description, separator="_")] = section_data
    return config


def generate_question_data(question, credit_application_id, template, host):
    question_data = {}

    if ChecklistAnswer.objects.filter(TemplateId=question.TemplateId_id, QuestionId=question.QuestionId,
                                      CreditApplicationId=credit_application_id).exists():
        answer = ChecklistAnswer.objects.get(TemplateId=question.TemplateId_id, QuestionId=question.QuestionId,
                                             CreditApplicationId=credit_application_id)
        question_data["checklistAnswers"] = [
            {"label": template.Response1Label, "response": answer.Response1Id_id},
            {"label": template.Response2Label, "response": answer.Response2Id_id},
            {"label": template.Response3Label, "response": answer.Response3Id_id},
            {"label": template.Response4Label, "response": answer.Response4Id_id},
        ]

    if ChecklistComment.objects.filter(QuestionId=question.QuestionId,
                                       CreditApplicationId=credit_application_id).exists():
        comments = ChecklistComment.objects.filter(QuestionId=question.QuestionId,
                                                   CreditApplicationId=credit_application_id)

        comments_data = []

        for comment in comments.filter(CommentIdRelated=None):
            comment_data = {"text": comment.Comment, "answers": [], "isOpen": False, "date": comment.InsertDate}

            sub_comments = comments.filter(CommentIdRelated=comment.CommentId)

            for sub_comment in sub_comments:
                comment_data['answers'].append({"text": sub_comment.Comment, "date": sub_comment.InsertDate})
                comment_data['isOpen'] = True

            comments_data.append(comment_data)

        question_data["comments"] = comments_data

    if ChecklistDocument.objects.filter(QuestionId=question.QuestionId,
                                        CreditApplicationId=credit_application_id).exists():
        checklist_document = ChecklistDocument.objects.filter(QuestionId=question.QuestionId,
                                                              CreditApplicationId=credit_application_id).first()
        document_file = DocumentFile.objects.get(DocumentId=checklist_document.DocumentId_id)

        question_data["fileName"] = document_file.FileName
        # section_data["fileInfo"] = document_file.FileObject
        if document_file is not None and document_file.DocumentFileId is not None and host is not None:
            question_data["fileView"] = "http://" + host + "/ViewFile/" + str(document_file.DocumentFileId)
        question_data["fileType"] = checklist_document.FileType
        question_data["fileSize"] = checklist_document.FileSize

    return question_data
