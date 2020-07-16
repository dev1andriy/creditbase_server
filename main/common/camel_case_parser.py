import collections


def to_camel_case(data):
    new_dict = {}
    for item in data:
        if type(data[item]) == collections.OrderedDict:
            for sub_item in data[item]:
                print(sub_item)
                if type(data[item][sub_item]) == collections.OrderedDict:
                    to_camel_case(item[sub_item])
                elif type(data[item][sub_item]) == list:
                    to_camel_case(item[sub_item])
                else:
                    if sub_item.upper() != sub_item:
                        temp_key = list(sub_item)
                        temp_key[0] = temp_key[0].upper()
                        new_key = "".join(temp_key)
                        new_dict[item][new_key] = data[item][sub_item]
        elif type(data[item]) == list:
            for sub_item in item:
                to_camel_case(sub_item)
    return new_dict


class CamelCaseParser():
    def to_camel_case_nested_object(data):
        new_list = []

        for item in data:
            temp_item = dict()

            for key in data[item]:
                if key.upper() != key:
                    temp_key = list(key)
                    temp_key[0] = temp_key[0].lower()
                    new_key = "".join(temp_key)
                    temp_item[new_key] = item[key]

            new_list.append(temp_item)

        return new_list

    def from_camel_case_nested_object(data):
        new_list = []

        for item in data:
            temp_item = dict()

            for key in item:
                if key.upper() != key:
                    temp_key = list(key)
                    temp_key[0] = temp_key[0].upper()
                    new_key = "".join(temp_key)
                    temp_item[key] = item[key]

            new_list.append(temp_item)

        return new_list

    def to_camel_case_array(data):
        new_list = []

        for item in data:
            temp_item = dict()
            for key in item:
                if key.upper() != key:
                    temp_key = list(key)
                    temp_key[0] = temp_key[0].lower()
                    new_key = "".join(temp_key)
                    temp_item[new_key] = item[key]
                else:
                    new_list[key] = data[key]

            new_list.append(temp_item)

        return new_list

    def from_camel_case_array(data):
        new_list = []

        for item in data:
            temp_item = dict()

            for key in item:
                if key.upper() != key:
                    temp_key = list(key)
                    temp_key[0] = temp_key[0].upper()
                    new_key = "".join(temp_key)
                    temp_item[new_key] = item[key]
                else:
                    new_list[key] = data[key]

            new_list.append(temp_item)

        return new_list

    def to_camel_case_single(data):
        new_list = dict()
        for key in data:
            if key.upper() != key:
                temp_key = list(key)
                temp_key[0] = temp_key[0].lower()
                new_key = "".join(temp_key)
                new_list[new_key] = data[key]
            else:
                new_list[key] = data[key]

        return new_list

    def from_camel_case_single(data):
        new_list = dict()

        for key in data:
            if key.upper() != key:
                temp_key = list(key)
                temp_key[0] = temp_key[0].upper()
                new_key = "".join(temp_key)
                new_list[new_key] = data[key]
            else:
                new_list[key] = data[key]


        return new_list

    def to_camel_case(self, data):
        pass
