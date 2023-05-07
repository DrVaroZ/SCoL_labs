import inspect

from serializers.source.constants import *


def get_type(item):
    item_type = str(type(item))

    return item_type[8:len(item_type) - 2]


def serialize(item):
    if isinstance(item, (int, float, complex, bool, str, type(None))):
        return serialize_single_var(item)
    if isinstance(item, (list, tuple, set, bytes)):
        return serialize_collection(item)
    if isinstance(item, dict):
        return serialize_dict(item)
    if inspect.isfunction(item):
        return serialize_function(item)
    if inspect.isclass(item):
        return serialize_class(item)
    if inspect.iscode(item):
        return serialize_code(item)
    if inspect.ismodule(item):
        return serialize_module(item)
    if inspect.ismethoddescriptor(item) or inspect.isbuiltin(item):
        return serialize_instance(item)
    if inspect.isgetsetdescriptor(item) or inspect.ismemberdescriptor(item):
        return serialize_instance(item)
    if isinstance(item, type(type.__dict__)):
        return serialize_instance(item)

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
        if obj[0] in FUNC_ATTRIBUTES:
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
