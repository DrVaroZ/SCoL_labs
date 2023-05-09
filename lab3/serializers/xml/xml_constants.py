KEY_GROUP_NAME = "key"
VALUE_GROUP_NAME = "value"
ELEMENTARY_NAMES_PATTERN = "int|float|bool|str|NoneType|list|dict"

XML_SCHEME_PATTERN = "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " + \
                     "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\""

XML_ELEMENT_PATTERN = fr"(\<(?P<{KEY_GROUP_NAME}>{ELEMENTARY_NAMES_PATTERN})\>" + \
                      fr"(?P<{VALUE_GROUP_NAME}>([^<>]*)|(?R)+)\</(?:{ELEMENTARY_NAMES_PATTERN})\>)"

FIRST_XML_ELEMENT_PATTERN = fr"(\<(?P<{KEY_GROUP_NAME}>{ELEMENTARY_NAMES_PATTERN})\s*({XML_SCHEME_PATTERN})?\>" + \
                            fr"(?P<{VALUE_GROUP_NAME}>([^<>]*)|(?R)+)\</(?:{ELEMENTARY_NAMES_PATTERN})\>)"
