import inspect
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
    serialized_dict = {TYPE: get_type(item)}
    value = {}
    for obj in members:
        if obj[0] in FUNCTION_ATTRIBUTES:
            value[obj[0]] = (obj[1])
        if obj[0] == CODE:
            co_names = obj[1].__getattribute__(CO_NAMES)
            globs = item.__getattribute__(GLOBALS)
            value[GLOBALS] = {}
            for obj2 in co_names:
                if obj2 == item.__name__:
                    value[GLOBALS][obj2] = item.__name__
                elif obj2 in globs and not inspect.ismodule(obj2) and obj2 not in __builtins__:
                    value[GLOBALS][obj2] = globs[obj2]
    serialized_dict[VALUE] = serialize(value)

    return serialized_dict


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
    if item[TYPE] in [FLOAT, INT, COMPLEX, NONE_TYPE, BOOL, STRING]:
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
    pass


def deserialize_class(item):
    pass


def deserialize_module(item):
    return __import__(item[VALUE])


def deserialize_object(item):
    pass
