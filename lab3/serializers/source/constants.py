TYPE = "type"
VALUE = "value"
GLOBALS = "__globals__"
CODE = "__code__"
NAME = "__name__"
CLASS = "class"
FLOAT = "float"
INT = "int"
NONE_TYPE = "NoneType"
COMPLEX = "complex"
BOOL = "bool"
STRING = "str"
LIST = "list"
TUPLE = "tuple"
BYTES = "bytes"
SET = "set"
DICT = "dict"
CO_NAMES = "co_names"
OBJECT = "object"
FIELDS = "__fields__"
OBJECT_TYPE = "__object_type__"
MODULE = "module"
BUILTINS = "__builtins__"
DOC = "__doc__"
FUNCTION = "function"
DEFAULTS = "__defaults__"
TRUE = "True"

FUNC_ATTRIBUTES = [
    "__code__",
    "__name__",
    "__defaults__"
]

NOT_CLASS_ATTRIBUTES = [
    "__class__",
    "__getattribute__",
    "__new__",
    "__setattr__",
]

CODE_ARGS = [
    'co_argcount',
    'co_posonlyargcount',
    'co_kwonlyargcount',
    'co_nlocals',
    'co_stacksize',
    'co_flags',
    'co_code',
    'co_consts',
    'co_names',
    'co_varnames',
    'co_filename',
    'co_name',
    'co_firstlineno',
    'co_lnotab',
    'co_freevars',
    'co_cellvars'
]
