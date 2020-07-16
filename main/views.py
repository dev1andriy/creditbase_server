import logging

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.http import *
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.utils import json
from rest_framework.views import APIView

from main import authenticators
from django.contrib.auth.models import User

from common.models import *

# from base_party.models import BaseParty, BasePartyIdentifier, BasePartyNonIndividual

from main.forms import SignupForm

from common.serializers import UserSerializer

logging.basicConfig(filename="test.log", level=logging.DEBUG)


@login_required(login_url='/api-auth/')
@ensure_csrf_cookie
def index(request):
    return HttpResponse("")


@login_required(login_url='/api-auth/')
@ensure_csrf_cookie
def profile(request):
    return HttpResponse("{page: profile}")


@login_required(login_url='/api-auth/')
@ensure_csrf_cookie
def create_account_category(request):
    current_user = request.user
    return HttpResponse(current_user.id)


@login_required(login_url='/api-auth/')
@api_view(['GET'])
@ensure_csrf_cookie
def get_account(request):
    current_user = request.user
    return Response(UserSerializer(current_user).data)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


class AuthView(APIView):
    authentication_classes = (authenticators.QuietBasicAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
            user_data = json.loads(request.body)
            user = authenticate(username=user_data['username'], password=user_data['password'])
            request.user = user
            login(request, request.user)
            return Response(UserSerializer(request.user).data)
        except:
            return HttpResponseBadRequest(json.dumps({'error': 'bad request'}), content_type="application/json")


def delete(self, request, *args, **kwargs):
    logout(request)
    return Response()


@api_view(['GET'])
def fill_database(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(username="admin",
                                      email="admin@mail.com",
                                      password="admin",
                                      first_name="Name",
                                      last_name="Surname")

    base_models = [
        FinancialInstitution,
        BusinessUnit,
        Sector,
        Industry,
        OperationalStatus,
        CRMStrategy,
        Country,
        Industry,
        AssetClassification,
        FinancialModel,
        FiscalYearEnd,
        FinancialModel,
        DecisionMakingType,
        GovernanceType,
        PreferenceType,
        TelephoneType,
        PreferenceType,
        # AddressType,
        EmailType,
        IdentifierCategory,
        IdentifierType,
        RelationCategory,
        # RelationType,
        ProfileType,
        ActivityType,
        BuyerPower,
        SupplierPower,
        NewEntrantThreat,
        SubstitutionThreat,
        CompetitiveRivalry,
        RelatedItemType,

        ApplicationPriority,
        ApplicationSource,
        ApplicationStatus,
        ApplicationType,
        BusinessUnit,
        DecisionType,
        DeclineReason,
        AuthorityLevel,
        ProductType,
        Purpose,

        AccountCategory,
        AccountClass,
        AccountStatus,
        AccountOfficer,
        # Currency,
        LimitType,
        PostingRestrictionType,

        RequestType
    ]

    base_party_types = [
        {"value": "Individual", "id": 1},
        {"value": "Non-individual", "id": 2}
    ]

    for type in base_party_types:
        base_party_type = BasePartyType()
        base_party_type.BasePartyTypeId = type["id"]
        base_party_type.Description = type["value"]
        base_party_type.save()

    adress_types = [
        {"value": "Physical Address", "id": 1},
        {"value": "Email", "id": 2}
    ]

    for type in adress_types:
        address_type = AddressType()
        address_type.AddressTypeId = type["id"]
        address_type.Description = type["value"]
        address_type.save()


    flags = [
        {"value": "Yes", "id": 1},
        {"value": "No", "id": 2},
    ]

    for flag in flags:
        flag_record = Flag()
        flag_record.FlagId = flag["id"]
        flag_record.Description = flag["value"]
        flag_record.save()

    for i in base_models:
        for j in range(1, 3):
            try:
                new_record = i()
                new_record.__dict__[i.__name__ + "Id"] = j
                new_record.__dict__['Description'] = "Option" + str(j)

                new_record.save()
            except:
                pass

    for i in range(1, 3):
        business_unit = BusinessUnit()
        business_unit.BusinessUnitId = i
        business_unit.FinancialInstitution_id = i
        business_unit.Description = "Option " + str(i)
        business_unit.save()

    for i in range(1, 3):
        account_type = AccountType()
        account_type.AccountTypeId = i
        account_type.AccountCategory_id = i
        account_type.Description = "Option " + str(i)
        account_type.save()

    for i in range(1, 3):
        relation_type = RelationType()
        relation_type.RelationTypeId = i
        relation_type.RelationCategory_id = i
        relation_type.Description = "Option " + str(i)
        relation_type.save()

    application_statuses = [
        {"value": "New application", "icon": "edit", "color": "#29b6f6"},
        {"value": "Analysis & writeup", "icon": "edit", "color": "#29b6f6"},
        {"value": "Pending decision", "icon": "call_split", "color": "#29b6f6"},
        {"value": "Returned for rework", "icon": "reply", "color": "#ffa726"},
        {"value": "Approved", "icon": "done", "color": "#66bb6a"},
        {"value": "Declined", "icon": "close", "color": "#ef5350"},
        {"value": "Pending offer preparation", "icon": "done", "color": "#66bb6a"},
        {"value": "Pending customer acceptance", "icon": "done", "color": "#66bb6a"},
        {"value": "Security perfection", "icon": "done", "color": "#66bb6a"},
        {"value": "Pending customer acceptance", "icon": "done", "color": "#66bb6a"},
        {"value": "Document verification", "icon": "done", "color": "#66bb6a"},
        {"value": "Pending booking", "icon": "done", "color": "#66bb6a"},
        {"value": "Booked", "icon": "done", "color": "#66bb6a"},
    ]

    index = 1
    for status in application_statuses:
        new_application_status = ApplicationStatus()
        new_application_status.ApplicationStatusId = index
        new_application_status.Description = status['value']
        new_application_status.Description1 = status['icon']
        new_application_status.Description2 = status['color']
        new_application_status.save()
        index += 1

    account_statuses = [
        {"value": "Active", "icon": "done", "color": "#66bb6a"},
        {"value": "Dormant", "icon": "ac_unit", "color": "#29b6f6"},
        {"value": "Posting restrictions", "icon": "remove_circle_outline", "color": "#ffa726"},
        {"value": "Closed", "icon": "clear", "color": "#ef5350"}
    ]

    index = 1
    for status in account_statuses:
        account_status = AccountStatus()
        account_status.AccountStatusId = index
        account_status.Description = status['value']
        account_status.Description1 = status['icon']
        account_status.Description2 = status['color']
        account_status.save()
        index += 1

    checklist_statuses = [
        {"value": "Passed", "color": "#66bb6a"},
        {"value": "Failed", "color": "#ef5350"},
        {"value": "Pending", "color": "#ffa726"},
    ]

    for index, value in enumerate(checklist_statuses):
        checklist_status = ChecklistStatus()
        checklist_status.ChecklistStatusId = index + 1
        checklist_status.Description = value["value"]
        checklist_status.Description1 = value["color"]
        checklist_status.save()

    checklist_tabs = [
        {"name": "abc_tab", "title": "ABC tab"},
        {"name": "qwertytab", "title": "QWERTYtab"}
    ]

    for index, value in enumerate(checklist_tabs):
        checklist_tab = ChecklistTab()
        checklist_tab.ChecklistTabId = index + 1
        checklist_tab.Name = value["name"]
        checklist_tab.Title = value["title"]
        checklist_tab.TabLevel = 1
        checklist_tab.save()

    checklist_template = ChecklistTemplate()
    checklist_template.TemplateId = 1
    checklist_template.ChecklistTabId_id = 1
    checklist_template.Name = "cool_template"
    checklist_template.Description = "Cool template"
    checklist_template.ProfileTypes = ["1", "2"]
    checklist_template.ApplicationTypes = ["1", "2"]
    checklist_template.ApplicationPurposes = ["1", "2"]
    checklist_template.ProductTypesApplicable = ["1", "2"]
    checklist_template.Response1Role = "Role1"
    checklist_template.Response2Role = "Role2"
    # checklist_template.Response3Role = "Role3"
    checklist_template.Response4Role = "Role4"
    checklist_template.Response1Label = "R1"
    checklist_template.Response2Label = "R2"
    # checklist_template.Response3Label = "R3"
    checklist_template.Response4Label = "R4"
    checklist_template.ScorePass = 6
    checklist_template.ScoreFail = 4
    checklist_template.ScorePending = 2
    checklist_template.save()

    checklist_question_without_parent = ChecklistQuestion()
    checklist_question_without_parent.QuestionId = 1
    checklist_question_without_parent.TemplateId = checklist_template
    checklist_question_without_parent.Description = "Cool question without section"
    checklist_question_without_parent.HelpText = "Select response '2' to see follow up question"
    checklist_question_without_parent.DocumentType = ["image/*", ".pdf"]
    checklist_question_without_parent.OrderingRank = 1
    checklist_question_without_parent.save()

    checklist_question_without_parent_followup = ChecklistQuestion()
    checklist_question_without_parent_followup.QuestionId = 2
    checklist_question_without_parent_followup.TemplateId = checklist_template
    checklist_question_without_parent_followup.Description = "Cool followup"
    checklist_question_without_parent_followup.HelpText = "Cool help text"
    checklist_question_without_parent_followup.DocumentType = ["image/*", ".pdf"]
    checklist_question_without_parent_followup.OrderingRank = 2
    checklist_question_without_parent_followup.save()

    checklist_section = ChecklistQuestion()
    checklist_section.QuestionId = 3
    checklist_section.ParentSectionFlag = True
    checklist_section.Description = "Cool section"
    checklist_section.TemplateId = checklist_template
    checklist_section.OrderingRank = 3
    checklist_section.save()

    checklist_question = ChecklistQuestion()
    checklist_question.QuestionId = 4
    checklist_question.ParentSectionId = checklist_section
    checklist_question.TemplateId = checklist_template
    checklist_question.Description = "Cool question"
    checklist_question.HelpText = "Select response '3' to see follow up questions"
    checklist_question.DocumentType = ["image/*", ".pdf"]
    checklist_question.OrderingRank = 4
    checklist_question.save()

    checklist_followup_question = ChecklistQuestion()
    checklist_followup_question.QuestionId = 5
    checklist_followup_question.ParentSectionId = checklist_section
    checklist_followup_question.TemplateId = checklist_template
    checklist_followup_question.Description = "Cool followup question"
    checklist_followup_question.HelpText = "Hi! I am follow up question"
    checklist_followup_question.DocumentType = ["image/*", ".pdf"]
    checklist_followup_question.DocumentsFlag = True
    checklist_followup_question.OrderingRank = 5
    checklist_followup_question.save()

    another_checklist_followup_question = ChecklistQuestion()
    another_checklist_followup_question.QuestionId = 6
    another_checklist_followup_question.ParentSectionId = checklist_section
    another_checklist_followup_question.TemplateId = checklist_template
    another_checklist_followup_question.Description = "Another followup question"
    another_checklist_followup_question.HelpText = "Hi! I am another follow up question"
    another_checklist_followup_question.DocumentType = ["image/*", ".pdf"]
    another_checklist_followup_question.OrderingRank = 6
    another_checklist_followup_question.save()

    another_checklist_question = ChecklistQuestion()
    another_checklist_question.QuestionId = 7
    another_checklist_question.ParentSectionId = checklist_section
    another_checklist_question.TemplateId = checklist_template
    another_checklist_question.Description = "Another cool question"
    another_checklist_question.HelpText = "Nice to see you here"
    another_checklist_question.DocumentType = ["image/*", ".pdf"]
    another_checklist_question.DocumentsFlag = True
    another_checklist_question.OrderingRank = 7
    another_checklist_question.save()

    checklist_responses = [
        {"question": checklist_followup_question, "points": 1, "follow_up": None, "description": 1, "id": 1},
        {"question": checklist_followup_question, "points": 2, "follow_up": None, "description": 2, "id": 2},

        {"question": checklist_question, "points": 1, "follow_up": None, "description": 1, "id": 3},
        {"question": checklist_question, "points": 2, "follow_up": None, "description": 2, "id": 4},
        {"question": checklist_question, "points": 3, "follow_up": ["5", "6"], "description": 3, "id": 5},
        {"question": checklist_question, "points": 4, "follow_up": None, "description": 4, "id": 6},

        {"question": another_checklist_question, "points": 1, "follow_up": None, "description": 1, "id": 7},
        {"question": another_checklist_question, "points": 2, "follow_up": None, "description": 2, "id": 8},
        {"question": another_checklist_question, "points": 3, "follow_up": None, "description": 3, "id": 9},

        {"question": another_checklist_followup_question, "points": 1, "follow_up": None, "description": 1, "id": 10},
        {"question": another_checklist_followup_question, "points": 2, "follow_up": None, "description": 2, "id": 11},

        {"question": checklist_question_without_parent, "points": 1, "follow_up": None, "description": 1, "id": 12},
        {"question": checklist_question_without_parent, "points": 2, "follow_up": ["2"], "description": 2, "id": 13},

        {"question": checklist_question_without_parent_followup, "points": 1, "follow_up": None, "description": 1, "id": 14},
        {"question": checklist_question_without_parent_followup, "points": 2, "follow_up": None, "description": 2, "id": 15},
    ]

    for response in checklist_responses:
        checklist_response = ChecklistResponse()
        checklist_response.ResponseId = response["id"]
        checklist_response.QuestionId = response["question"]
        checklist_response.Points = response["points"]
        checklist_response.FollowupQuestionId = response["follow_up"]
        checklist_response.Description = response["description"]
        checklist_response.save()

    workflow_process = WorkflowProcess()
    workflow_process.WorkflowProcessId = 1
    workflow_process.Description = "Cool workflow"
    workflow_process.ProfileTypes = ["1", "2"]
    workflow_process.ApplicationTypes = ["1"]
    workflow_process.ApplicationPurposes = ["1", "2"]
    workflow_process.ProductTypesApplicable = ["1", "2"]
    workflow_process.save()

    another_workflow_process = WorkflowProcess()
    another_workflow_process.WorkflowProcessId = 2
    another_workflow_process.Description = "Another cool workflow"
    another_workflow_process.ProfileTypes = ["1", "2"]
    another_workflow_process.ApplicationTypes = ["2"]
    another_workflow_process.ApplicationPurposes = ["1", "2"]
    another_workflow_process.ProductTypesApplicable = ["1", "2"]
    another_workflow_process.save()

    application_template = ApplicationTemplate()
    application_template.ApplicationTemplateId = 1
    application_template.Description = "Cool app template"
    application_template.ProfileTypes = ["1", "2"]
    application_template.ApplicationTypes = ["1"]
    application_template.ApplicationPurposes = ["1", "2"]
    application_template.ProductTypesApplicable = ["1", "2"]
    application_template.save()

    another_application_template = ApplicationTemplate()
    another_application_template.ApplicationTemplateId = 2
    another_application_template.Description = "Another cool app template"
    another_application_template.ProfileTypes = ["1", "2"]
    another_application_template.ApplicationTypes = ["2"]
    another_application_template.ApplicationPurposes = ["1", "2"]
    another_application_template.ProductTypesApplicable = ["1", "2"]
    another_application_template.save()

    application_template_section = [
        {"id": 1, "template": "Cool app template", "tab": "general", "name": "applicationHighlights", "title": "Application Highlights", "type": "dict"},
        {"id": 2, "template": "Another cool app template", "tab": "general", "name": "applicationStaff", "title": "Application Staff", "type": "array"},
    ]

    for template in application_template_section:
        template_section = ApplicationTemplateSection()
        template_section.ApplicationTemplateSectionId = template["id"]
        template_section.Description = template['template']
        template_section.Description1 = template['tab']
        template_section.Description2 = template['name']
        template_section.Description3 = template['title']
        template_section.Description4 = template['type']
        template_section.save()

    # ARRANGEMENT

    arrangement_categories = [
        {"id": 1, "value": "Facility"},
        {"id": 2, "value": "Collateral"},
        {"id": 3, "value": "Deposit"}
    ]

    for category in arrangement_categories:
        arrangement_category = ArrangementCategory()
        arrangement_category.ArrangementCategoryId = category["id"]
        arrangement_category.Description = category["value"]
        arrangement_category.save()

    arrangement_types = [
        {"id": 1, "value": "Parent type", "parent_flag": True, "parent": None, "category": 1},
        {"id": 2, "value": "Children type", "parent_flag": False, "parent": 1, "category": 1},
        {"id": 3, "value": "Alone type", "parent_flag": True, "parent": None, "category": 1},
    ]

    for type in arrangement_types:
        arrangement_type = ArrangementType()
        arrangement_type.ArrangementTypeId = type["id"]
        arrangement_type.Description = type["value"]
        arrangement_type.ParentFlag = type["parent_flag"]
        arrangement_type.ArrangementTypeParent_id = type["parent"]
        arrangement_type.ArrangementCategory_id = type["category"]
        arrangement_type.save()

    arrangement_param_categories = [
        {"id": 1, "value": "General parameters", "category": 1},
        {"id": 2, "value": "Date parameters", "category": 1},
    ]

    for category in arrangement_param_categories:
        arrangement_param_category = ArrangementParamCategory()
        arrangement_param_category.ArrangementParamCategoryId = category["id"]
        arrangement_param_category.Description = category["value"]
        arrangement_param_category.ArrangementCategory_id = category["category"]
        arrangement_param_category.save()

    arrangement_params = [
        {"id": 1, "category": 1, "param_category": 1, "field_type": 2, "name1": "", "name2": "Description",
         "name3": "Desc", "name4": "Description1", "required": True},
        {"id": 2, "category": 1, "param_category": 1, "field_type": 5, "name1": "", "name2": "Currency",
         "name3": "Curr", "name4": "Currency", "description": "Currency", "description1": "CurrencyId", "description2": "Description", "required": True},
        {"id": 3, "category": 1, "param_category": 1, "field_type": 1, "name1": "", "name2": "Balance Value",
         "name3": "BalValue", "name4": "BalanceValue", "required": False},
        {"id": 4, "category": 1, "param_category": 1, "field_type": 2, "name1": "", "name2": "Open Market Value",
         "name3": "OMValue", "name4": "OpenMarketValue", "required": True},
        {"id": 5, "category": 1, "param_category": 2, "field_type": 4, "name1": "", "name2": "Balance Date",
         "name3": "BalDate", "name4": "BalanceDate", "required": False},
    ]

    for param in arrangement_params:
        arrangement_param = ArrangementParam()
        arrangement_param.ArrangementParamId = param["id"]
        arrangement_param.ArrangementCategory_id = param["category"]
        arrangement_param.ArrangementParamCategory_id = param["param_category"]
        arrangement_param.FieldType = param["field_type"]
        arrangement_param.Name1 = param["name1"]
        arrangement_param.Name2 = param["name2"]
        arrangement_param.Name3 = param["name3"]
        arrangement_param.Name4 = param["name4"]
        arrangement_param.Description = param["description"] if "description" in param else None
        arrangement_param.Description1 = param["description1"] if "description1" in param else None
        arrangement_param.Description2 = param["description2"] if "description2" in param else None
        arrangement_param.Mandatory = param["required"]
        arrangement_param.save()

    arrangement_param_matrixes = [
        {
            "id": 1,
            "param_id": 1,
            "arrangement_type": 2,
            "request_type": 1,
            "value_limits": None,
            "display_flag": {
                "DataView1": 1,
                "DataView2": 1,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            },
            "modify_flag": {
                "DataView1": 1,
                "DataView2": 1,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            },
            "print_flag": {
                "DataView1": 2,
                "DataView2": 0,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            }
        },
        {
            "id": 2,
            "param_id": 2,
            "arrangement_type": 2,
            "request_type": 1,
            "value_limits": None,
            "display_flag": {
                "DataView1": 1,
                "DataView2": 1,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            },
            "modify_flag": {
                "DataView1": 1,
                "DataView2": 1,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            },
            "print_flag": {
                "DataView1": 2,
                "DataView2": 0,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            }
        },
        {
            "id": 3,
            "param_id": 3,
            "arrangement_type": 2,
            "request_type": 1,
            "value_limits": {
                "Lower": 10,
                "Default": 15,
                "Upper": 20
            },
            "display_flag": {
                "DataView1": 1,
                "DataView2": 1,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            },
            "modify_flag": {
                "DataView1": 1,
                "DataView2": 0,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            },
            "print_flag": {
                "DataView1": 1,
                "DataView2": 1,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            }
        },
        {
            "id": 4,
            "param_id": 4,
            "arrangement_type": 2,
            "request_type": 2,
            "value_limits": None,
            "display_flag": {
                "DataView1": 0,
                "DataView2": 1,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            },
            "modify_flag": {
                "DataView1": 0,
                "DataView2": 1,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            },
            "print_flag": {
                "DataView1": 0,
                "DataView2": 1,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            }
        },
        {
            "id": 5,
            "param_id": 5,
            "arrangement_type": 2,
            "request_type": 1,
            "value_limits": None,
            "display_flag": {
                "DataView1": 1,
                "DataView2": 1,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            },
            "modify_flag": {
                "DataView1": 1,
                "DataView2": 0,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            },
            "print_flag": {
                "DataView1": 1,
                "DataView2": 1,
                "DataView3": 0,
                "DataView4": 0,
                "DataView5": 0,
            }
        }
    ]

    for param_matrix in arrangement_param_matrixes:
        arrangement_param_matrix = ArrangementParamMatrix()
        arrangement_param_matrix.ArrangementParamMatrixId = param_matrix["id"]
        arrangement_param_matrix.ArrangementParamId_id = param_matrix["param_id"]
        arrangement_param_matrix.ArrangementType_id = param_matrix["arrangement_type"]
        arrangement_param_matrix.RequestType_id = param_matrix["request_type"]
        arrangement_param_matrix.ValueLimits = param_matrix["value_limits"]
        arrangement_param_matrix.DisplayFlag = param_matrix["display_flag"]
        arrangement_param_matrix.ModifyFlag = param_matrix["modify_flag"]
        arrangement_param_matrix.PrintFlag = param_matrix["print_flag"]
        arrangement_param_matrix.save()

    currencies = [
        {'id': 1, 'description': 'USD'},
        {'id': 2, 'description': 'UAH'},
        {'id': 3, 'description': 'EUR'},
        {'id': 4, 'description': 'KES'},
    ]

    for currency in currencies:
        currency_record = Currency()
        currency_record.CurrencyId = currency.get('id')
        currency_record.Description = currency.get('description')
        currency_record.save()

    currency_rates = [
        {'id': 1, 'currency_in': 1, 'currency_out': 2, 'rate': 0.039, 'rate_date': None},
        {'id': 2, 'currency_in': 1, 'currency_out': 3, 'rate': 1.12, 'rate_date': None},
        {'id': 3, 'currency_in': 1, 'currency_out': 4, 'rate': 0.0097, 'rate_date': None},

        {'id': 4, 'currency_in': 2, 'currency_out': 1, 'rate': 25.57, 'rate_date': None},
        {'id': 5, 'currency_in': 2, 'currency_out': 3, 'rate': 28.73, 'rate_date': None},
        {'id': 6, 'currency_in': 2, 'currency_out': 4, 'rate': 0.25, 'rate_date': None},

        {'id': 7, 'currency_in': 3, 'currency_out': 1, 'rate': 0.89, 'rate_date': None},
        {'id': 8, 'currency_in': 3, 'currency_out': 2, 'rate': 0.035, 'rate_date': None},
        {'id': 9, 'currency_in': 3, 'currency_out': 4, 'rate': 0.0086, 'rate_date': None},

        {'id': 10, 'currency_in': 4, 'currency_out': 1, 'rate': 103.47, 'rate_date': None},
        {'id': 11, 'currency_in': 4, 'currency_out': 2, 'rate': 4.05, 'rate_date': None},
        {'id': 12, 'currency_in': 4, 'currency_out': 3, 'rate': 116.17, 'rate_date': None},
    ]

    for rate in currency_rates:
        currency_rate = CurrencyRate()
        currency_rate.CurrencyRateId = rate['id']
        currency_rate.CurrencyIn_id = rate['currency_in']
        currency_rate.CurrencyOut_id = rate['currency_out']
        currency_rate.ExchangeRate = rate['rate']
        currency_rate.save()

    # SEARCH
    search_templates = [
        {"TemplateId": 1, "TemplateName": "Advanced Search", "OrderingRank": 1, "Enabled": True},
        {"TemplateId": 2, "TemplateName": "Advanced Search", "OrderingRank": 1, "Enabled": True}
    ]

    for template in search_templates:
        SearchTemplates.objects.create(**template)

    search_criteria = [
        {"CriteriaId": 1, "CriteriaName": "Equals", "CriteriaSymbol": "exact", "IsExcludeCondition": False},
        {"CriteriaId": 2, "CriteriaName": "Contains", "CriteriaSymbol": "icontains", "IsExcludeCondition": False},
        {"CriteriaId": 3, "CriteriaName": "Less Than", "CriteriaSymbol": "lt", "IsExcludeCondition": False},
        {"CriteriaId": 4, "CriteriaName": "Greater Than", "CriteriaSymbol": "gt", "IsExcludeCondition": False},
        {"CriteriaId": 5, "CriteriaName": "Between", "CriteriaSymbol": "in", "IsExcludeCondition": False},
        {"CriteriaId": 6, "CriteriaName": "In Range", "CriteriaSymbol": "in", "IsExcludeCondition": False},
        {"CriteriaId": 7, "CriteriaName": "Not Equal", "CriteriaSymbol": "exact", "IsExcludeCondition": True},
    ]

    for criteria in search_criteria:
        SearchCriteria.objects.create(**criteria)

    search_fields = [
        {"FieldId": 1, "FieldType": 1, "Name": "BasePartyName", "Description": "Base Party Name",
         "FieldModelPath": None, "ActiveFlag": True, "AllowNullFlag": True, "DefaultCriteriaId_id": 2,
         "LookupKey": None, "LookupValue": None, "ApplicableCriteria": "[1, 2, 7]"},
        {"FieldId": 2, "FieldType": 5, "Name": "Sector", "Description": "Sector", "FieldModelPath": None,
         "ActiveFlag": True, "AllowNullFlag": True, "DefaultCriteriaId_id": 1, "LookupKey": "SectorId",
         "LookupValue": "Description", "ApplicableCriteria": "[1, 2, 3, 4, 5, 6, 7]"},
        {"FieldId": 3, "FieldType": 3, "Name": "ApplicationNumber", "Description": "Application Number",
         "FieldModelPath": "BasePartyCreditApplication__CreditApplicationId", "ActiveFlag": True, "AllowNullFlag": True,
         "DefaultCriteriaId_id": 1, "LookupKey": None, "LookupValue": None, "ApplicableCriteria": "[1]"},
        {"FieldId": 4, "FieldType": 5, "Name": "BusinessUnit", "Description": "Business Unit", "FieldModelPath": None,
         "ActiveFlag": True, "AllowNullFlag": True, "DefaultCriteriaId_id": 1, "LookupKey": "BusinessUnitId",
         "LookupValue": "Description", "ApplicableCriteria": "[1, 2, 3, 4, 5, 6, 7]"},
        {"FieldId": 5, "FieldType": 4, "Name": "DOB", "Description": "Date Of Birth", "FieldModelPath": None,
         "ActiveFlag": True, "AllowNullFlag": True, "DefaultCriteriaId_id": 1, "LookupKey": None, "LookupValue": None,
         "ApplicableCriteria": "[1, 3, 4, 5, 6, 7]"}
    ]
    for fields in search_fields:
        SearchFields.objects.create(**fields)

    search_template_params = [
        {"ParamId": 2, "TemplateField_id": 1, "TemplateId_id": 1},
        {"ParamId": 3, "TemplateField_id": 2, "TemplateId_id": 1},
        {"ParamId": 4, "TemplateField_id": 3, "TemplateId_id": 1},
        {"ParamId": 5, "TemplateField_id": 1, "TemplateId_id": 2},
        {"ParamId": 6, "TemplateField_id": 4, "TemplateId_id": 2}
    ]
    for template_params in search_template_params:
        SearchTemplateParams.objects.create(**template_params)

    search_grid_config = [
        {"SearchGridId": 1,
         "GridConfig": "{\"columns\": [{\"field\": \"basePartyName\", \"action\": \"edit\", \"filter\": "
                       "\"agTextColumnFilter\", \"headerName\": \"Full Name\", \"cellRenderer\": \"styleRenderer\", "
                       "\"filterParams\": {\"filterOptions\": [\"contains\"]}, \"checkboxSelection\": true}, "
                       "{\"field\": \"legalId\", \"filter\": \"agTextColumnFilter\", \"headerName\": \"Legal ID\", "
                       "\"filterParams\": {\"filterOptions\": [\"contains\"]}}, {\"field\": \"sector\", \"filter\": "
                       "\"agTextColumnFilter\", \"headerName\": \"Sector\", \"filterParams\": {\"filterOptions\": ["
                       "\"contains\"]}}, {\"hide\": true, \"field\": \"systemSource\", \"filter\": "
                       "\"agTextColumnFilter\", \"rowGroup\": true, \"headerName\": \"Source\", \"filterParams\": {"
                       "\"filterOptions\": [\"contains\"]}}]}",
         "TemplateId_id": 1},
        {"SearchGridId": 2,
         "GridConfig": "{\"columns\": [{\"field\": \"basePartyName\", \"action\": \"edit\", \"filter\": "
                       "\"agTextColumnFilter\", \"headerName\": \"Full Name\", \"cellRenderer\": \"styleRenderer\", "
                       "\"filterParams\": {\"filterOptions\": [\"contains\"]}, \"checkboxSelection\": true}, "
                       "{\"field\": \"legalId\", \"filter\": \"agTextColumnFilter\", \"headerName\": \"Legal ID\", "
                       "\"filterParams\": {\"filterOptions\": [\"contains\"]}}, {\"field\": \"sector\", \"filter\": "
                       "\"agTextColumnFilter\", \"headerName\": \"Sector\", \"filterParams\": {\"filterOptions\": ["
                       "\"contains\"]}}, {\"hide\": true, \"field\": \"systemSource\", \"filter\": "
                       "\"agTextColumnFilter\", \"rowGroup\": true, \"headerName\": \"Source\", \"filterParams\": {"
                       "\"filterOptions\": [\"contains\"]}}]}",
         "TemplateId_id": 2}
    ]

    for grid_config in search_grid_config:
        SearchGridConfig.objects.create(**grid_config)

    return HttpResponse(200)
