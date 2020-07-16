from django.apps import apps
from django.core import serializers
from django.db.models import F, Q

from common.models import SearchTemplates, SearchTemplateParams, SearchFields, SearchCriteria, BaseParty
from common.serializers.other import DynamicModelSerializer


def generate_template():
    response_data = []
    templates = SearchTemplates.objects.filter(Enabled=True)
    criteria = list(SearchCriteria.objects.all().values(value=F('CriteriaId'), label=F('CriteriaName')))
    input_types = {
        1: dict(type='input', inputType='number'),
        2: dict(type='input', inputType='text'),
        3: dict(type='input', inputType='number'),
        4: dict(type='input', inputType='date'),
        5: dict(type='select', inputType=None),
        # 6: dict(type='readOnly',input_types=None)
        None: dict(type='input', inputType='text')
    }
    for template in templates:
        template_data = {
            'title': template.TemplateName,
            'id': template.TemplateId,
            'order': template.OrderingRank,
            'paramsConfig': []
        }
        template_fields = SearchTemplateParams.objects.filter(TemplateId=template.TemplateId)
        params_config = []
        for template_field in template_fields:
            field_props = SearchFields.objects.filter(FieldId=template_field.TemplateField.FieldId)
            for field_prop in field_props:
                criteria_c = list(filter(lambda x: x['value'] in list(field_prop.ApplicableCriteria),
                                         criteria)) if field_prop.ApplicableCriteria is not None else None
                field = {
                    'type': 'input',
                    'label': field_prop.Description,
                    'inputType': 'double',
                    'name': field_prop.Name,
                    'names': ['criteria', 'value'],
                    'types': ['select', input_types[field_prop.FieldType]['type']],
                    'inputTypes': ['select', input_types[field_prop.FieldType]['inputType']],
                    'order': field_prop.OrderingRank,
                    'options': [criteria_c if criteria_c is not None else criteria, get_search_lookups(field_prop)]
                }
                params_config.append(field)
                print(field_prop.FieldId)
        template_data['paramsConfig'] = params_config
        response_data.append(template_data)

    return response_data


def get_search_lookups(field_prop):
    if field_prop.FieldType != 5:
        return []
    else:
        return DynamicModelSerializer(apps.get_registered_model('common', field_prop.Name).objects.all(), many=True,
                                      value_field=field_prop.LookupKey, label_field=field_prop.LookupValue,
                                      model=field_prop.Name).data if field_prop.Name is not None and field_prop.LookupKey is not None and field_prop.LookupValue is not None else None


def search_base_party(search_data):
    search_param = {}
    for field_name, filter_value in search_data.items():
        if filter_value['criteria'] not in (None, '') and filter_value['value'] not in (None, ''):
            search_param[field_name] = filter_value
    # print(search_param)

    search_criteria = SearchCriteria.objects.values('CriteriaId', 'IsExcludeCondition', 'CriteriaSymbol')
    condition = Q()
    exclude_condition = Q()
    for field_name, filter_value in search_param.items():
        criteria = list(filter(lambda x: x['CriteriaId'] == int(filter_value['criteria']), search_criteria))
        field_model = list(SearchFields.objects.filter(Name=field_name).values('FieldModelPath'))
        field_model_path = field_model[0]['FieldModelPath'] if len(field_model) > 0 else None
        if len(criteria) == 0:
            condition.add(Q(**{field_name if field_model_path is None else field_model_path: filter_value['value']}),
                          Q.AND)

        elif criteria[0]['IsExcludeCondition']:
            exclude_condition.add(Q(**{
                '{}{}'.format(field_name if field_model_path is None else field_model_path,
                              '__' + criteria[0]['CriteriaSymbol'] if criteria is not None else None):
                    filter_value['value']}), Q.AND)
        else:
            condition.add(Q(**{
                '{}{}'.format(field_name if field_model_path is None else field_model_path,
                              '__' + criteria[0]['CriteriaSymbol'] if criteria is not None else None):
                    filter_value['value']}), Q.AND)
        '''
        if len(criteria) == 0:
            if field_model_path is None:
                condition.add(Q(**{field_name: filter_value['value']}), Q.AND)
            else:
                condition.add(~Q(**{field_model_path: filter_value['value']}), Q.AND)

        elif criteria[0]['IsExcludeCondition']:
            if field_model_path is None:
                exclude_condition.add(Q(**{'{}{}'.format(field_name, '__'+criteria[0]['CriteriaSymbol'] if criteria is not None else None): filter_value['value']}), Q.AND)
            else:
                exclude_condition.add(~Q(**{
                    '{}{}'.format(field_model_path, '__' + criteria[0]['CriteriaSymbol'] if criteria is not None else None):
                        filter_value['value']}), Q.AND)
        else:
            if field_model_path is None:
                condition.add(Q(**{'{}{}'.format(field_name, '__'+criteria[0]['CriteriaSymbol'] if criteria is not None else None): filter_value['value']}), Q.AND)
            else:
                condition.add(~Q(**{
                    '{}{}'.format(field_model_path, '__' + criteria[0]['CriteriaSymbol'] if criteria is not None else None):
                        filter_value['value']}), Q.AND)
        '''
    base_parties = BaseParty.objects.prefetch_related('BasePartyCreditApplication').filter(condition). \
        exclude(exclude_condition).select_related('HostId', 'BasePartyType', 'ProfileType', 'FinancialInstitution',
                                                  'BusinessUnit', 'CRMPortfolio', 'CRMStrategy', 'PrimaryEmailId',
                                                  'PrimaryTelephoneId', 'PrimaryContactId', 'ApplicationSummary',
                                                  'BankingSummary', 'FinancialsSummary', 'Individual',
                                                  'OtherInformation', 'RatingSummary', 'relatedstaff')
    print(base_parties)
    qs_json = serializers.serialize('json', base_parties)
    print(qs_json, file=open('D:/filename.txt', 'w+'))
    return qs_json
