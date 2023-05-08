TYPE = "type"
VALUE = "value"

INT = "int"
FLOAT = "float"
BOOL = "bool"
STRING = "str"
COMPLEX = "complex"
NONE_TYPE = "NoneType"

LIST = "list"
TUPLE = "tuple"
SET = "set"
BYTES = "bytes"

DICT = "dict"

FUNCTION = "function"

CLASS = "class"
OBJECT = "object"
CO_NAMES = "co_names"
FIELDS = "__fields__"
OBJECT_TYPE = "__object_type__"

MODULE = "module"

GLOBALS = "__globals__"
CODE = "__code__"
NAME = "__name__"

BUILTINS = "__builtins__"
DOC = "__doc__"
DEFAULTS = "__defaults__"
TRUE = "True"

FUNCTION_ATTRIBUTES = [
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
    'co_linetable',
    'co_freevars',
    'co_cellvars'
]
