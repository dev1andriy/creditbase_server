from django.apps import apps
from common.models import ArrangementParamMatrix, ArrangementParam
from common.serializers.other import DynamicModelSerializer
from common.utils.generate_request_type_param import generate_request_type_param

field_types = ['Numeric', 'Text', 'Float', 'Date', 'Combo']


def generate_params(data_view, arrangement_type, request_type, instance=None):
    if request_type is not None:
        arrangement_param_matrixes = ArrangementParamMatrix.objects.filter(ArrangementType_id=arrangement_type, RequestType_id=request_type)
        params_to_display = [generate_request_type_param(request_type)]
    else:
        arrangement_param_matrixes = ArrangementParamMatrix.objects.filter(ArrangementType_id=arrangement_type)
        params_to_display = []

    arrangement_params = ArrangementParam.objects.filter(ArrangementParamId__in=list(arrangement_param_matrixes.values_list("ArrangementParamId", flat=True)))

    for param in arrangement_params:
        matrix = arrangement_param_matrixes.filter(ArrangementParamId_id=param.ArrangementParamId).first()

        if matrix.DisplayFlag['DataView{}'.format(data_view)] == 1:
            if instance is None:
                generated_param = generate_param_row_without_data(param, matrix, data_view)

                params_to_display.append(generated_param)
            elif instance is not None and param.Name4 in instance and instance[param.Name4] is not None:
                generated_param = generate_param_row_with_data(param, matrix, data_view, instance)

                params_to_display.append(generated_param)

    return params_to_display


def generate_param_row_without_data(param, matrix, data_view):
    modify_flag = matrix.ModifyFlag['DataView{}'.format(data_view)]

    param_row = {
        'required': param.Mandatory,
        'name': param.Name4,
        'parameterCategory': param.ArrangementParamCategory.Description if param.ArrangementParamCategory is not None else None,
        'parameterName': {
            'value': param.Name2,
            'color': '#707070'
        },
        'hostValue': {
            'config': generate_param_row_config(param, matrix, modify_flag),
            'data': 'No change' if modify_flag == 0 else matrix.ValueLimits.get('Default', None) if matrix.ValueLimits is not None else None,
        },
        'modify': {
            'statesAmount': 2,
            'rewritable': True if modify_flag == 1 else False,
            'data': modify_flag
        },
        'proposedValue': {
            'config': generate_param_row_config(param, matrix, modify_flag),
            'data': 'No change' if modify_flag == 0 else matrix.ValueLimits.get('Default', None) if matrix.ValueLimits is not None else None
        },
        'print': {
            'statesAmount': 3,
            'rewritable': True,
            'data': matrix.PrintFlag['DataView{}'.format(data_view)]
        }
    }

    return param_row


def generate_param_row_with_data(param, matrix, data_view, instance):
    modify_flag = matrix.ModifyFlag['DataView{}'.format(data_view)]

    parameter_data = instance[param.Name4]

    print(parameter_data, type(parameter_data))

    param_row = {
        'required': param.Mandatory,
        'name': param.Name4,
        'parameterCategory': param.ArrangementParamCategory.Description if param.ArrangementParamCategory is not None else None,
        'parameterName': {
            'value': param.Name2,
            'color': '#707070'
        },
        'hostValue': {
            'config': generate_param_row_config(param, matrix, modify_flag),
            'data': 'No change' if modify_flag == 0 else parameter_data['HostValue']
        },
        'modify': {
            'statesAmount': 2,
            'rewritable': True if modify_flag == 1 else False,
            'data': parameter_data['ModifyFlag']
        },
        'proposedValue': {
            'config': generate_param_row_config(param, matrix, modify_flag),
            'data': 'No change' if modify_flag == 0 else parameter_data['ProposedValue']
        },
        'print': {
            'statesAmount': 3,
            'rewritable': True,
            'data': parameter_data['PrintFlag']
        }
    }

    return param_row


def generate_param_row_config(param, matrix, modify_flag):
    if modify_flag == 0:
        return {
            'type': 'readOnly',
            'inputType': None,
        }

    return {
        1: {
            'type': 'input',
            'inputType': 'number',
            'minValue': matrix.ValueLimits.get('Lower') if matrix.ValueLimits is not None else None,
            'maxValue': matrix.ValueLimits.get('Upper') if matrix.ValueLimits is not None else None,
        },
        2: {
            'type': 'input',
            'inputType': 'text',
        },
        3: {
            'type': 'input',
            'inputType': 'number',
            'minValue': matrix.ValueLimits.get('Lower') if matrix.ValueLimits is not None else None,
            'maxValue': matrix.ValueLimits.get('Upper') if matrix.ValueLimits is not None else None,
        },
        4: {
            'type': 'input',
            'inputType': 'date',
        },
        5: {
            'type': 'select',
            'options': DynamicModelSerializer(apps.get_registered_model('common', param.Description).objects.all(), many=True, value_field=param.Description1, label_field=param.Description2, model=param.Description).data if param.Description is not None and param.Description1 is not None and param.Description2 is not None else None
        },
        None: {
            'type': 'input',
            'inputType': 'text',
        },
    }[param.FieldType]
