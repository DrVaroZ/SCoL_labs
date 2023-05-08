import inspect
import types
from types import CodeType, FunctionType
from pydoc import locate

from serializers.source.constants import *


def get_type(item):
    item_type = str(type(item))

    return item_type[8:len(item_type) - 2]


def serialize(item):
    if isinstance(item, (int, float, complex, bool, str, type(None))):
        return serialize_single_var(item)
    elif isinstance(item, (list, tuple, set, bytes)):
        return serialize_collection(item)
    elif isinstance(item, dict):
        return serialize_dict(item)
    elif inspect.isfunction(item):
        return serialize_function(item)
    elif inspect.isclass(item):
        return serialize_class(item)
    elif inspect.iscode(item):
        return serialize_code(item)
    elif inspect.ismodule(item):
        return serialize_module(item)
    elif inspect.ismethoddescriptor(item) or inspect.isbuiltin(item):
        return serialize_instance(item)
    elif inspect.isgetsetdescriptor(item) or inspect.ismemberdescriptor(item):
        return serialize_instance(item)
    elif isinstance(item, type(type.__dict__)):
        return serialize_instance(item)
    else:
        return serialize_object(item)


def serialize_single_var(item):
    serialized_dict = {TYPE: get_type(item), VALUE: item}

    return serialized_dict


def serialize_collection(item):
    serialized_dict = {TYPE: get_type(item), VALUE: [serialize(obj) for obj in item]}

    return serialized_dict


def serialize_dict(item):
    serialized_dict = {TYPE: get_type(item), VALUE: [[serialize(key), serialize(item[key])] for key in item]}

    return serialized_dict


def serialize_function(item):
    members = inspect.getmembers(item)
    serialized = dict()
    serialized['type'] = str(type(item))[8:-2]
    value = dict()

    for tmp in members:
        if tmp[0] in ['__code__', '__name__', '__defaults__']:
            value[tmp[0]] = (tmp[1])
        if tmp[0] == '__code__':
            co_names = tmp[1].__getattribute__('co_names')
            globs = item.__getattribute__('__globals__')
            value['__globals__'] = dict()

            for tmp_co_names in co_names:
                if tmp_co_names == item.__name__:
                    value['__globals__'][tmp_co_names] = item.__name__
                elif not inspect.ismodule(tmp_co_names) \
                        and tmp_co_names in globs:
                    # and tmp_co_names not in __builtins__:
                    value['__globals__'][tmp_co_names] = globs[tmp_co_names]

    serialized['value'] = serialize(value)

    return serialized


def serialize_class(item):
    serialized_dict = {TYPE: CLASS}
    value = {NAME: item.__name__}
    members = inspect.getmembers(item)
    for obj in members:
        if not (obj[0] in NOT_CLASS_ATTRIBUTES):
            value[obj[0]] = obj[1]
    serialized_dict[VALUE] = serialize(value)

    return serialized_dict


def serialize_code(item):
    if get_type(item) is None:
        return None

    members = inspect.getmembers(item)
    serialized_dict = {TYPE: get_type(item), VALUE: serialize({obj[0]: obj[1] for obj in members if not callable(obj[1])})}

    return serialized_dict


def serialize_module(item):
    temp_item = str(item)
    serialized_dict = {TYPE: get_type(item), VALUE: temp_item[9:len(temp_item) - 13]}

    return serialized_dict


def serialize_instance(item):
    members = inspect.getmembers(item)
    serialized_dict = {TYPE: get_type(item), VALUE: serialize({obj[0]: obj[1] for obj in members if not callable(obj[1])})}

    return serialized_dict


def serialize_object(item):
    serialized_dict = {TYPE: OBJECT, VALUE: serialize({OBJECT_TYPE: type(item), FIELDS: item.__dict__})}

    return serialized_dict


def deserialize(item):
    if item[TYPE] in [INT, FLOAT, BOOL, STRING, COMPLEX, NONE_TYPE]:
        return deserialize_single_var(item)
    elif item[TYPE] in [LIST, TUPLE, SET, BYTES]:
        return deserialize_collection(item)
    elif item[TYPE] == DICT:
        return deserialize_dict(item)
    elif item[TYPE] == FUNCTION:
        return deserialize_function(item)
    elif item[TYPE] == CLASS:
        return deserialize_class(item)
    elif item[TYPE] == MODULE:
        return deserialize_module(item)
    elif item[TYPE] == OBJECT:
        return deserialize_object(item)


def deserialize_single_var(item):
    if item[TYPE] == NONE_TYPE:
        return None
    elif item[TYPE] == BOOL and isinstance(item[VALUE], str):
        return item[VALUE] == TRUE
    else:
        return locate(item[TYPE])(item[VALUE])


def deserialize_collection(item):
    if item[TYPE] == LIST:
        return list(deserialize(obj) for obj in item[VALUE])
    elif item[TYPE] == TUPLE:
        return tuple(deserialize(obj) for obj in item[VALUE])
    elif item[TYPE] == SET:
        return set(deserialize(obj) for obj in item[VALUE])
    elif item[TYPE] == BYTES:
        return bytes(deserialize(obj) for obj in item[VALUE])


def deserialize_dict(item):
    return {deserialize(obj[0]): deserialize(obj[1]) for obj in item[VALUE]}


def deserialize_function(item):
    res_dict = deserialize(item['value'])

    res_dict['code'] = deserialize_code(item)
    res_dict.pop('__code__')

    res_dict['globals'] = res_dict['__globals__']
    res_dict.pop('__globals__')

    res_dict['name'] = res_dict['__name__']
    res_dict.pop('__name__')

    res_dict['argdefs'] = res_dict['__defaults__']
    res_dict.pop('__defaults__')

    res = types.FunctionType(**res_dict)
    if res.__name__ in res.__getattribute__('__globals__'):
        res.__getattribute__('__globals__')[res.__name__] = res

    return res


def deserialize_code(item):
    items = item['value']['value']

    for tmp in items:
        if tmp[0]['value'] == '__code__':
            args = deserialize(tmp[1]['value'])
            code_dict = dict()
            for arg in args:
                arg_val = args[arg]
                if arg != '__doc__':
                    code_dict[arg] = arg_val
            code_list = [0] * 16

            for name in code_dict:
                if name == 'co_lnotab':
                    continue
                code_list[CODE_ARGS.index(name)] = code_dict[name]

            return types.CodeType(*code_list)


def deserialize_class(item):
    class_dict = deserialize(item[VALUE])
    name = class_dict[NAME]
    del class_dict[NAME]

    return type(name, (object,), class_dict)


def deserialize_module(item):
    return __import__(item[VALUE])


def deserialize_object(item):
    value = deserialize(item[VALUE])
    result = value[OBJECT_TYPE](**value[FIELDS])

    for key, value in value[FIELDS].items():
        result.key = value

    return result
