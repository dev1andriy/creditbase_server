def return_value_or_none(dictionary, value):
    return dictionary.get(value, None) if dictionary is not None else None


def return_deep_value_or_none(dictionary, value_key, value):
    nested_dictionary = dictionary.get(value_key, None) if dictionary is not None else None
    return dict.get(value, None) if nested_dictionary is not None else None

