from common.models.credit_application.general.credit_application import *
from common.serializers.general import ApplicationTemplateSectionsSerializer
from common.models.credit_application.general.credit_application_template_state import *


def get_credit_application_sections_data(credit_application_id):
    credit_application = CreditApplication.objects.filter(CreditApplicationId=credit_application_id).first()
    credit_application_template = credit_application.ApplicationTemplate.Description
    credit_application_template_id = credit_application.ApplicationTemplate.ApplicationTemplateId
    credit_application_template_sections = ApplicationTemplateSection.objects.filter(Description=credit_application_template)
    sections_tabs = []

    for template_section in credit_application_template_sections:
        if template_section.Description1 not in sections_tabs:
            sections_tabs.append(template_section.Description1)

    tabs = {}

    for tab in sections_tabs:
        tabs[tab] = ApplicationTemplateSectionsSerializer(credit_application_template_sections.filter(Description1=tab), many=True).data


    return {
        "tabs": tabs,
        "credit_application_id": credit_application_id,
        "credit_application_template": credit_application_template,
        "credit_application_template_sections": credit_application_template_sections,
        "credit_application_template_id": credit_application_template_id
    }


def get_credit_application_sections_statues(credit_application_id):
    if credit_application_id is None:
        return


    sections_data = get_credit_application_sections_data(credit_application_id)

    tabs = sections_data['tabs']
    credit_application_id = sections_data['credit_application_id']
    credit_application_template_id = sections_data['credit_application_template_id']
    credit_application_template_states = CreditApplicationTemplateState.objects.filter(CreditApplicationId=credit_application_id,

                                                                                       ApplicationTemplate=credit_application_template_id)

    application_sections_statuses = []
    credit_application_status = None
    sections_partial_valid = False
    sections_fully_valid = True

    for tab in tabs:
        for section in tabs[tab]:
            state = credit_application_template_states.filter(ApplicationTemplateSection=section['id']).first().ApplicationTemplateSectionState

            section_status = {
                "id": section['id'],
                "tab": tab,
                "name": section["name"],
                "label": section["label"],
                "state": state
            }

            if section_status["state"] == 1:
                sections_partial_valid = True
            elif section_status["state"] == 2:
                credit_application_status = 2
                sections_partial_valid = True
                sections_fully_valid = False
            elif section_status["state"] == 3:
                sections_fully_valid = False

            application_sections_statuses.append(section_status)

    if sections_partial_valid and sections_fully_valid:
        credit_application_status = 1
    elif not sections_fully_valid and sections_partial_valid:
        credit_application_status = 2
    elif not sections_fully_valid and not sections_partial_valid:
        credit_application_status = 3

    return {
        "application_sections_statuses": application_sections_statuses,
        "credit_application_status": credit_application_status
    }


def generate_credit_application_sections_statuses(credit_application_data):
    if credit_application_data is None or credit_application_data['creditApplicationId'] is None:
        return

    sections_data = get_credit_application_sections_data(credit_application_data['creditApplicationId'])

    tabs = sections_data['tabs']
    credit_application_id = sections_data['credit_application_id']
    credit_application_template_id = sections_data['credit_application_template_id']

    application_sections_statuses = []
    credit_application_status = None
    sections_partial_valid = False
    sections_fully_valid = True

    for tab in tabs:
        for section in tabs[tab]:
            section_status = {
                "id": section["id"],
                "tab": tab,
                "name": section["name"],
                "label": section["label"],
                "state": None
            }

            partial_valid = False
            fully_valid = True
            if section['type'] == 'dict':
                for field in credit_application_data[tab][section["name"]][section["nestedName"]] if "nestedName" in section else credit_application_data[tab][section["name"]]:
                    value = credit_application_data[tab][section["name"]][section["nestedName"]][field] if "nestedName" in section else credit_application_data[tab][section["name"]][field]
                    if value is None or (value is not None and isinstance(value, str) and len(value) == 0):
                        fully_valid = False
                    elif value is not None or (value is not None and isinstance(value, str) and len(value) > 0):
                        partial_valid = True

            elif section['type'] == 'string':
                if credit_application_data[tab][section["name"]] is None or credit_application_data[tab][section["name"]] == '':
                    fully_valid = False
                elif credit_application_data[tab][section["name"]] is not None and credit_application_data[tab][section["name"]] != '':
                    fully_valid = True
                    partial_valid = True

            elif section['type'] == 'array':
                if len(credit_application_data[tab][section["name"]]) > 0:
                    for item in credit_application_data[tab][section["name"]]:
                        for field in item:
                            if isinstance(item[field], str):
                                value = item[field]
                                if value is None or (value is not None and isinstance(value, str) and len(value) == 0):
                                    fully_valid = False
                                elif value is not None or (value is not None and isinstance(value, str) and len(value) > 0):
                                    partial_valid = True
                            elif isinstance(item[field], dict):
                                for sub_item in item[field]:
                                    value = item[field][sub_item]
                                    if value is None or (value is not None and isinstance(value, str) and len(value) == 0):
                                        fully_valid = False
                                    elif value is not None or (
                                            value is not None and isinstance(value, str) and len(value) > 0):
                                        partial_valid = True
                elif len(credit_application_data[tab][section["name"]]) == 0:
                    fully_valid = False
                    partial_valid = False

            if partial_valid and fully_valid:
                section_status["state"] = 1
                sections_partial_valid = True
            elif not fully_valid and partial_valid:
                section_status["state"] = 2
                credit_application_status = 2
                sections_partial_valid = True
                sections_fully_valid = False
            elif not fully_valid and not partial_valid:
                section_status["state"] = 3
                sections_fully_valid = False

            if CreditApplicationTemplateState.objects.filter(CreditApplicationId=credit_application_id,
                                                             ApplicationTemplate=credit_application_template_id,
                                                             ApplicationTemplateSection=section_status['id']).exists():
                template_state = CreditApplicationTemplateState.objects.filter(CreditApplicationId=credit_application_id,
                                                                               ApplicationTemplate=credit_application_template_id,
                                                                               ApplicationTemplateSection=section_status['id']).first()

                template_state.ApplicationTemplateSectionState = section_status['state']
                template_state.save()
            else:
                template_state = CreditApplicationTemplateState()
                template_state.CreditApplicationId_id = credit_application_id
                template_state.ApplicationTemplate_id = credit_application_template_id
                template_state.ApplicationTemplateSection_id = section_status['id']
                template_state.ApplicationTemplateSectionState = section_status['state']
                template_state.save()

    if sections_partial_valid and sections_fully_valid:
        credit_application_status = 1
    elif not sections_fully_valid and sections_partial_valid:
        credit_application_status = 2
    elif not sections_fully_valid and not sections_partial_valid:
        credit_application_status = 3

    return {
        "application_sections_statuses": application_sections_statuses,
        "credit_application_status": credit_application_status
    }
